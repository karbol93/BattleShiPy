import pygame
from DrawableObject import DrawableObject

class Boat(DrawableObject):
	def __init__(self, imagePath, x, y, rotation):
		self.image = pygame.image.load(imagePath)
		super().__init__(self.image, x, y, rotation)
