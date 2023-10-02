from .zWaveAccesControlEvent import *

class ZWaveAccesClosed(ZWaveAccesControlEvent):
    def __init__(self, moduleId, dateTime, location, id=0):
        ZWaveAccesControlEvent.__init__(self, moduleId, dateTime, location, "acces closed", id)    

    def __str__(self):
        return "[{}]: l'accès a l' emplacement {} as été fermé".format(self.dateTime, self.location)