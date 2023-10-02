from .zWaveModuleEvent import *

class ZWaveModuleReady(ZWaveModuleEvent):

	def __init__(self, moduleId, dateTime, location, Type="module ready", id=0):
		ZWaveModuleEvent.__init__(self, moduleId, dateTime, location, Type, id)

	def __str__(self):
		return "[{}]: le module n°{} est prêt".format(self.dateTime, self.moduleId)