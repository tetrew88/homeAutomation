from .zWaveLightEvent import *

class ZWaveLightSettingOff(ZWaveLightEvent):
    def __init__(self, moduleId, dateTime, location, id=0):
        ZWaveLightEvent.__init__(self, moduleId, dateTime, location, "light setting off", id)    

    def __str__(self):
        return "[{}]: l'éclairage n°{} as été éteint".format(self.dateTime, self.moduleId)