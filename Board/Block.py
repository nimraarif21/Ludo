
class Block:
    def __init__(self, color, value):
        self.color = color
        self.value = value

    def GetValue(self):
        return self.value

    def SetValue(self, value):
        self.value = value