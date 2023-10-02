from .zWaveControllerEvent import *

class ZWaveControllerResetted(ZWaveControllerEvent):
    def __init__(self, datetime, id=0):
        ZWaveControllerEvent.__init__(self, datetime, "controller resetted", id)


    
    def __str__(self):
        return "[{}]: le controller as été réinitialiser".format(self.dateTime)