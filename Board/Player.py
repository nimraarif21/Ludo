from .Key import Key
import numpy as np

class Player:
    
    def __init__(self, color, startPoint):
        self.keys=np.empty(4,dtype=Key)
        self.keys[0]=Key(0, color, '-1,-1', color[0]+'1')
        self.keys[1]=Key(0, color, '-1,-1', color[0]+'2')
        self.keys[2]=Key(0, color, '-1,-1', color[0]+'3')
        self.keys[3]=Key(0, color, '-1,-1', color[0]+'4')
        self.color=color
        self.start_point=startPoint
    
    def GetKeys(self):
        return self.keys

    def GetStartPoint(self):
        return self.start_point