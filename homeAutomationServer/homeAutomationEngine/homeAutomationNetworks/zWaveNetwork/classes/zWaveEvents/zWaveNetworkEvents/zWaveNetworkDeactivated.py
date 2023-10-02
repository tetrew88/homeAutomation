from .zWaveNetworkEvent import *

class ZWaveNetworkDeactivated(ZWaveNetworkEvent):
    def __init__(self, datetime, id=0):
        ZWaveNetworkEvent.__init__(self, datetime, "network deactivated", id)

    
    def __str__(self):
        return "[{}]: le réseau zwave as été desactivé".format(self.dateTime)