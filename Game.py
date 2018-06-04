import pygame

class Game:
	
	def __init__(self):
		self.exit = False
		

	def event_loop(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.exit = True
		
		
	def update(self):
		pass
		
		
	def draw(self):
		pygame.display.flip()
		
		
	def run(self):
		while not self.exit:
			self.event_loop()
			self.update()
			self.draw()
			