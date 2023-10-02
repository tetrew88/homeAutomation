from .zWaveNetworkEvent import *

class ZWaveNetworkReady(ZWaveNetworkEvent):
    def __init__(self, datetime, id=0):
        ZWaveNetworkEvent.__init__(self, datetime, "network ready", id)



    def __str__(self):
        return "[{}]: le réseau zwave est pret".format(self.dateTime)