from ..zWaveSensorEvent import *

class ZWaveAccesControlEvent(ZWaveSensorEvent):
    def __init__(self, moduleId, dateTime, location, Type="acces control event", id=0):
        ZWaveSensorEvent.__init__(self, moduleId, dateTime, location, Type, id)