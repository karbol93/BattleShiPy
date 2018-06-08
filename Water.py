import pygame
from DrawableObject import DrawableObject

class Water(DrawableObject):
	def __init__(self, x, y, rotation):
		image = pygame.image.load('./res/img/field_watter.png')
		super().__init__(image, x, y, rotation)
