from .zWaveSensor import *

class ZWaveTemperatureSensor(ZWaveSensor):
    """      
    
    """

    def __init__(self, id, name, location, values, parametters, manufacturerName, productName, productType, deviceType, type, canWakeUp, isAwake, isFailed, isReady, isSleeping, batteryLevel, commandClassAsString, temperature):
        ZWaveSensor.__init__(id, name, location, values, parametters, manufacturerName, productName, productType, deviceType, type, canWakeUp, isAwake, isFailed, isReady, isSleeping, batteryLevel, commandClassAsString, False, "temperatureSensor")
        self.temperature = temperature



    def serialize(self):
        data = super().serialize()

        data['temperature'] = self.temperature

        return data