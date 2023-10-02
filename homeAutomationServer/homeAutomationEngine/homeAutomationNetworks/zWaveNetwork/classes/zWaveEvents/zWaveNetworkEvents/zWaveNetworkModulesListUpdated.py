from .zWaveNetworkEvent import *

class ZWaveNetworkModulesListUpdated(ZWaveNetworkEvent):
    def __init__(self, datetime, id=0):
        ZWaveNetworkEvent.__init__(self, datetime, "network modules list updated", id)



    def __str__(self):
        return "[{}]: la liste de module as été mise a jour".format(self.dateTime)