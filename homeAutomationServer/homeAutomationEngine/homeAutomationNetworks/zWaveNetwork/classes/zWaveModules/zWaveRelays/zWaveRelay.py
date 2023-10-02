from ..zWaveModule import *

class ZWaveRelay(ZWaveModule):
    """
        class bringing all the information and functionality of an relay
    
            attributes:
                moduleNode: network node of the module
                role: role of the module
            
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

                #relay property
                    state: allow to know the state of the relay

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
    
                #relay methods
                    switch_on: method used for switch the relay on
                    switch_off: method used for switch the relay off
    """
    
    def __init__(self, moduleNode, role ='relay'):
        ZWaveModule.__init__(self, moduleNode, role)

    
    @property
    def state(self):
        """
            property allow to know the state of the relay

                return:
                    if succes true/false
                    else false
        """
        
        state = False

        for value in self.values:
            if value.label == "switch":
                state = value.data
                break
            else:
                state = False

        return state



    """SWITCH METHOD"""
    def switch_on(self):
        """
            method used for switch the relay on

                return:
                    if succes return true
                    else False
        """

        succes = False
        
        for value in self.values:
            if value.label == "switch":
                if self.set_value_data(value.id, True):
                    succes = True
                    break
                else:
                    succes = False
            else:
                succes = False

        return succes



    def switch_off(self):
        """
            method used for switch the relay off

                return:
                    if succes return true
                    else False
        """

        succes = False
        
        for value in self.values:
            if value.label == "switch":
                if self.set_value_data(value.id, False):
                    succes = True
                    break
                else:
                    succes = False
            else:
                succes = False

        return succes

    

    def serialize(self):
        data = super().serialize()

        #state
        data['state'] = self.state