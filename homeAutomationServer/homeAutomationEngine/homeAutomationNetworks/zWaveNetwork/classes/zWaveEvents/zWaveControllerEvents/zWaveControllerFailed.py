from .zWaveControllerEvent import *

class ZWaveControllerFailed(ZWaveControllerEvent):
    def __init__(self, datetime, id=0):
        ZWaveControllerEvent.__init__(self, datetime, "controller failed", id)



    def __str__(self):
        return "[{}]: le controller as faillis".format(self.dateTime)