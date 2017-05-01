import pygame

import sys

from math import fabs

from random import randint

from pygame.sprite import Group, groupcollide

from Harry_Potter import Harry_Potter

from Peter_Pettigrew import Peter_Pettigrew

from Dolores_Umbridge import Dolores_Umbridge

from Lucius_Malfoy import Lucius_Malfoy

from Lord_Voldemort import Lord_Voldemort

### Start the Game ###
pygame.init()


### Screen/Display Properties ###


screen = {
	"height": 450,
	"width": 750
}
screen_size = (screen["width"], screen["height"])
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("The Battle of Hogwarts")




### Game Functions ###
pygame.mixer.music.load('./sounds/HP-theme.wav')
pygame.mixer.music.play(-1)



keys = {
	"right": 275,
	"left": 276,
	"up": 273,
	"down": 274
}

keys_down = {
	"right": False,
	"left": False,
	"up": False,
	"down": False
}

debuff = {
	"x": 250,
    "y": 250
}


direction = [
	"N", "S", "E", "W", "NE", "NW", "SE", "SW"

]

Harry_Potter = Harry_Potter(pygame_screen)
Peter_Pettigrew = Peter_Pettigrew(pygame_screen)
Dolores_Umbridge = Dolores_Umbridge(pygame_screen)
Lucius_Malfoy = Lucius_Malfoy(pygame_screen)
Lord_Voldemort = Lord_Voldemort(pygame_screen)


Heroes = Group()
Heroes.add(Harry_Potter)
Villains = Group()
Villains.add(Peter_Pettigrew)	


### Start Screen. ###
game_start = False	

while (game_start==False):

	background_image = pygame.image.load('./images/start_screen.png')
	myfont=pygame.font.SysFont("Edwardian Script ITC", 40)
	nlabel3= myfont.render("&", 1, (190, 190, 190))
	nlabel2=myfont.render("The Battle of Hogwarts", 1, (190, 190, 190))
	nlabel = pygame.image.load('./images/Letters.png')
	for event in pygame.event.get():
		if event.type== pygame.KEYDOWN:
			game_start=True

	pygame_screen.blit(background_image, [0,0])
	pygame_screen.blit(nlabel,(275,100))
	pygame_screen.blit(nlabel2,(240, 260))
	pygame_screen.blit(nlabel3,(385, 215))
	pygame.display.flip()



###     Main Game Loop Begins here.   ###

tick = 0
game_on = True
enemy_level = 1

while game_on:

	background_image = pygame.image.load('./images/Battle_Screen.png')
	pygame_screen.blit(background_image, [0,0])

	font = pygame.font.Font(None, 25)
	wins_text = font.render("Avada Kedavra: %d" % (Harry_Potter.location['Avada Kedavra']), True, (0,0,0))
	pygame_screen.blit(wins_text, [40,40])

	debuff_image = pygame.image.load('./images/butterbeer.png')
	pygame_screen.blit(debuff_image, [debuff['x'], debuff['y']])

	Harry_Potter.draw_me()
	
	for Villain in Villains:
		Villain.draw_me()


	tick +=1
	# print tick
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_on = False
		if event.type == pygame.KEYDOWN:
			if event.key == keys ['up']:
				keys_down['up'] = True
			if event.key == keys ['down']:
				keys_down['down'] = True
			if event.key == keys ['left']:
				keys_down ['left'] = True
			if event.key == keys ['right']:
				keys_down ['right'] = True

		elif event.type == pygame.KEYUP:
			if event.key == keys ['up']:
				keys_down['up'] = False
			if event.key == keys ['down']:
				keys_down['down'] = False
			if event.key == keys ['left']:
				keys_down['left'] = False
			if event.key == keys ['right']:
				keys_down['right'] = False

	distance_between = fabs(Harry_Potter.location['x'] - debuff['x']) + fabs(Harry_Potter.location['y'] - debuff['y'])
	if (distance_between < 32):
		rand_X = randint(0, screen['width'])
		rand_Y = randint(0, screen['height'])
		debuff['x'] = rand_X
		debuff['y'] = rand_Y

		Harry_Potter.location['speed'] -= 2
			


	Harry_Potter.move(keys_down, screen)
	Peter_Pettigrew.move(direction, screen, tick)
	Dolores_Umbridge.move(direction,screen, tick)
	Lucius_Malfoy.move(direction, screen, tick)
	Lord_Voldemort.move(direction, screen, tick)
	

	enemy_dies  = groupcollide(Heroes, Villains, False, True)

	pygame.display.flip()

	if enemy_dies:
		print enemy_level

		enemy_level += 1

		if enemy_level == 2:
			Villains.add(Dolores_Umbridge)
			Harry_Potter.location['Avada Kedavra'] += 1
			print "level 2"
			
		if enemy_level == 3:
			Villains.add(Lucius_Malfoy)
			Harry_Potter.location['Avada Kedavra'] += 1
			print "level 3"


		if enemy_level == 4:
			Villains.add(Lord_Voldemort)
			Harry_Potter.location['Avada Kedavra'] += 1
			print "level 4"

		if enemy_level == 5:
			game_on = False

			### debuff ###


gameOver = True

while gameOver:
	background_image = pygame.image.load('./images/Happy.jpg')
	myfont=pygame.font.SysFont("Edwardian Script ITC", 40)
	nlabel3= myfont.render("CONGRATULATIONS!", 1, (255, 255, 0))
	nlabel2=myfont.render("You defeated the Death Eaters!", 1, (255, 255, 0))
	nlabel = pygame.image.load('./images/Letters.png')
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_on = False

	pygame_screen.blit(background_image, [0,0])
	pygame_screen.blit(nlabel,(20,20))
	pygame_screen.blit(nlabel2,(30, 160))
	pygame_screen.blit(nlabel3,(25, 10))
	pygame.display.flip()



			
			




