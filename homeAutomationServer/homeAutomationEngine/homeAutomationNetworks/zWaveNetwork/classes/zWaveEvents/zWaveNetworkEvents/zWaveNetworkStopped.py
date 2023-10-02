from .zWaveNetworkEvent import *

class ZWaveNetworkStopped(ZWaveNetworkEvent):
    def __init__(self, datetime, id=0):
        ZWaveNetworkEvent.__init__(self, datetime, "network stopped", id)



    def __str__(self):
        return "[{}]: le réseau zwave as été arreté".format(self.dateTime)