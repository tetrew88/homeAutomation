from .zWaveNetworkEvent import *

class ZWaveNetworkHealed(ZWaveNetworkEvent):
    def __init__(self, datetime, id=0):
        ZWaveNetworkEvent.__init__(self, datetime, "network healed", id)

    
    def __str__(self):
        return "[{}]: le réseau zwave as été soigné".format(self.dateTime)