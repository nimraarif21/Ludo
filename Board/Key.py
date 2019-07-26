
class Key:
    def __init__(self, value, color, position, name):
        self.value=value
        self.color=color
        self.position=position
        self.name=name

    def GetName(self):
        return self.name
    
    def GetPosition(self):
        return self.position

    def GetValue(self):
        return self.value

    def SetValue(self, value):
        self.value=value

    def SetPosition(self, position):
        self.position=position