import pygame
from Game       import Game
from Options    import Options
from About      import About

class Menu:

    menu_options_text = [
        "Single player",
        "Multi player",
        "Options",
        "About",
        "Exit",
    ]


    SINGLE_PLAYER = 0
    MULTI_PLAYER = 1
    OPTIONS = 2
    ABOUT = 3
    EXIT = 4


    def __init__(self):
        self.cursor_position = self.SINGLE_PLAYER
        self.font = None
        self.done = False
        self.screen= pygame.display.get_surface()

        if pygame.font.match_font('comicsansms'):
            self.font = pygame.font.SysFont("comicsansms", 18)


    def cursor_move_up(self):
        if self.cursor_position > 0:
            self.cursor_position -= 1


    def cursor_move_down(self):
        if self.cursor_position < len(self.menu_options_text) - 1:
            self.cursor_position += 1


    def enter_key_event(self):
        if self.cursor_position == self.SINGLE_PLAYER:
            game = Game(self.SINGLE_PLAYER)
            game.run()
        elif self.cursor_position == self.MULTI_PLAYER:
            game = Game(self.MULTI_PLAYER)
            game.run()
        elif self.cursor_position == self.OPTIONS:
            options = Options()
            options.run()
        elif self.cursor_position == self.ABOUT:
            about = About()
            about.run()
        elif self.cursor_position == self.EXIT:
            self.done = True


    def key_down_event(self, key):
        if key == pygame.K_UP:
            self.cursor_move_up()
        elif key == pygame.K_DOWN:
            self.cursor_move_down()
        elif key == pygame.K_RETURN:
            self.enter_key_event()


    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == pygame.KEYDOWN:
                self.key_down_event(event.key)


    def draw_options(self):
        for i in range(0, len(self.menu_options_text)):
            text = self.font.render(self.menu_options_text[i], True, (15, 96, 226))
            self.screen.blit(text, ((self.screen.get_width() // 2) - (text.get_width() // 2), 20 * i))



    def draw_cursor(self):
        text = self.font.render(self.menu_options_text[self.cursor_position], True, (15, 96, 226))
        pygame.draw.circle(self.screen, (15, 96, 226), ( (self.screen.get_width() // 2) - (text.get_width() // 2) - 10, self.cursor_position * 20 + 13), 5)


    def draw(self):
        self.screen.fill((175, 196, 15))
        self.draw_options()
        self.draw_cursor()
        pygame.display.flip()


    def run(self):
        while not self.done:
            self.event_loop()
            self.draw()
