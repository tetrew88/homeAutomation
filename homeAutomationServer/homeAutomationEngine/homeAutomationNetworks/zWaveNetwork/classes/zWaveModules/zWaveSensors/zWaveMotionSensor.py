from .zWaveSensor import *

class ZWaveMotionSensor(ZWaveSensor):
    """
        class representing an motion sensor
            Attributes:
            property:
            method:
    """

    def __init__(self, node, role="motion sensor"):
        ZWaveSensor.__init__(self, node, False, role)



    def serialize(self):
        data = {}
        data['role'] = self.role

        return data