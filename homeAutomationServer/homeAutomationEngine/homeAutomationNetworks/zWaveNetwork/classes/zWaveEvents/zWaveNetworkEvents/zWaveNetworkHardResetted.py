from .zWaveNetworkEvent import *

class ZWaveNetworkHardResetted(ZWaveNetworkEvent):
    def __init__(self, datetime, id=0):
        ZWaveNetworkEvent.__init__(self, datetime, "network hard resetted", id)

    
    def __str__(self):
        return "[{}]: le réseau zwave as été durement réinitialisé".format(self.dateTime)