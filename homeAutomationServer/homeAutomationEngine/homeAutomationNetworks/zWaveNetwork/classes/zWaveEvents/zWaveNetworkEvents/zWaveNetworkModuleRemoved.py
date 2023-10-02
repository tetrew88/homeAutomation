from .zWaveNetworkEvent import *

class ZWaveNetworkModuleRemoved(ZWaveNetworkEvent):
    def __init__(self, datetime, moduleId, id=0):
        ZWaveNetworkEvent.__init__(self, datetime, "module removed", id)
        self.moduleId = moduleId



    def __str__(self):
        return "[{}]: un module as été retiré du réseau zwave".format(self.dateTime)