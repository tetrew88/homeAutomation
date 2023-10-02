from .zWaveSensorEvent import *

class ZWaveMotionDetection(ZWaveSensorEvent):
    def __init__(self, moduleId, dateTime, location, id=0):
        ZWaveSensorEvent.__init__(self, moduleId, dateTime, location, "motion detected", id)


    def __str__(self):
        return "[{}]: un mouvement as été detecter".format(self.dateTime, self.location)