class ZWaveEvent:
	"""
		bringing all the information of an zwave event

			parrametters:
				id: id of the event(int)
				type: type of event(str)
				dateTime: datetime of the event(str)

			methods:
				serialize: serialize the class
	"""
	
	def __init__(self, dateTime, Type="zWave event", id=0):
		self.id = id
		self.type = Type
		self.dateTime = dateTime


	def serialize(self):
		"""
    		method called for seriallize data of the class
    	"""

		data = {}

		data = {'id': self.id,
        'type': self.type,
        'dateTime': self.dateTime,
        'str': self.__str__()
        }

		return data


	def __str__(self):
		return "[{}]: {}".format(self.dateTime, self.type)