from .zWaveControllerEvent import *

class ZWaveControllerReady(ZWaveControllerEvent):
    def __init__(self, datetime, id=0):
        ZWaveControllerEvent.__init__(self, datetime, "controller ready", id)



    def __str__(self):
        return "[{}]: le controller est pret".format(self.dateTime)