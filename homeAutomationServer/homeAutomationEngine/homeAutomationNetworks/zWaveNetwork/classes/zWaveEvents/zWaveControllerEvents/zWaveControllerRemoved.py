from .zWaveControllerEvent import *

class ZWaveControllerRemoved(ZWaveControllerEvent):
    def __init__(self, datetime, id=0):
        ZWaveControllerEvent.__init__(self, datetime, "controller removed", id)



    def __str__(self):
        return "[{}]: le controller as été retirer".format(self.dateTime)