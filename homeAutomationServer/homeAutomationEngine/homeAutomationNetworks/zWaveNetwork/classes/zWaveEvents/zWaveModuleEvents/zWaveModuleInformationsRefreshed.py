from .zWaveModuleEvent import *

class ZWaveModuleInformationsRefreshed(ZWaveModuleEvent):

	def __init__(self, moduleId, dateTime, location, Type="module informations refreshed", id=0):
		ZWaveModuleEvent.__init__(self, moduleId, dateTime, location, Type, id)

	def __str__(self):
		return "[{}]: les informations du module n°{} ont été rafraichi".format(self.dateTime, self.moduleId)