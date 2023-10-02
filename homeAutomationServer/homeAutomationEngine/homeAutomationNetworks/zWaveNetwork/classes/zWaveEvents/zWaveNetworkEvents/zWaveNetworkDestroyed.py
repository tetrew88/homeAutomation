from .zWaveNetworkEvent import *

class ZWaveNetworkDestroyed(ZWaveNetworkEvent):
    def __init__(self, datetime, id=0):
        ZWaveNetworkEvent.__init__(self, datetime, "network destroyed", id)

    
    def __str__(self):
        return "[{}]: le réseau zwave as été détruit".format(self.dateTime)