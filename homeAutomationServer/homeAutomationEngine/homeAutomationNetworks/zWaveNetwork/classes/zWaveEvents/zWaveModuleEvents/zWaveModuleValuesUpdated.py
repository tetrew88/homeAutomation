from .zWaveModuleEvent import *

class ZWaveModuleValuesUpdated(ZWaveModuleEvent):

	def __init__(self, moduleId, dateTime, location, Type="module values updated", id=0):
		ZWaveModuleEvent.__init__(self, moduleId, dateTime, location, Type, id)

	def __str__(self):
		return "[{}]: les valeurs du module n°{} ont été mise a jour".format(self.dateTime, self.moduleId)