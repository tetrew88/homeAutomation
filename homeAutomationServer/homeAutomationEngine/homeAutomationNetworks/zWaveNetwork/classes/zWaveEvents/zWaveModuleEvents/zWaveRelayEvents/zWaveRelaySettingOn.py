from .zWaveRelayEvent import *

class ZWaveRelaySettingOn(ZWaveRelayEvent):
    def __init__(self, moduleId, dateTime, location, id=0):
        ZWaveRelayEvent.__init__(self, moduleId,dateTime, location, "relay setting on", id)    

    def __str__(self):
        return "[{}]: le relay {} as été allumé".format(self.dateTime, self.moduleId)