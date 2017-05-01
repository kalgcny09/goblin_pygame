import pygame

from math import fabs

from random import randint

from pygame.sprite import Sprite

class Lord_Voldemort(Sprite):

	def __init__ (self, screen):
		super(Lord_Voldemort, self).__init__()	
		self.location = {
							"x": 335,
							"y": 385,
							"speed": 10,
							"direction": "SE"
						}
		self.image = pygame.image.load('./images/Lord_Voldemort.png')
		self.rect = self.image.get_rect()
		self.screen = screen

	def move (self, direction, screen, tick):
		if 	(self.location["direction"]) == "N":
				self.location['y'] -= self.location['speed']
		elif self.location["direction"] == "S":
			self.location['y'] += self.location['speed']
		elif self.location["direction"] == "E":
			self.location['x'] += self.location['speed']
		elif self.location["direction"] == "W":
			self.location['x'] -= self.location['speed']


		elif self.location["direction"] == "NE":
			self.location['y'] -= self.location['speed']
			self.location['x'] += self.location['speed']
		elif self.location["direction"] == "NW":
			self.location['y'] -= self.location['speed']
			self.location['y'] -= self.location['speed']
		elif self.location["direction"] == "SE":
			self.location['y'] += self.location['speed']
			self.location['x'] += self.location['speed']
		elif self.location["direction"] == "SW":
			self.location['y'] += self.location['speed']
			self.location['x'] -= self.location['speed']

		## To keep the villian from moving outside the screen
		if (self.location['x'] > screen['width']):
			self.location['x'] = 0
		elif (self.location['x'] < 0):
			self.location['x'] = screen['width']
		if (self.location['y'] > screen['height']):
			self.location['y'] = 0
		elif (self.location['y'] < 0):
			self.location['y'] = screen['height']

		### New Direction. ###
		
		if tick % 60 == 0:
			new_dir_index = randint(0, len(direction)-1)
			self.location["direction"] = direction[new_dir_index]
			print tick

		self.rect.left = self.location["x"]
		self.rect.top = self.location["y"]
		# print self.rect


	def draw_me(self):
		self.rect.left = self.location["x"]
		self.rect.top = self.location["y"]
		self.screen.blit(self.image, [self.location["x"], self.location["y"]])