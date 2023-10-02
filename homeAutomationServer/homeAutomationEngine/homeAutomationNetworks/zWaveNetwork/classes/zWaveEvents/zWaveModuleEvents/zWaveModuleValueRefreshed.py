from .zWaveModuleEvent import *

class ZWaveModuleValueRefreshed(ZWaveModuleEvent):

	def __init__(self, moduleId, dateTime, location, valueId, Type="module value refreshed", id=0):
		ZWaveModuleEvent.__init__(self, moduleId, dateTime, location, Type, id)
		self.valueId = valueId

	def __str__(self):
		return "[{}]: la valeurs n°{} du module n°{} as été rafraichi".format(self.dateTime, self.valueId, self.moduleId)