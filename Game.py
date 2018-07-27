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
		self.drawableObjects = [ ]
		self.userBoard = GameBoard()
		self.shipBox = GameShipContainer()
		self.drawSelectedShip = False
		self.flyingDutch = Boat("./res/img/boat_one_mast.png",0,0,0)


	def event_loop(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(0)
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				self.exit = True
			elif event.type == pygame.MOUSEBUTTONDOWN:
				self.drawSelectedShip = self.shipBox.shipSelect(event)
				self.flyingDutch = self.shipBox.getSelectedShip()
			elif event.type == pygame.MOUSEBUTTONUP:
				self.drawSelectedShip = False
			elif event.type == pygame.MOUSEMOTION:
				if (self.drawSelectedShip):
					self.flyingDutch.x, self.flyingDutch.y = event.pos


	def update(self):
		pass


	def draw_background(self):
		self.screen.fill((0, 0, 0))


	def draw_objects(self):
		for object in self.drawableObjects:
			image = pygame.transform.rotate(object.image, object.rotation)
			imageRectangle = image.get_rect()
			imageRectangle.center = object.image.get_rect().center
			imageRectangle = imageRectangle.move(object.x, object.y)
			self.screen.blit(image, imageRectangle)


	def draw_userBoard(self):
		for fields in self.userBoard.getFields():
			for field in fields:
				img = field.image
				x,y = field.x,field.y
				self.screen.blit(img,(x,y))


	def draw_shipBox(self):
		for line in self.shipBox.ships:
			ship, number = line[0], line[1]
			image = pygame.transform.rotate(ship.image, ship.rotation)
			self.screen.blit(image, (ship.x, ship.y))
			font = pygame.font.SysFont("comicsansms", 10)
			text = font.render("x" + str(number), True, (255, 0, 0))
			self.screen.blit(text, (ship.x , ship.y))


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
