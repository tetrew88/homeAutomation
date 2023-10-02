from .zWaveModuleEvent import *

class ZWaveModuleRenamed(ZWaveModuleEvent):

	def __init__(self, moduleId, dateTime, location, Type="module renamed", id=0):
		ZWaveModuleEvent.__init__(self, moduleId, dateTime, location, Type, id)

	def __str__(self):
		return "[{}]: le module n°{} as été renomer".format(self.dateTime, self.moduleId)