from .zWaveLightEvent import *

class ZWaveLightSettingOn(ZWaveLightEvent):
    def __init__(self, moduleId, dateTime, location, id=0):
        ZWaveLightEvent.__init__(self, moduleId, dateTime, location, "light setting on", id)    

    def __str__(self):
        return "[{}]: l'éclairage n°{} as été allumé".format(self.dateTime, self.moduleId)