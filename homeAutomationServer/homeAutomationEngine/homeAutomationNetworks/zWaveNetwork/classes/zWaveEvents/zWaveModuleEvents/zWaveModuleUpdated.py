from .zWaveModuleEvent import *

class ZWaveModuleUpdated(ZWaveModuleEvent):

	def __init__(self, moduleId, dateTime, location, Type="module updated", id=0):
		ZWaveModuleEvent.__init__(self, moduleId, dateTime, location, Type, id)

	def __str__(self):
		return "[{}]: le module n°{} as été mis a jour".format(self.dateTime, self.moduleId)