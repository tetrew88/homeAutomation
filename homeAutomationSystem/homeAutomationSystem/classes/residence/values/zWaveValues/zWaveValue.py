from ..value import *

class ZWaveValue(Value):
    """
        

    """


    def __init__(self, id, label, data, dataItems, networkId, max, min, nodeId, type, units):
        Value.__init__(id, label, data)
        self.dataItems = dataItems
        self.networkId = networkId
        self.max = max
        self.min = min
        self.nodeId = nodeId
        self.type = type
        self.units = units
        

    
    def serialize(self):
        data = super().serialize()

        #data items
        data['dataItems'] = self.dataItems

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

        return data
