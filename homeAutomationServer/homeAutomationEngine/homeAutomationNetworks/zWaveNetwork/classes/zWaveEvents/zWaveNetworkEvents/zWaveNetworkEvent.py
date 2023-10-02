from ..zWaveEvent import *

class ZWaveNetworkEvent(ZWaveEvent):
    def __init__(self, datetime, Type="zwave network event", id=0):
        ZWaveEvent.__init__(self, datetime, Type, id)


    def __str__(self):
        return super().__str__()