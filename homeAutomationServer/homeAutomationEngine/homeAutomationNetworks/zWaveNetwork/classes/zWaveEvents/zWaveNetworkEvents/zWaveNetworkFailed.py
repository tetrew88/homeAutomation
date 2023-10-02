from .zWaveNetworkEvent import *

class ZWaveNetworkFailed(ZWaveNetworkEvent):
    def __init__(self, datetime, id=0):
        ZWaveNetworkEvent.__init__(self, datetime, "network failed", id)



    def __str__(self):
        return "[{}]: le réseau zwave as faillis".format(self.dateTime)