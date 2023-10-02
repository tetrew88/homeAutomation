from .room import *

class Outside(Room):
	'''
        class bringing all the information and functionality of an outside
			
			Parametters:
				id: identifiant of the room
				name: name of the room
				type: type of room(outside)
    '''

	def __init__(self, id, name):
		Room.__init__(self, id, name, "outside")