class ZWaveValue:
    """
        class used for representing an zwave value

            attributes:
                zWave value: openzwave value class

            property:
                id: id of the value (int)
                data: data of the value
                dataItems: list of possible data for the value
                netwotkId: id network of the value
                label: label of the value(str)
                max: max value of the data
                min: min value of the data
                node id: id of the associated module
                type: type of the data
                units: unit of the data

            methods:
                set data: method used for modify the data of the value
                serialize: method used for serialize the class
    """


    def __init__(self, zwaveValue, role="value"):
        self.zwaveValue = zwaveValue
        self.role = role
        


    @property
    def id(self):
        """
            property representing the id of the value

                return:
                    id (int)
        """
        
        id = False
        
        try:
            id = int(self.zwaveValue.value_id)
        except:
            id = False

        return id


    @property
    def data(self):
        """
            property representing the data of the value

                return:
                    if succes data
                    else False
        """

        data = False

        try:
            data = self.zwaveValue.data
        except:
            data = False

        return data


    @property
    def dataItems(self):
        """
            property representing the data items list of the value
        
                return:
                    if values as data items return data item list
                    else return false
        """

        setValueList = False

        try:
            if isinstance(self.zwaveValue.data_items, set) or isinstance(self.zwaveValue.data_items, str):
                if isinstance(self.zwaveValue.data_items, str):
                    setValueList = self.zwaveValue.data_items
                else:
                    setValueList = []

                    for SetValue in self.zwaveValue.data_items:
                        setValueList.append(SetValue)
            else:
                setValueList = False
        except:
            setValueList = False

        return setValueList


    @property
    def networkId(self):
        """
            property representing the network id of the the value
        
                return:
                    if succes return network id
                    else false
        """

        networkId = False

        try:
            networkId = self.zwaveValue.id_on_network
        except:
            networkId = False

        return networkId


    @property
    def label(self):
        """
            property representing the label of the value

                return:
                    if succes return label (str)
                    else return false
        """

        label = False

        try:
            label = self.zwaveValue.label.lower()
        except:
            label = False

        return label


    @property
    def max(self):
        """
            property representing the max value of the data

                return:
                    if succes max value of the data
                    else false
        """

        max = False

        try:
            max = self.zwaveValue.max
        except:
            max = False

        return max


    @property
    def min(self):
        """
            property representing the max value of the data

                return:
                    if succes min value of the data
                    else false
        """

        min = False

        try:
            min = self.zwaveValue.min
        except:
            min = False

        return min


    @property
    def nodeId(self):
        """
            property representing the node id contained the value
        
                return:
                    if succes return the id of the node contained the value (int)
                    else False
        """

        nodeId = False

        try:
            nodeId = int(self.zwaveValue.node)
        except:
            nodeId = False
        
        return nodeId


    @property
    def type(self):
        """
            property representing the type of the value

                return:
                    if succes return type of the value (str)
                    else False
        """

        type = False

        try:
            type = self.zwaveValue.type.lower()
        except:
            type = False

        return type


    @property
    def units(self):
        """
            property representing the unit of the value

                return:
                    if succes return unit of the value (str)
                    else False
        """

        units = False

        try:
            units = self.zwaveValue.units
        except:
            units = False

        return units


    def set_data(self, newData):
        """
            method allow to set the value data

                parametter:
                    new data: new data of the value
        """

        newDataIsValid = succes = False

        #test newData
        if self.type == 'int' or self.type == 'byte' or self.type == 'short':
            if isinstance(newData, int):
                newDataIsValid = True
            else:
                newDataIsValid = False

        elif self.type == 'bool' or self.type == "button":
            if isinstance(newData, bool):
                newDataIsValid = True
            else:
                newDataIsValid = False

        elif self.type == 'decimal':
            if isinstance(newData, float) or isinstance(newData, int):
                newDataIsValid = True
            else:
                newDataIsValid = False

        elif self.type == "string":
            if isinstance(newData, str):
                newDataIsValid = True
            else:
                newDataIsValid = False

        elif self.type == "list":
            if isinstance(newData, list) or isinstance(newData, str):
                newDataIsValid = True
            else:
                newDataIsValid = False

        #set data
        if newDataIsValid:
            try:
                self.zwaveValue.data = newData
                succes = True
            except:
                succes = False
        else:
            succes = False

        return succes


    def __str__(self):
        return "'{}' {}: {} '{}".format(self.id, self.label, self.data, self.type)

    
    def serialize(self):
        data = {}

        #value id
        data['id'] = self.id

        #data
        data['data'] = self.data

        #data items
        data['dataItems'] = self.dataItems

        #label
        data['label'] = self.label

        #network id
        data['networkId'] = self.networkId

        #max
        data['max'] = self.max

        #min
        data['min'] = self.min

        #node id
        data['nodeId'] = self.nodeId

        #type
        data['type'] = self.type

        #unit
        data["units"] = self.units

        #role
        data['role'] = self.role

        return data
