import pygame

class DrawableObject:
	def __init__(self, imagePath, x, y, rotation):
		self.image =  pygame.image.load(imagePath)
		self.x = x
		self.y = y
		self.rotation = rotation
