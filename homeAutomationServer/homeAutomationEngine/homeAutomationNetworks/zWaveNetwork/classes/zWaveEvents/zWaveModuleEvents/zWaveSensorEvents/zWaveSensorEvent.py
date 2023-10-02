from ..zWaveModuleEvent import *

class ZWaveSensorEvent(ZWaveModuleEvent):
    def __init__(self, moduleId, dateTime, location, Type="sensorEvent", id=0):
        ZWaveModuleEvent.__init__(self, moduleId, dateTime, location, Type, id)