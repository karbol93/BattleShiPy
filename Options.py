import pygame
import sys

class Options:
    WINDOW_PROPERTIES = {
        "fullscreen": False,
        "screen_resolution": (550, 500)
    }


    def __init__(self):
        self.done = False
        self.screen= pygame.display.get_surface()


    def key_down_event(self, key):
        if key == pygame.K_ESCAPE:
            self.done = True


    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                self.key_down_event(event.key)


    def draw(self):
        self.screen.fill((62, 86, 183))
        pygame.display.flip()


    def run(self):
        while not self.done:
            self.event_loop()
            self.draw()
