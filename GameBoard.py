from DrawableObject import DrawableObject
from Water import Water
import pygame

class GameBoard(DrawableObject):

    def __init__(self,x,y):
        self.w = 50
        self.h = 50
        self.top_x = 30
        self.top_y = 30
        self.panel = pygame.Surface((500,500))

        self.fields = [[Water( self.top_x+(j*self.w), self.top_y+(i*self.h),0) for j in range(0,9)] for i in range(0,9)]

        super().__init__(self.panel, x, y, rotation=0)

    def getFields(self):
        return self.fields

    def draw(self, surface):
        for fields in self.fields:
            for field in fields:
                field.draw(self.panel)
        super().draw(surface)
