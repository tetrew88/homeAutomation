from .zWaveSensor import *

class ZWaveAccesControlSensor(ZWaveSensor):
    '''
        class bringing all the information and functionality of an acces control sensor
            
            attributes:
                moduleNode: network node of the module
                role: role of the module
                sensors: list of sensor contained in the main sensor
            
            property:
                id: id of the module(str)
                name: name of the module(str)
                location: location(room id (int))

                manufacturerName: manufacturer name of the module(str)
                productName: product name of the module(str)

                productType: product type of the module(str)
                deviceType: device tye of the module(str)
                type: type of the node(str)

                values: list of node values(list of value class)
                parammetters: list of node parametters(list of parametters class)

                canWakeUp: property allow to know if the module can be wake up(True/False)

                isAwake: property allow to know if the module is awake(True/False)
                isFailed: property allow to know if the module is failed(True/False)
                isReady: property allow to know if the module is ready(True/False)
                isSleeping: property allow to know if the module is sleeping(True/False)

                batteryLevel: property allow to know the battery level of the module(int/false)

                commandClassAsString: list of command class(list (str))

                role: role of the module (str)

                #sensor property
                    strSensorsList: str sensor list of the sensor

                #acces control sensor property
                    acces_state: allow to kwnow the state of an acces


            methods:
                get methods:
                    get_value: method allow to get an value of the module

                set methods:
                    set_name: method allow to set the name of the module
                    set_location: method allow to set the location of the module
                    set_value_data: method allow to set an value data of the module

                update methods:
                    update_return_route: method used for update the return route
                    neighbor_update: method used for updated the neigbor list of the module
                    network_update: method used for update the network of the module

                refresh method:
                    refresh_info: method used for update the info of the module
                    refresh_value: method used for refresh an value of the module
                    refresh_values: method used fot refresh all values of the module

                heal methods:
                    heal: method used for heal the module

                serialize method:
                    serialize: method used for serialize the class
    '''

    def __init__(self, node, role="acces control sensor"):
        ZWaveSensor.__init__(self, node, False, role)


    
    @property
    def acces_state(self):
        """
            property allow to kwnow the state of an acces

                return
                    str(open/closed/unknow)
        """

        accesValue = False
        accesState = 'unknow'

        for value in self.values:
            if value.label == "access control":
                accesValue = value
                break
            else:
                accesValue = False

        if accesValue != False:
            if accesValue.data == 23:
                accesState = 'closed'
            elif accesValue.data == 22:
                accesState = 'open'
            else:
                accesState = 'unknow'
        else:
            accesState = 'unknow'

        return accesState



    def serialize(self):
        data = {}
        
        #acces state
        data['role'] = self.role
        data['accesState'] = self.acces_state

        return data