from .zWaveValue import *

class ZWaveParametter(ZWaveValue):
    """
        class used for representing an zwave parametters

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

    
    def __init__(self, zwaveValue, role="parametter"):
        ZWaveValue.__init__(self, zwaveValue, role)

    

    def serialize(self):
        return super().serialize()