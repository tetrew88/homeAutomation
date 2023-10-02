class Event:
	def __init__(self, id, type, datetime, location):
		self.id = id
		self.type = type
		self.datetime = datetime
		self.location = location



	def serialize(self):
		"""
    		method called for seriallize data of the class
    	"""

		data = {}

		data = {'id': self.id,
        'type': self.type,
        'datetime': self.datetime,
        'location': self.location
        }

		return data