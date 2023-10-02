from .zWaveSensor import *

class ZWaveLuminanceSensor(ZWaveSensor):
    """      
    
    """

    def __init__(self, id, name, location, values, parametters, manufacturerName,productName, productType, deviceType, type, canWakeUp, isAwake, isFailed, isReady, isSleeping, batteryLevel, commandClassAsString, luminance):
        ZWaveSensor.__init__(id, name, location, values, parametters, manufacturerName, productName, productType, deviceType, type, canWakeUp, isAwake, isFailed, isReady, isSleeping, batteryLevel, commandClassAsString, False, "luminanceSensor")
        self.luminance = luminance



    def serialize(self):
        data = super().serialize()

        data['luminance'] = self.luminance

        return data