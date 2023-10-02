from .zWaveLightController import *


class ZWaveColorLightController(ZWaveLightController):
    def __init__(self, id, name, location, values, parametters, manufacturerName, productName, productType, deviceType, type, canWakeUp, isAwake, isFailed, isReady, isSleeping, batteryLevel, commandClassAsString, level, lightUp, maxLevel, minLevel, startLevel, colorLabel, colorValue, colorPalette, role="color light controller"):
        """constructor"""
        ZWaveLightController.__init__(self, id, name, location, values, parametters, manufacturerName, productName, productType, deviceType, type, canWakeUp, isAwake, isFailed, isReady, isSleeping, batteryLevel, commandClassAsString, level, lightUp, maxLevel, minLevel, startLevel)
        self.colorLabel = colorLabel
        self.colorValue = colorValue
        self.colorPalette = colorPalette


    def serialize(self):
        data = super().serialize()

        #color label
        data["colorLabel"] = self.colorLabel

        #color value
        data["colorValue"] = self.colorValue

        #color palette
        data["colorPalette"] = self.colorPalette

        return data