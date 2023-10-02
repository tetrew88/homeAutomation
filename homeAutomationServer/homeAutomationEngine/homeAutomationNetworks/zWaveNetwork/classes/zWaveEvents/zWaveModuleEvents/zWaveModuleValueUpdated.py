from .zWaveModuleEvent import *

class ZWaveModuleValueUpdated(ZWaveModuleEvent):

	def __init__(self, moduleId, dateTime, location, valueId, Type="module value updated", id=0):
		ZWaveModuleEvent.__init__(self, moduleId, dateTime, location, Type, id)
		self.valueId = valueId

	def __str__(self):
		return "[{}]: la valeur n°{} du module n°{} as été mise a jour".format(self.dateTime, self.valueId, self.moduleId)