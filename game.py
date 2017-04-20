import pygame

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
	"speed": 10
}


screen_size = (screen["height"], screen["width"])
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Goblin Chase")
background_image = pygame.image.load('./images/background.png')
hero_image = pygame.image.load('./images/hero.png')



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

	pygame_screen.blit(hero_image, [hero['x'], hero['y']])

	pygame.display.flip()