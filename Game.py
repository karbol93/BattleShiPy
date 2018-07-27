import pygame, sys
from DrawableObject import DrawableObject
from GameBoard import GameBoard
from GameShipContainer import GameShipContainer
from Boat import Boat

class Game:

	SINGLE_PLAYER	= 0
	MULTI_PLAYER 	= 1


	def __init__(self, game_mode):
		self.exit = False
		self.screen = pygame.display.get_surface()
		self.screen.fill((0, 0, 0))
		self.userBoard = GameBoard(0, 0)
		self.shipBox = GameShipContainer(500, 40)
		self.drawableObjects = [self.userBoard, self.shipBox]


	def event_loop(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(0)
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				self.exit = True
			elif event.type == pygame.MOUSEBUTTONDOWN:
				#for drawableOject in drawableOject:
					#if drawableOject.clicked():
						#clickedObject = drawableOject.getClicked()
				self.drawSelectedShip = self.shipBox.shipSelected(event)
				self.flyingDutch = self.shipBox.getSelectedShip()
			elif event.type == pygame.MOUSEBUTTONUP:
				pass
				self.drawSelectedShip = False
			elif event.type == pygame.MOUSEMOTION:
				pass


	def update(self):
		pass


	def draw_background(self):
		self.screen.fill((0, 0, 0))


	def draw_objects(self):
		pass
		'''
		for object in self.drawableObjects:
			image = pygame.transform.rotate(object.image, object.rotation)
			imageRectangle = image.get_rect()
			imageRectangle.center = object.image.get_rect().center
			imageRectangle = imageRectangle.move(object.x, object.y)
			self.screen.blit(image, imageRectangle)
		'''

	def draw_userBoard(self):
		self.userBoard.draw(self.screen)



	def draw_shipBox(self):
		self.shipBox.draw(self.screen)


	def draw_gui(self):
		self.draw_userBoard()
		self.draw_shipBox()


	def draw(self):
		self.draw_background()
		self.draw_gui()
		self.draw_objects()
		pygame.display.flip()


	def run(self):
		while not self.exit:
			self.event_loop()
			self.update()
			self.draw()
