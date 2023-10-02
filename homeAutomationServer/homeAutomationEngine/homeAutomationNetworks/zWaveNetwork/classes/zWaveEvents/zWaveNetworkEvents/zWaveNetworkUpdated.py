from .zWaveNetworkEvent import *

class ZWaveNetworkUpdated(ZWaveNetworkEvent):
    def __init__(self, datetime, id=0):
        ZWaveNetworkEvent.__init__(self, datetime, "network updated", id)

    
    def __str__(self):
        return "[{}]: le réseau zwave as été modifier".format(self.dateTime)