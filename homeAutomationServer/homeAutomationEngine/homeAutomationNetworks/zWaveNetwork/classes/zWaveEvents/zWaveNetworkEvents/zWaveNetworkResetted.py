from .zWaveNetworkEvent import *

class ZWaveNetworkResetted(ZWaveNetworkEvent):
    def __init__(self, datetime, id=0):
        ZWaveNetworkEvent.__init__(self, datetime, "network resetted", id)

    def __str__(self):
        return "[{}]: le réseau zwave as été redémarer".format(self.dateTime)