import pygame
from DrawableObject import DrawableObject

class Boat(DrawableObject):
	def __init__(self, imagePath, x, y, rotation):
		super().__init__(imagePath, x, y, rotation)
