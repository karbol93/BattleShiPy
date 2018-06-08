import pygame, sys, os
from Game import Game

WINDOW_NAME = "BattleShiPy game"
SCREEN_SIZE = (550, 500)
FULLSCREEN = False

if __name__ == "__main__":
	os.environ['SDL_VIDEO_CENTERED'] = '1'
	pygame.init()
	pygame.display.set_caption(WINDOW_NAME)
	pygame.display.set_mode(SCREEN_SIZE)

	game = Game()
	game.run()
