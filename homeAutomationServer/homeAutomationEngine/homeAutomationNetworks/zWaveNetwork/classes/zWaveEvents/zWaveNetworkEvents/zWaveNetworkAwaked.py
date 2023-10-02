from .zWaveNetworkEvent import *

class ZWaveNetworkAwaked(ZWaveNetworkEvent):
    def __init__(self, datetime, id=0):
        ZWaveNetworkEvent.__init__(self, datetime, "network awaked", id)

    
    def __str__(self):
        return "[{}]: le réseau zwave as été réveiller".format(self.dateTime)