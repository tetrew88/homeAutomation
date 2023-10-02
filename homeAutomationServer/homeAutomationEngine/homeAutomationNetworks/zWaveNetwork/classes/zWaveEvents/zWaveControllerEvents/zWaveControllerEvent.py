from ..zWaveEvent import *

class ZWaveControllerEvent(ZWaveEvent):
    def __init__(self, datetime, Type="controller event", id=0):
        ZWaveEvent.__init__(self, datetime, Type, id)