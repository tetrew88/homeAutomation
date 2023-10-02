from .zWaveModule import *

class ZWaveNetworkController(ZWaveModule):

    def __init__(self, id, name, location, values, parametters, manufacturerName, productName, productType, deviceType, type, canWakeUp, isAwake, isFailed, isReady, isSleeping, batteryLevel, commandClassAsString):
        ZWaveModule.__init__(self, id, name, location, "network conroller", values, parametters, manufacturerName, productName, productType, deviceType, type, canWakeUp, isAwake, isFailed, isReady, isSleeping, batteryLevel, commandClassAsString)

    