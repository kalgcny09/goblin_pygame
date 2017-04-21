import pygame

from math import fabs

from random import randint

from pygame.sprite import spritecollide

pygame.init()

screen = {
	"height": 512,
	"width": 480
}

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


hero = {
	"x": 100,
	"y": 100,
	"speed": 10,
	"wins": 0
}

monster = {
	"x": 300,
	"y": 300,
	"speed": 20
}

power_up = {
	"x": 250,
	"y": 250

}


screen_size = (screen["height"], screen["width"])
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Goblin Chase")

background_image = pygame.image.load('./images/battle1.png')

hero_image = pygame.image.load('./images/hero.png')

monster_image = pygame.image.load('./images/LV.png')
monster_image_scaled = pygame.transform.scale(monster_image, (50, 50))

power_up_image = pygame.image.load('./images/butterbeer.png')

pygame.mixer.music.load('./sounds/music.wav')
pygame.mixer.music.play(-1)


####Main Game Loop Begins here

game_on = True

while game_on:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_on = False
		elif event.type == pygame.KEYDOWN:
			if event.key == keys ['up']:
				keys_down['up'] = True
				#hero['y'] -= hero['speed']
			if event.key == keys ['down']:
				keys_down['down'] = True
				#hero['y'] += hero['speed']
			if event.key == keys ['left']:
				keys_down ['left'] = True
				#hero['x'] -= hero['speed']
			if event.key == keys ['right']:
				keys_down ['right'] = True
				#hero['x'] += hero['speed']
		elif event.type == pygame.KEYUP:
			if event.key == keys ['up']:
				keys_down['up'] = False
			if event.key == keys ['down']:
				keys_down['down'] = False
			if event.key == keys ['left']:
				keys_down['left'] = False
			if event.key == keys ['right']:
				keys_down['right'] = False


	if keys_down['up']:
		hero['y'] -= hero['speed']
	elif keys_down['down']:
		hero['y'] += hero['speed']
	if keys_down['left']:
		hero['x'] -= hero['speed']
	elif keys_down['right']:
		hero['x'] += hero['speed']

	### Render (these items layer so background should be first)
	pygame_screen.blit(background_image, [0,0])

	font = pygame.font.Font(None, 25)
	wins_text = font.render("wins: %d" % (hero['wins']), True, (0,0,0))
	pygame_screen.blit(wins_text, [40,40])

	pygame_screen.blit(hero_image, [hero['x'], hero['y']])

	pygame_screen.blit(monster_image, [monster['x'], monster['y']])

	pygame_screen.blit(power_up_image, [power_up['x'], power_up['y']])

	pygame.display.flip()


	## collision detection
	distance_between = fabs(hero['x'] - monster['x']) + fabs(hero['y'] - monster['y'])
	if (distance_between < 32):
		rand_X = randint(0, screen['width'])
		rand_Y = randint(0, screen['height'])
		monster['x'] = rand_X
		monster['y'] = rand_Y

		hero['wins'] += 1



	## Coin Power up
	distance_between = fabs(hero['x'] - power_up['x']) + fabs(hero['y'] - power_up['y'])
	if (distance_between < 32):
		rand_X = randint(0, screen['width'])
		rand_Y = randint(0, screen['height'])
		power_up['x'] = rand_X
		power_up['y'] = rand_Y

		hero['speed'] -= 5


