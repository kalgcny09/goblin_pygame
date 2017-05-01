import pygame

from pygame.sprite import Sprite



class Harry_Potter(Sprite):
	def __init__ (self, screen):
		super(Harry_Potter, self).__init__()	
		self.location = {
							"x": 100,
							"y": 100,
							"speed": 10,
							"Avada Kedavra": 0
						}
		self.image = pygame.image.load('./images/Harry_Potter.png')
		self.rect = self.image.get_rect()
		self.screen = screen

	def move (self, keys_down, screen):
		if keys_down['up']:
			self.location['y'] -= self.location['speed']
		elif keys_down['down']:
			self.location['y'] += self.location['speed']
		if keys_down['left']:
			self.location['x'] -= self.location['speed']
		elif keys_down['right']:
			self.location['x'] += self.location['speed']

		### Harry's Limits ###
		if (self.location['x'] > screen['width']):
			self.location['x'] = 0
		elif (self.location['x'] < 0):
			self.location['x'] = screen['width']
		if (self.location['y'] > screen['height']):
			self.location['y'] = 0
		elif (self.location['y'] < 0):
			self.location['y'] = screen['height']

	def draw_me(self):
		self.rect.left = self.location["x"]
		self.rect.top = self.location["y"]
		# print self.rect
		self.screen.blit(self.image, [self.location["x"], self.location["y"]])
