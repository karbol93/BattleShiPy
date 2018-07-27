import pygame
from DrawableObject import DrawableObject

class Water(DrawableObject):
	def __init__(self, x, y, rotation):
		image_path = './res/img/field_watter.png'
		super().__init__(image_path, x, y, rotation)
