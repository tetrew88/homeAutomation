from .zWaveNetworkEvent import *

class ZWaveNetworkModuleAdded(ZWaveNetworkEvent):
    def __init__(self, datetime, moduleId, id=0):
        ZWaveNetworkEvent.__init__(self, datetime, "module added", id)
        self.moduleId = moduleId



    def __str__(self):
        return "[{}]: un module as été ajouter au réseau zwave".format(self.dateTime)