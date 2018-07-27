from Boat import Boat
import pygame

class GameShipContainer:

    def __init__(self):
        self.x = 500
        self.y = 40
        self.selectedShip = None

        self.ships = [
            [Boat("./res/img/boat_one_mast.png", self.x, self.y, 90)         ,4],
            [Boat("./res/img/boat_two_masts.png", self.x, self.y + 60, 90)   ,3],
            [Boat("./res/img/boat_three_masts.png", self.x, self.y + 120, 90),2],
            [Boat("./res/img/boat_four_masts.png", self.x, self.y + 180, 90) ,1]
            [Boat(Boat.ONE_MAST, self.x, self.y, 90)         ,4],
            [Boat(Boat.TWO_MASTS, self.x, self.y + 60, 90)   ,3],
            [Boat(Boat.THREE_MASTS, self.x, self.y + 120, 90),2],
            [Boat(Boat.FOUR_MASTS, self.x, self.y + 180, 90) ,1]
        ]

    def shipSelect(self,event):
        mx, my = event.pos

        for i, ship in enumerate(self.ships):
            if(mx > ship[0].x and my > ship[0].y and mx < ship[0].x +((1+i) * 50) and my < ship[0].y + 50 ):
                self.selectedShip = self.ships[i][0]
                return True

    def getSelectedShip(self):
        return self.selectedShip
