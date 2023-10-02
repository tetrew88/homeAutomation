from .zWaveRelayEvent import *

class ZWaveRelaySettingOff(ZWaveRelayEvent):
    def __init__(self, moduleId, dateTime, location, id=0):
        ZWaveRelayEvent.__init__(self, moduleId, dateTime, location, "relay setting off", id)    

    def __str__(self):
        return "[{}]: le relay {} as été éteint".format(self.dateTime, self.moduleId)