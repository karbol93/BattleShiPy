import pygame, sys, os
from Menu import Menu

WINDOW_NAME = "BattleShiPy game"
SCREEN_SIZE = (750, 500)
FULLSCREEN = False

if __name__ == "__main__":
	os.environ['SDL_VIDEO_CENTERED'] = '1'
	pygame.init()
	pygame.display.set_caption(WINDOW_NAME)
	pygame.display.set_mode(SCREEN_SIZE)

	menu = Menu()
	menu.run()
