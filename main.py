import pygame, sys, os

WINDOW_NAME = "BattleShiPy game"
SCREEN_SIZE = (500, 500)
FULLSCREEN = False

if __name__ == "__main__":
	os.environ['SDL_VIDEO_CENTERED'] = '1'
	pygame.init()
	pygame.display.set_caption(WINDOW_NAME)
	pygame.display.set_mode(SCREEN_SIZE)
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(0)
		pygame.display.flip()