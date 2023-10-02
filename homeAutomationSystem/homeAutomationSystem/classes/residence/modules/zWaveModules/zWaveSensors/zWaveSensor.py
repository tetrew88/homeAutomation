from ..zWaveModule import *

class ZWaveSensor(ZWaveModule):
    '''
        
    '''


    def __init__(self, id, name, location, values, parametters, manufacturerName, productName, productType, deviceType, type, canWakeUp, isAwake, isFailed, isReady, isSleeping, batteryLevel, commandClassAsString, sensors, role="sensor"):
        ZWaveModule.__init__(self, id, name, location, role, values, parametters, manufacturerName, productName, productType, deviceType, type, canWakeUp, isAwake, isFailed, isReady, isSleeping, batteryLevel, commandClassAsString)
        self.sensors = sensors

    
    @property
    def strSensorsList(self):
        """
            property representing the str sensor list of the sensor
        
                return:
                    if succes return str sensor list
                    else false
        """
        
        succes = strSensorsList = False

        try:
            strSensorsList = list(self.sensors.keys())
        except:
            strSensorsList = []

        return strSensorsList


    
    def serialize(self):
        data = super().serialize()

        data['sensors'] = []
        for sensor in self.sensors:
            data['sensors'].append(sensor.serialize())

        data['strSensorsList'] = self.strSensorsList
            

        return data