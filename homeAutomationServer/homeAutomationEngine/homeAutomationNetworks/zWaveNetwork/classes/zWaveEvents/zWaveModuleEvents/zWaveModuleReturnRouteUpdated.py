from .zWaveModuleEvent import *

class ZWaveModuleReturnRouteUpdated(ZWaveModuleEvent):

	def __init__(self, moduleId, dateTime, location, Type="module return route updated", id=0):
		ZWaveModuleEvent.__init__(self, moduleId, dateTime, location, Type, id)

	def __str__(self):
		return "[{}]: la route de retour du module n°{} as été mis a jour".format(self.dateTime, self.moduleId)