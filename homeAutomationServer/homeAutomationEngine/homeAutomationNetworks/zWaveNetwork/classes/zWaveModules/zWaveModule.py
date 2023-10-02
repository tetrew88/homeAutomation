from ..zWaveValues.zWaveValue import *
from ..zWaveValues.zWaveParametter import *


class ZWaveModule:
    '''
        class bringing all the information and functionality of an module
            
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


    def __init__(self, moduleNode, role="module"):
        """constructor"""
        
        self.moduleNode = moduleNode
        self.role = role
        self.protocol = "zWave"



    @property
    def id(self):
        """
            property representing the module identifier
                
                return: 
                    module id (int)
        """

        id = False

        try:
            id = int(self.moduleNode.node_id)
        except:
            id = False

        return id


    @property
    def name(self):
        """
            property representing the name of the module
                
                return: 
                    name of the module (str)
        """
        name = False

        try:
            name = self.moduleNode.name
        except:
            name = False

        if name == "" or name == False:
            name = self.productName
        else:
            pass
        
        return name


    @property
    def location(self):
        """
            property representing the location of the module (room id)
                return: 
                    room id (int)
        """

        location = False
        
        try:
            location = int(self.moduleNode.location)
        except:
            location = False

        return location


    @property
    def manufacturerName(self):
        """
            property representing the manufacturer name of the module
                
                return: 
                    manufacturer name of the module (str)
        """

        manufacturerName = False

        try:
            manufacturerName = self.moduleNode.manufacturer_name
        except:
            manufacturerName = False

        return manufacturerName


    @property
    def productName(self):
        """
            property representing the product name of the module
                
                return:
                    product name of the module (str)
        """

        productName = False

        try:
            productName = self.moduleNode.product_name
        except:
            productName = False

        return productName


    @property
    def productType(self):
        """
            property representing the product type of the module
                
                return:
                    product type of the module(str)
        """

        productType = False

        try:
            productType = self.moduleNode.product_type
        except:
            productType = False

        return productType


    @property
    def deviceType(self):
        """
            property representing the device type of the module
                return:
                    device type of the module(str)
        """

        deviceType = False

        try:
            deviceType = self.moduleNode.device_type
        except:
            deviceType = False

        return deviceType


    @property
    def type(self):
        """
            property representing the type of the module
                return: 
                    type of the module(str)
        """

        type = False

        try:
            type = self.moduleNode.type
        except:
            type = False

        return type

    
    @property 
    def values(self):
        """
            property representing the values of the module

                return:
                    value list(list)
        """
        
        valueList = []
        tmpValueList = False

        try:
            tmpValueList = self.moduleNode.get_values(class_id='All', genre='All', type='All', readonly='All', writeonly='All', index='All', label='All')

            for value in tmpValueList:
                if tmpValueList[value].is_read_only == True:
                    try:
                        valueList.append(ZWaveValue(tmpValueList[value]))
                    except:
                        pass
                else:
                    try:
                        valueList.append(ZWaveParametter(tmpValueList[value]))
                    except:
                        pass
        except:
            pass

        return valueList


    @property
    def parametters(self):
        """
            property representing the parametters of the module

                return:
                    parametters list (list)
        """
        
        paramettersList = []

        try:
            for value in self.values:
                if isinstance(value, ZWaveParametter):
                    paramettersList.append(value)
                else:
                    pass
        except:
            pass

        return paramettersList


    @property
    def canWakeUp(self):
        """
            property allows to know if an module can wake up

                return:
                    false/true
        """
        
        canWakeUp = False

        try:
            canWakeUp = self.moduleNode.can_wake_up()
        except:
            canWakeUp = False

        return canWakeUp


    @property
    def isAwake(self):
        """
            property representing if the module is awake or not
                return: 
                    False/True
        """

        isAwake = False

        try:
            isAwake = self.moduleNode.is_awake
        except:
            isAwake = False

        return isAwake


    @property
    def isFailed(self):
        """
            property representing if the module is failed or not
                return:
                    False/True
        """

        isFailed = True

        try:
            isFailed = self.moduleNode.is_failed
        except:
            isFailed = True

        return isFailed


    @property
    def isReady(self):
        """
            property representing if the module is ready or not
                return:
                    False/True
        """

        isReady = False

        try:
            isReady = self.moduleNode.is_ready
        except:
            isReady = False

        return isReady


    @property
    def isSleeping(self):
        """
            property representing if the module is sleeping or not
                return:
                    False/True
        """

        isSleeping = False

        try:
            isSleeping = self.moduleNode.is_sleeping
        except:
            isSleeping = False

        return isSleeping


    @property
    def batteryLevel(self):
        """
            property representin the batterie level of an module

                return:
                    battery level(int)/none
        """
        batteryLevel = False

        try:
            batteryLevel = int(self.moduleNode.get_battery_level())
        except:
            batteryLevel = False

        return batteryLevel


    @property
    def commandClassAsString(self):
        """
            property representing the list of command class as string

                return:
                    command class list (list(str))
        """

        commandClassAsString = False

        try:
            commandClassAsString = self.moduleNode.command_classes_as_string
        except:
            commandClassAsString = False

        return commandClassAsString



    """GET METHOD"""
    def get_value(self, valueId):
        """
            method used for getting an value of the module

                parametters:
                    valueID: int

                fonctionning:
                    return value of value list which corresponds at the value id parametter

                return:
                    if value was found return value
                    else return false
        """
        
        selectedValue = False

        if isinstance(valueId, int):
            for value in self.values:
                if value.id == valueId:
                    selectedValue = value
                    break
                else:
                    selectedValue = False
        else:
            selectedValue = False

        return selectedValue



    """SET METHOD"""
    def set_name(self, newName):
        """
            methods called for set an module's name.
                Parametters:
                    newName: str
                functionning:
                    set the module's name
                        if the module's name was correctly modified:
                            return True
                        else:
                            return False
                return:
                    succes: True/False
        """
        succes = False

        if isinstance(newName, str):
            try:
                self.moduleNode.set_field('name', newName)
                if self.update_network():
                    succes = True
                else:
                    succes = False
            except:
                succes = False
        else:
            succes = False


        return succes


    def set_location(self, newLocation):
        """
            methods called for set an module's location.
                functionning:
                    set the module's location
                        if the module's location was correctly modified:
                            return True
                        else:
                            return False
                return:
                    succes: True/False
        """

        succes = False

        if isinstance(newLocation, int):
            try:
                self.moduleNode.set_field('location', str(newLocation))
                if self.update_network():
                    succes = True
                else:
                    succes = False
            except:
                succes = False
        else:
            succes = False


        return succes


    def set_value_data(self, valueId, data):
        """
            method used for modify an value (data of the value)

                functioning:
                    get the value
                    ask to value to set his date
                    update module network

                return:
                    true/false
        """

        value = succes = False

        if isinstance(valueId, int):
            value = self.get_value(valueId)
            if value != False:
                if value.set_data(data):
                    if self.update_network():
                        succes = True
                    else:
                        succes = False
                else:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        return succes



    """UPDATE METHOD"""
    def update_return_route(self):
        """
            method used for update return route

                return:
                    true/false
        """

        returnRouteUpdated = False

        try :
            self.moduleNode.assign_return_route()
            returnRouteUpdated = True
        except:
            returnRouteUpdated = False

        return returnRouteUpdated


    def update_neighbors(self):
        """
            method used for update neighbors list of the module

                return:
                    True/False
        """
        
        neighborsUpdated = False

        try:
            self.moduleNode.neighbor_update()
            neighborsUpdated = True
        except:
            neighborsUpdated = False

        return neighborsUpdated


    def update_network(self):
        """
            method used for update network of the module

                return:
                    True/False
        """
        
        networkUpdated = False

        try:
            self.moduleNode.network_update()
            networkUpdated = True
        except:
            networkUpdated = False

        return networkUpdated



    """REFRESH METHOD"""
    def refresh_info(self):
        """
            method used for refresh the information of the module

                return:
                    True/False
        """
        
        infoRefreshed = False

        try:
            self.moduleNode.refresh_info()
            infoRefreshed = True
        except:
            infoRefreshed = False

        return infoRefreshed


    def refresh_value(self, valueId):
        """
            method used for refresh an value of the module

                parametters:
                    id of the value (int)

                return:
                    True/False
        """
        
        valueRefreshed = False

        if isinstance(valueId, int):
            try:
                self.moduleNode.refresh_value(valueId)
                valueRefreshed = True
            except:
                valueRefreshed = False
        else:
            valueRefreshed = False

        return valueRefreshed


    def refresh_values(self):
        """
            method used for refresh all the value of the node

                retun:
                    False/True
        """

        valuesRefreshed = False
        
        for value in self.values:
            if self.refresh_value(value.id):
                valuesRefreshed = True
            else:
                valuesRefreshed = False
                break

        return valuesRefreshed



    """HEAL METHOD"""
    def heal(self):
        """
            method used for heal the module

                return:
                    True/False
        """
        
        moduleHealed = False

        try:
            self.moduleNode.heal()
            moduleHealed = True
        except:
            moduleHealed = False

        return moduleHealed



    """STR METHOD"""
    def __str__(self):
        return "id: {}\nnom: {}\nemplacement: {}\nniveau de batterie: {}\n\nreveiller: {}\nechec: {}\npret: {}\n\nnom du fabriquant: {}\nnom de produit: {}\ntype de produit: {}\ntype de systeme: {}\nrole: {}\ntype: {}\n\nvaleurs:\n    {}\n\nparamettre:\n    {}\n\nclasse de commande:\n    {}\n\n".format(self.id, self.name, self.location, self.batteryLevel, self.isAwake, self.isFailed, self.isReady, self.manufacturerName, self.productName, self.productType, self.deviceType, self.role, self.type, self.values, self.parametters, self.commandClassAsString)



    """serialize method"""
    def serialize(self):
        data = {}

        #module id
        data['id'] = self.id

        #module name
        data['name'] = self.name

        #module location
        data['location'] = self.location

        #manufacturer name
        data['manufacturerName'] = self.manufacturerName

        #product name
        data['productName'] = self.productName

        #product type
        data['productType'] = self.productType

        #device type
        data['deviceType'] = self.deviceType

        #type
        data['type'] = self.type

        #values
        data['values'] = []

        for value in self.values:
            data['values'].append(value.serialize())

        #parametters
        data['parametters'] = []

        for parametter in self.parametters:
            data['parametters'].append(parametter.serialize())

        #can wake up
        data['canWakeUp'] = self.canWakeUp

        #is awake
        data['isAwake'] = self.isAwake

        #is failed
        data['isFailed'] = self.isFailed

        #is ready
        data['isReady'] = self.isReady

        #is sleeping
        data['isSleeping'] = self.isSleeping

        #battery level
        data['batteryLevel'] = self.batteryLevel

        #command class
        data['commandClassAsString'] = self.commandClassAsString

        #role
        data['role'] = self.role

        data["protocol"] = self.protocol

        return data