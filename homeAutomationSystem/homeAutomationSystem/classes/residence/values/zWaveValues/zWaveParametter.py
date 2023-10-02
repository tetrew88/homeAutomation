from .zWaveValue import *

class ZWaveParametter(ZWaveValue):
    """
        
    """

    
    def __init__(self, id, label, data, dataItems, networkId, max, min, nodeId, type, units):
        ZWaveValue.__init__(self, id, label, data, dataItems, networkId, max, min, nodeId, type, units)