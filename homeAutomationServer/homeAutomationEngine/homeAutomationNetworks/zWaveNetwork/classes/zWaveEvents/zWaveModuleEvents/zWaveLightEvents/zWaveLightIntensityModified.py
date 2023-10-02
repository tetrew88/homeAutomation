from .zWaveLightEvent import *

class ZWaveLightIntensityModified(ZWaveLightEvent):
    def __init__(self, moduleId, dateTime, location, id=0):
        ZWaveLightEvent.__init__(self, moduleId, dateTime, location, "light intensity modified", id)    

    def __str__(self):
        return "[{}]: l'intensité de l'éclairage n°{} as été modifier".format(self.dateTime, self.moduleId)