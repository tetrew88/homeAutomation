from .room import *

class Livingroom(Room):
	'''
        class bringing all the information and functionality of an livingroom
			
			Parametters:
				id: identifiant of the room
				name: name of the room
				type: type of room(livingroom)
    '''

	def __init__(self, id, name):
		Room.__init__(self, id, name, "livingroom")