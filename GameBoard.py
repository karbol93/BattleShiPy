from DrawableObject import DrawableObject
from Water import Water

class GameBoard:

    def __init__(self):
        self.w = 50
        self.h = 50
        self.top_x = 40
        self.top_y = 40

        self.fields = [[Water( self.top_x+(j*self.w), self.top_y+(i*self.h),0) for j in range(0,9)] for i in range(0,9)]

    def getFields(self):
        return self.fields
