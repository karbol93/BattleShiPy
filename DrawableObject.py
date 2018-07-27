import pygame

class DrawableObject:
	def __init__(self, image, x, y, rotation):
		if type(image) is str:
			self.image =  pygame.image.load(image)
		else:
			self.image = image
		self.x = x
		self.y = y
		self.rotation = rotation

	def draw(self, surface):
		self.image = pygame.transform.rotate(self.image, self.rotation)
		surface.blit(self.image, (self.x, self.y))
