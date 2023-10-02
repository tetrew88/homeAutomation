from .zWaveModuleEvent import *

class ZWaveModuleMoved(ZWaveModuleEvent):

	def __init__(self, moduleId, dateTime, location, Type="module moved", id=0):
		ZWaveModuleEvent.__init__(self, moduleId, dateTime, location, Type, id)

	def __str__(self):
		return "[{}]: le module n°{} as été déplacer".format(self.dateTime, self.moduleId)