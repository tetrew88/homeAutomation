from .engineEvent import *

class EngineStarted(EngineEvent):
    def __init__(self, datetime, id=0):
        EngineEvent.__init__(self, datetime, "engine started", id)



    def __str__(self):
        return "[{}]: le moteur domotique as été démarer".format(self.dateTime)