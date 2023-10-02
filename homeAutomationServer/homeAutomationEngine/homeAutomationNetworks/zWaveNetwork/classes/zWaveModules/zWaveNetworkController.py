from .zWaveModule import *

class ZWaveNetworkController(ZWaveModule):

    def __init__(self, zwaveController, type='network controller'):
        ZWaveModule.__init__(self, zwaveController.node, type)
        self.zwaveController = zwaveController


    def add_node(self):
        succes = False

        try:
            self.zwaveController.add_node()
            succes = True
        except:
            succes = False

        return succes


    def remove_node(self):
        succes = False

        try:
            self.zwaveController.remove_node()
            succes = True
        except:
            succes = False

        return succes


    def soft_reset_network(self):
        succes = False

        try:
            self.zwaveController.soft_reset()
            succes = True
        except:
            succes = False

        return succes


    def hard_reset_network(self):
        succes = False

        try:
            self.zwaveController.hard_reset()
            succes = True
        except:
            succes = False

        return succes