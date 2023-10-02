from ..zWaveModule import *

class ZWaveRelay(ZWaveModule):
    '''
        
    '''


    def __init__(self, id, name, location, values, parametters, manufacturerName, productName, productType, deviceType, type, canWakeUp, isAwake, isFailed, isReady, isSleeping, batteryLevel, commandClassAsString, state, role="relay"):
        """constructor"""

        ZWaveModule.__init__(self, id, name, location, role, values, parametters, manufacturerName, productName, productType, deviceType, type, canWakeUp, isAwake, isFailed, isReady, isSleeping, batteryLevel, commandClassAsString)
        self.state = state

    

    def serialize(self):
        data = super().serialize()

        #state
        data['state'] = self.state