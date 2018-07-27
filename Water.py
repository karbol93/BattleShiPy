import pygame
from DrawableObject import DrawableObject

image_path = './res/img/field_watter.png'

class Water(DrawableObject):
	def __init__(self, x, y, rotation):
		super().__init__(image_path, x, y, rotation)
