from .engineEvent import *

class EngineStopped(EngineEvent):
    def __init__(self, datetime, id=0):
        EngineEvent.__init__(self, datetime, "engine stopped", id)



    def __str__(self):
        return "[{}]: le moteur domotique as été éteint".format(self.dateTime)