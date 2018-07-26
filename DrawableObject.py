import pygame

class DrawableObject:
	def __init__(self, image, x, y, rotation):
		self.image =  image
		self.x = x
		self.y = y
		self.rotation = rotation
