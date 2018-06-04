import pygame
from DrawableObject import DrawableObject

class Game:
	
	def __init__(self):
		self.exit = False
		self.screen = pygame.display.get_surface()
		self.drawableObjects = [ ]
		

	def event_loop(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.exit = True
		
		
	def update(self):
		pass
		
	
	def draw_gui(self):
		pass
		
		
	def draw_background(self):
		pass
		
	
	def draw_objects(self):
		for object in self.drawableObjects:
			image = pygame.transform.rotate(object.image, object.rotation)
			imageRectangle = image.get_rect()
			imageRectangle.center = object.image.get_rect().center
			imageRectangle = imageRectangle.move(object.x, object.y)
			self.screen.blit(image, imageRectangle)
		
		
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
			