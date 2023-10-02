from .zWaveAccesControlEvent import *

class ZWaveAccesOpened(ZWaveAccesControlEvent):
    def __init__(self, moduleId, dateTime, location, id=0):
        ZWaveAccesControlEvent.__init__(self, moduleId, dateTime, location, "acces opened", id)    

    def __str__(self):
        return "[{}]: l'accès a l' emplacement {} as été ouvert".format(self.dateTime, self.location)