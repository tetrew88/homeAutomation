from .zWaveModuleEvent import *

class ZWaveModuleHealed(ZWaveModuleEvent):

	def __init__(self, moduleId, dateTime, location, Type="module healed", id=0):
		ZWaveModuleEvent.__init__(self, moduleId, dateTime, location, Type, id)

	def __str__(self):
		return "[{}]: le module n°{} as été soigner".format(self.dateTime, self.moduleId)