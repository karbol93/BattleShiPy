import pygame

class Options:
    WINDOW_PROPERTIES = {
        "fullscreen": False,
        "screen_resolution": (550, 500)
    }


    def __init__(self):
        self.done = False

    def event_loop(self):
        pass

    def draw(self):
        pass

    def run(self):
        while not self.done:
            self.event_loop()
            self.draw()
