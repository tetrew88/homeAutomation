from .zWaveSensor import *

class ZWaveMotionSensor(ZWaveSensor):
    """
        class representing an motion sensor
            Attributes:
            property:
            method:
    """

    def __init__(self, id, name, location, values, parametters, manufacturerName, productName, productType, deviceType, type, canWakeUp, isAwake, isFailed, isReady, isSleeping, batteryLevel, commandClassAsString):
        ZWaveSensor.__init__(id, name, location, values, parametters, manufacturerName, productName, productType, deviceType, type, canWakeUp, isAwake, isFailed, isReady, isSleeping, batteryLevel, commandClassAsString, False, "motionSensor")