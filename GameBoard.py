from DrawableObject import DrawableObject
from Water import Water

class GameBoard:

    def __init__(self):
        self.w = 50
        self.h = 50
        self.pading_left = 40
        self.pading_top = 40

        self.fields = [[Water( self.pading_left+(j*self.w), self.pading_top+(i*self.h),0) for j in range(0,9)] for i in range(0,9)]

    def getFields(self):
        return self.fields
