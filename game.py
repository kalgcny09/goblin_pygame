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
	"speed": 1,
	"direction": "N"
}

power_up = {
	"x": 250,
	"y": 250

}
direction = [
	"N", "S", "E", "W", "NE", "NW", "SE", "SW"



]	

screen_size = (screen["height"], screen["width"])
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("monster Chase")

background_image = pygame.image.load('./images/battle1.png')

hero_image = pygame.image.load('./images/hp.png')

monster_image = pygame.image.load('./images/LV.png')
monster_image_scaled = pygame.transform.scale(monster_image, (50, 50))

power_up_image = pygame.image.load('./images/butterbeer.png')

pygame.mixer.music.load('./sounds/music.wav')
pygame.mixer.music.play(-1)

tick = 0

####Main Game Loop Begins here

game_on = True

while game_on:
	tick +=1
	print tick
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

### update hero's position
	if keys_down['up']:
		hero['y'] -= hero['speed']
	elif keys_down['down']:
		hero['y'] += hero['speed']
	if keys_down['left']:
		hero['x'] -= hero['speed']
	elif keys_down['right']:
		hero['x'] += hero['speed']



	#Update monster position
	if (monster["direction"]) == "N":
			monster['y'] -= monster['speed']
	elif	monster["direction"] == "S":
			monster['y'] += monster['speed']
	elif	monster["direction"] == "E":
			monster['x'] += monster['speed']
	elif    monster["direction"] == "W":
			monster['x'] -= monster['speed']
	elif    monster["direction"] == "NE":
			monster['y'] -= monster['speed']
			monster['x'] += monster['speed']
	elif    monster["direction"] == "NW":
			monster['y'] -= monster['speed']
			monster['y'] -= monster['speed']
	elif    monster["direction"] == "SE":
			monster['y'] += monster['speed']
			monster['x'] += monster['speed']
	elif    monster["direction"] == "SW":
			monster['y'] += monster['speed']
			monster['x'] -= monster['speed']



	if tick % 60 == 0:
		new_dir_index = randint(0, len(direction)-1)
		monster['direction'] = direction[new_dir_index]

	if (monster['x'] > screen['width']):
		monster['x'] = 0
	elif (monster['x'] < 0):
		monster['x'] = screen['width']
	if (monster['y'] > screen['height']):
		monster['y'] = 0
	elif (monster['y'] < 0):
		monster['y'] = screen['height']

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


