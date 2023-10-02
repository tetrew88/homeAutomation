from ..zWaveModule import *


class ZWaveLightController(ZWaveModule):
	"""
		
	"""
		
		
	def __init__(self, id, name, location, values, parametters, manufacturerName, productName, productType, deviceType, type, canWakeUp, isAwake, isFailed, isReady, isSleeping, batteryLevel, commandClassAsString, level, lightUp, maxLevel, minLevel, startLevel, role="light controller"):
		"""constructor"""
		
		ZWaveModule.__init__(self, id, name, location, role, values, parametters, manufacturerName, productName, productType, deviceType, type, canWakeUp, isAwake, isFailed, isReady, isSleeping, batteryLevel, commandClassAsString)
		self.level = level
		self.lightUp = lightUp
		self.maxLevel = maxLevel
		self.minLevel = minLevel
		self.startLevel = startLevel


	def serialize(self):
		data = super().serialize()

		#level
		data['level'] = self.level

		#light up
		data['lightUp'] = self.lightUp

		#max level
		data['maxLevel'] = self.maxLevel

		#min level
		data['minLevel'] = self.minLevel

		#start level
		data['startLevel'] = self.startLevel

		return data
