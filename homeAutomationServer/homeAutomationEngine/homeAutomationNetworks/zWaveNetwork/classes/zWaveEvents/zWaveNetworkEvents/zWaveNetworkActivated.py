from .zWaveNetworkEvent import *

class ZWaveNetworkActivated(ZWaveNetworkEvent):
    def __init__(self, datetime, id=0):
        ZWaveNetworkEvent.__init__(self, datetime, "network activated", id)

    
    def __str__(self):
        return "[{}]: le réseau zwave as été activé".format(self.dateTime)