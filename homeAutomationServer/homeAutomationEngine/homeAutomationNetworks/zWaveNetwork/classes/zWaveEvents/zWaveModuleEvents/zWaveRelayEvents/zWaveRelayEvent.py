from ..zWaveModuleEvent import *

class ZWaveRelayEvent(ZWaveModuleEvent):
    def __init__(self, moduleId, dateTime, location, type='relay event', id=0):
        ZWaveModuleEvent.__init__(self, moduleId, type, dateTime, location, id)

    

    def __str__(self):
        return "[{}]: {}".format(self.dateTime, self.type)