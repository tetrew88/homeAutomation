from ..zWaveEvent import *

class ZWaveModuleEvent(ZWaveEvent):
	"""
		class bringing all the information and functionality of an event
			Parametters:
				moduleId: module id(int)
				type: type of event (motion detection, light on, ...) (str)
				datetime: datetime of the event (str)
				location: location of the event (roomId(int))
			Attributes:
				type: type of event (motion detection, light on, ...) (str)
				datetime: datetime of the event (str)
				moduleId: module id(int)
				location: location of the event (roomId(int))
			methods:
				serialize (allows to transform the class in dict for json use)
	"""

	def __init__(self, moduleId, dateTime, location, Type="module event", id=0):
		ZWaveEvent.__init__(self, dateTime, Type, id)
		self.moduleId = moduleId
		self.location = location


	def serialize(self):
		"""
    		method called for seriallize data of the class
    	"""

		data = {}

		data = {'id': self.id,
        'type': self.type,
        'dateTime': self.dateTime,
		'moduleId': self.moduleId,
        'location': self.location,
        'str': self.__str__()
        }

		return data

	def __str__(self):
		return "[{}]: {}".format(self.dateTime, self.type)