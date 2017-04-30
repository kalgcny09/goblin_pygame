import pygame

import sys

from math import fabs

from random import randint

from pygame.sprite import Group, groupcollide

from Harry_Potter import Harry_Potter

from Peter_Pettigrew import Peter_Pettigrew

from Dolores_Umbridge import Dolores_Umbridge

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

direction = [
	"N", "S", "E", "W", "NE", "NW", "SE", "SW"

]

Harry_Potter = Harry_Potter(pygame_screen)
Peter_Pettigrew = Peter_Pettigrew(pygame_screen)
Dolores_Umbridge = Dolores_Umbridge(pygame_screen)


Heroes = Group()
Heroes.add(Harry_Potter)
Villains = Group()
Villains.add(Peter_Pettigrew)	


### Start Screen. ###
game_start = True

while (game_start==True):

	background_image = pygame.image.load('./images/start_screen.png')
	myfont=pygame.font.SysFont("Edwardian Script ITC", 40)
	nlabel3= myfont.render("&", 1, (190, 190, 190))
	nlabel2=myfont.render("The Battle of Hogwarts", 1, (190, 190, 190))
	nlabel = pygame.image.load('./images/Letters.png')
	for event in pygame.event.get():
		if event.type== pygame.KEYDOWN:
			game_start=False

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
	Harry_Potter.draw_me()
	
	for Villain in Villains:
		Villain.draw_me()




	tick +=1
	# print tick
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_on = False
		elif event.type == pygame.KEYDOWN:
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




	Harry_Potter.move(keys_down, screen)
	Peter_Pettigrew.move(direction, screen, tick)
	Dolores_Umbridge.move(direction,screen, tick)
	

	enemy_dies  = groupcollide(Heroes, Villains, False, True)

	pygame.display.flip()

	if enemy_dies:
		print enemy_level

		enemy_level += 1

		if enemy_level == 2:
			Villains.add(Dolores_Umbridge)
			
		# if enemy_level == 3:




			
			
		# Harry_Potter['wins'] += 1

		# distance_between = fabs(Harry_Potter.location['x'] - Peter_Pettigrew.location['x']) + fabs(Harry_Potter.location['y'] - Peter_Pettigrew.location['y'])
		# # defeat = 0
		# if (distance_between < 50):
		# 	rand_X = randint(0, screen['width'])
		# 	rand_Y = randint(0, screen['height'])
		# 	Peter_Pettigrew.location['x'] = rand_X
		# 	Peter_Pettigrew.location['y'] = rand_Y


# debuff = {
# 	"x": 250,
# 	"y": 250


# 	## debuff
# distance_between = fabs(Harry_Potter['x'] - debuff['x']) + fabs(Harry_Potter['y'] - debuff['y'])
# if (distance_between < 32):
# 	rand_X = randint(0, screen['width'])
# 	rand_Y = randint(0, screen['height'])
# 	debuff['x'] = rand_X
# 	debuff['y'] = rand_Y

# 	Harry_Potter['speed'] -= 5


