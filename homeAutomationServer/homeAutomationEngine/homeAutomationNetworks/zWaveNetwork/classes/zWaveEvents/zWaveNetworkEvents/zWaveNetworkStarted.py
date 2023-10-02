from .zWaveNetworkEvent import *

class ZWaveNetworkStarted(ZWaveNetworkEvent):
    def __init__(self, datetime, id=0):
        ZWaveNetworkEvent.__init__(self, datetime, "network started", id)



    def __str__(self):
        return "[{}]: le réseau zwave as été démarer".format(self.dateTime)