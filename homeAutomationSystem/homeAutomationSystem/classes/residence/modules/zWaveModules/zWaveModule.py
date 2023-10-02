from ..module import *


class ZWaveModule(Module):
    '''
        
    '''


    def __init__(self, id, name, location, role, values, parametters, manufacturerName, productName, productType, deviceType, type, canWakeUp, isAwake, isFailed, isReady, isSleeping, batteryLevel, commandClassAsString):
        """constructor"""

        Module.__init__(self, id, name, location, role, 'zWave')

        self.values = values
        self.parametters = parametters
        self.manufacturerName = manufacturerName
        self.productName = productType
        self.profuctType = productType
        self.deviceType = deviceType
        self.type = type
        self.canWakeUp = canWakeUp
        self.isAwake = isAwake
        self.isFailed = isFailed
        self.isReady = isReady
        self.isSleeping = isSleeping
        self.batteryLevel = batteryLevel
        self.commandClassAsString = commandClassAsString

    
    def serialize(self):
        data = super().serialize()
        valuesList = []
        paramettersList = []

        for value in self.values:
            valuesList.append(value.serialize())
        data['values'] = valuesList

        for parametter in self.parametters:
            paramettersList.append(parametter.serialize())
        data['parametters'] = paramettersList

        data['manufacturerName'] = self.manufacturerName
        data['productName'] = self.productName
        data['productType'] = self.profuctType
        data["deviceType"] = self.deviceType
        data['type'] = self.type
        data['canWakeUp'] = self.canWakeUp
        data['isAwake'] = self.isAwake
        data['isFailed'] = self.isFailed
        data['isReady'] = self.isReady
        data['isSleeping'] = self.isSleeping
        data['batteryLevel'] = self.batteryLevel
        data['commandClassAsString'] = self.commandClassAsString

        return data