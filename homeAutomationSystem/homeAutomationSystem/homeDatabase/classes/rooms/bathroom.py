from .room import *

class Bathroom(Room):
	'''
        class bringing all the information and functionality of an bathroom
			
			Parametters:
				id: identifiant of the room
				name: name of the room
				type: type of room(bathroom)
    '''

	def __init__(self, id, name):
		Room.__init__(self, id, name, "bathroom")