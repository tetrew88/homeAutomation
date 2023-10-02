from .zWaveSensor import *

class ZWaveAccesControlSensor(ZWaveSensor):
    def __init__(self, id, name, location, values, parametters, manufacturerName, productName, productType, deviceType, type, canWakeUp, isAwake, isFailed, isReady, isSleeping, batteryLevel, commandClassAsString, accesState):
        ZWaveSensor.__init__(id, name, location, values, parametters, manufacturerName, productName, productType, deviceType, type, canWakeUp, isAwake, isFailed, isReady, isSleeping, batteryLevel, commandClassAsString, False, "accesControlSensor")
        self.accesState = accesState


    def serialize(self):
        data = super().serialize()

        data['accesState'] = self.accesState

        return data