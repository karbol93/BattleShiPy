import pygame
from DrawableObject import DrawableObject

class Boat(DrawableObject):
	def __init__(self, x, y, rotation):
		image = pygame.image.load('./boat.png')
		super().__init__(image, x, y, rotation)