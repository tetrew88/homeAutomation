from .zWaveNetworkEvent import *

class ZWaveNetworkSoftResetted(ZWaveNetworkEvent):
    def __init__(self, datetime, id=0):
        ZWaveNetworkEvent.__init__(self, datetime, "network soft resetted", id)

    
    def __str__(self):
        return "[{}]: le réseau zwave as été légèrement reinitialisé".format(self.dateTime)