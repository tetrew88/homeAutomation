from .zWaveLightEvent import *

class ZWaveLightColorModified(ZWaveLightEvent):
    def __init__(self, moduleId, dateTime, location, id=0):
        ZWaveLightEvent.__init__(self, moduleId, dateTime, location, "light color modified", id)    

    def __str__(self):
        return "[{}]: la couleur de l'éclairage n°{} as été modifier".format(self.dateTime, self.moduleId)