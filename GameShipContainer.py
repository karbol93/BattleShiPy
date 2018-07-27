from Boat import Boat
from DrawableObject import DrawableObject
import pygame

class GameShipContainer(DrawableObject):

    def __init__(self, x, y):
        self.boat_x = 25
        self.boat_y = 50
        self.selectedShip = None
        self.panel = pygame.Surface((240, 300))
        if pygame.font.match_font('comicsansms'):
            self.font = pygame.font.SysFont("comicsansms", 18)
        else:
            self.font = pygame.font.SysFont(pygame.font.get_default_font(), 18)

        self.ships = [
            [Boat(Boat.FOUR_MASTS, self.boat_x, self.boat_y, 90)         ,4],
            [Boat(Boat.THREE_MASTS, self.boat_x, self.boat_y + 60, 90)   ,3],
            [Boat(Boat.TWO_MASTS, self.boat_x, self.boat_y + 120, 90),2],
            [Boat(Boat.ONE_MAST, self.boat_x, self.boat_y + 180, 90) ,1]
        ]

        super().__init__(self.panel, x, y, rotation=0)


    def shipSelected(self, event):
        mx, my = event.pos
        mx = mx - self.x
        my = my - self.y
        print(mx, '\t', my)

        for i, ship in enumerate(self.ships):
            if(mx > ship[0].x and my > ship[0].y and mx < ship[0].x +((1+i) * 50) and my < ship[0].y + 50 ):
                self.selectedShip = self.ships[i][0]
                return True;


    def getSelectedShip(self):
        return self.selectedShip


    def draw(self, surface):
        self.panel.fill((66, 134, 244))
        text = self.font.render("Ship picker", True, (255, 0, 0))
        self.panel.blit(text, (((self.panel.get_width()/2) - (text.get_width()/2)), 10) )
        for line in self.ships:
            ship, number = line[0], line[1]
            ship.draw(self.panel)
            text = self.font.render("x" + str(number), True, (255, 0, 0))
            self.panel.blit(text, (ship.x-20 , ship.y+9 ))

        super().draw(surface)
