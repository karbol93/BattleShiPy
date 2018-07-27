import pygame
from DrawableObject import DrawableObject

oneMastPath = './res/img/boat_one_mast.png'
twoMastsPath = './res/img/boat_two_masts.png'
threeMastsPath = './res/img/boat_three_masts.png'
fourMastsPath = './res/img/boat_four_masts.png'

class Boat(DrawableObject):
	ONE_MAST = 1
	TWO_MASTS = 2
	THREE_MASTS = 3
	FOUR_MASTS = 4

	def __init__(self, boatSize, x, y, rotation):
		self.boatSize = boatSize
		imagePath = self.getImagePath()
		super().__init__(imagePath, x, y, rotation)


	def getImagePath(self):
		if self.boatSize == self.ONE_MAST:
			imagePath = oneMastPath
		elif self.boatSize == self.TWO_MASTS:
			imagePath = twoMastsPath
		elif self.boatSize == self.THREE_MASTS:
			imagePath = threeMastsPath
		elif self.boatSize == self.FOUR_MASTS:
			imagePath = fourMastsPath
		else:
			imagePath = oneMastPath
		return imagePath
