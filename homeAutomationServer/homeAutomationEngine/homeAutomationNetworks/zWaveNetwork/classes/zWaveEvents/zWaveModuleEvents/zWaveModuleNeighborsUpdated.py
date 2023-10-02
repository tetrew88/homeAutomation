from .zWaveModuleEvent import *

class ZWaveModuleNeighborsUpdated(ZWaveModuleEvent):

	def __init__(self, moduleId, dateTime, location, Type="module neighbors updated", id=0):
		ZWaveModuleEvent.__init__(self, moduleId, dateTime, location, Type, id)

	def __str__(self):
		return "[{}]: la liste de voisins du module n°{} as été mis a jour".format(self.dateTime, self.moduleId)