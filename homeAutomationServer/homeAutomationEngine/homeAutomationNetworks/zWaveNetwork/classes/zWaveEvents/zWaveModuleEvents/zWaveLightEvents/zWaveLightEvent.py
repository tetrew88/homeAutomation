from ..zWaveModuleEvent import *

class ZWaveLightEvent(ZWaveModuleEvent):
    def __init__(self, moduleId, dateTime, location, Type="light event", id=0):
        ZWaveModuleEvent.__init__(self, moduleId, dateTime, location, Type, id)