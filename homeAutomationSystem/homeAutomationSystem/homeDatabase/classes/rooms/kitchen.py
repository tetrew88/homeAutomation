from .room import *

class Kitchen(Room):
	'''
        class bringing all the information and functionality of an kitchen
			
			Parametters:
				id: identifiant of the room
				name: name of the room
				type: type of room(kitchen)
    '''

	def __init__(self, id, name):
		Room.__init__(self, id, name, "kitchen")