import json
import mysql.connector

from .users.administrator import *
from .users.guest import *
from .users.inhabitant import *
from .users.user import *
from .users.profil import *

from .rooms.room import *
from .rooms.bathroom import *
from .rooms.bedroom import *
from .rooms.corridor import *
from .rooms.kitchen import *
from .rooms.livingroom import *
from .rooms.outside import *

from .events.event import *



class HomeDatabase:
	"""
		class bringing all the information and functionality of the home database.

			Attributes:
				config file path: path to the config file
                host: host of the database

                db_connection
                db_cursor

			Property:
				username: username used for database connection
				database name: name of the database
                database password: password for the database

			Methods:
				connect
				disconnect
				commit_change

				get_users_list
				get_profils_list
				get_inhabitant_List
				get_guest_list
				get_administrator_list
				get_profil_by_id

				add_user
				add_profil
				
				check_config_file_existence
				check_database_connection
	"""


	def __init__(self, configFilePath):
		self.configFilePath = configFilePath
		self.host = "localHost"

		self.db_connection = False
		self.db_cursor = False



	@property
	def databaseName(self):
		"""
			property allowing to retrieve the database name from config file

			functionning:
				1.check config file existance
				2.collecte data
				3.select database name data
				4.return

			return:
				if succes:
					databaseName(str)
				else:
					False
		"""

		succes = data = databaseName = False

		#check config file existance
		if self.check_config_file_existence() is True:
			try:
				#collecte data
				with open(self.configFilePath) as configFile:
				    data = json.load(configFile)
			except:
				data = False
		else:
			data = False

		if data is not False:
			try:
				#select database name data
				databaseName = data['databaseName']
			except KeyError:
				databaseName = False

		if databaseName is not False:
			succes = True
		else:
			succes = False

		#return
		if succes:
			return databaseName
		else:
			return False


	@property
	def username(self):
		"""
			property allowing to retrieve the username from config file

			functionning:
				1.check config file existance
				2.collecte data
				3.select system user name data
				4.return


			return:
				if succes:
					username(str)
				else:
					False
		"""

		succes = data = username = False

		#check config file existance
		if self.check_config_file_existence() is True:
			try:
				#collecte data
				with open(self.configFilePath) as configFile:
				    data = json.load(configFile)
			except:
				data = False
		else:
			data = False

		if data is not False:
			try:
				#select system user name data
				username = data['systemUserName']
			except KeyError:
				username = False

		if username is not False:
			succes = True
		else:
			succes = False

		#return
		if succes:
			return username
		else:
			return False


	@property
	def password(self):
		"""
			property allowing to retrieve the user password from config file

			functionning:
				1.check config file existance
				2.collecte data
				3.select system user password data
				4.return

			return:
				if succes:
					password(str)
				else:
					False
		"""

		succes = data = password = False

		#check config file existance
		if self.check_config_file_existence() is True:
			try:
				#collecte data
				with open(self.configFilePath) as configFile:
				    data = json.load(configFile)
			except:
				data = False
		else:
			data = False

		if data is not False:
			try:
				#select system user password data
				password = data['systemUserPassword']
			except KeyError:
				password = False

		if password is not False:
			succes = True
		else:
			succes = False

		#return
		if succes:
			return password
		else:
			return False



	#base method
	def connect(self):
		"""
			method called for establish connection with the home database

			functionning:
				1.check if connection wasn't aleady established
				2.establish the connection
				3.check if connection succes
				4.return

			return:
				succes (True/False)
		"""

		succes = False

		#check if connection wasn't aleady established
		if self.db_connection == False or self.db_cursor == False:
			try:
				#establish the connection
				self.db_connection = mysql.connector.connect(
					host=self.host,
					user=self.username,
					passwd=self.password,
					database=self.databaseName
				)
				self.db_cursor = self.db_connection.cursor(buffered=True)
			except Exception as e:
				self.db_connection = False
				self.db_cursor = False

			#check if connection succes
			if self.db_connection == False or self.db_cursor == False:
				succes = False
			else:
				succes = True
		else:
			succes = True

		#return
		return succes
		

	def disconnect(self):
		"""
			method called for cut the connection with the home database

			functioning:
				1.test if connection wasn't already disconnected
				2.disconnection of the database
				3.return


			return:
				succes (True/False)
		"""

		succes = False

		#test if connection wasn't already disconnected
		if self.db_connection is not False:
			try:
				#disconnection of the database
				self.db_connection.close()
				self.db_cursor = False
				self.db_connection = False

				succes = True
			except:
				succes = False
		else:
			succes = True

		#return
		return succes


	def commit_change(self):
		"""
			method called for commit change to the database

			functionnement:
				1.test if connection was established
				2.commit change in datatabase
				3.return

			return:
				succes (True/False)
		"""

		succes = False

		#test if connection was established 
		if self.db_connection != False:
			try:
				#commit change in datatabase
				self.db_connection.commit()
				succes = True
			except:
				succes = False
		else:
			succes = False

		#return
		return succes



	#get method
	def get_users_list(self):
		"""
    		method called for get an list of user

			functioning:
				1.connect to the database
				2.get all user in database
				3.database disconnection
				4.transform all user in database on user instance classe
				5.check user list conformity
				6.return
    		
			return:
    			list of user class
    	"""

		succes = tmpUsersList = usersList = False

		request = """SELECT * FROM Users"""

		#connect to the database
		if self.connect():
			try:
				#get all user in database
				self.db_cursor.execute(request)
				tmpUsersList = self.db_cursor.fetchall()
			except:
				tmpUsersList = False
			finally:
				#database disconnection
				self.disconnect()
		else:
			tmpUsersList = False

		#transform all user in database on user instance classe
		if tmpUsersList != False:
			usersList = []

			if len(tmpUsersList) > 0:
				for user in tmpUsersList:
					userProfil = False
					userProfil = self.get_profil_by_id(int(user[1]))

					if userProfil != False:
						try:
							if user[2] == "admin":
								usersList.append(Administrator(user[0], userProfil, user[3], user[4], user[5], user[6]))
							elif user[3] == "inhabitant":
									usersList.append(Inhabitant(user[0], userProfil, user[2], user[4], user[5], user[6]))
							elif user[3] == 'guest':
								usersList.append(Guest(user[0], userProfil, user[2], user[4], user[5], user[6]))
						except:
							pass
					else:
						pass
			else:
				usersList = []
		else:
			succes = False

		#check user list conformity
		if usersList != False:
			if len(usersList) > 0:
				for user in usersList:
					if isinstance(user, User):
						succes = True
					else:
						succes = False
						break
			else:
				succes = True
		else:
			succes = False

		#return
		if succes:
			return usersList
		else:
			return False

		
	def get_profils_list(self):
		"""
    		method called for get an list of profil

			functioning:
				1.connect to the database
				2.get all profil in database
				3.database disconnection
				4.transform all profil in database on profils instance classe
				5.check profil list conformity
				6.return
    		
			return:
    			list of profil class
    	"""

		succes = tmpProfilsList = profilsList = False

		request = """SELECT * FROM Profils"""

		#connect to the database
		if self.connect():
			try:
				#get all profil in database
				self.db_cursor.execute(request)
				tmpProfilsList = self.db_cursor.fetchall()
			except:
				tmpProfilsList = False
			finally:
				self.disconnect()
		else:
			tmpProfilsList = False

		#transform all profil in database on profils instance classe
		if tmpProfilsList != False:
			profilsList = []

			if len(tmpProfilsList) > 0:
				for profil in tmpProfilsList:
					try:
						profilsList.append(Profil(profil[0], profil[1], profil[2], profil[3], profil[4]))
					except:
						profilsList = False
			else:
				profilsList = []
		else:
			profilsList = False

		#check profil list conformity
		if profilsList != False:
			if len(profilsList) > 0:
				for profil in profilsList:
					if isinstance(profil, Profil):
						succes = True
					else:
						profilsList = False
						break
			else:
				succes = True
		else:
			succes = False

		if succes:
			return profilsList
		else:
			return False


	def get_inhabitants_List(self):
		"""
    		method called for get an list of inhabitant

			functioning:
				1.connect to the database
				2.get all inhabitant in database
				3.database disconnection
				4.transform all inhabitant in database on inhabitant instance classe
				5.check inhabitant list conformity
				6.return
    		
			return:
    			list of inhabitant class
    	"""

		succes = tmpInhabitantList = inhabitantList = False

		request = """SELECT * FROM Users WHERE role = 'inhabitant'"""

		#connect to the database
		if self.connect():
			try:
				#get all inhabitant in database
				self.db_cursor.execute(request)
				tmpInhabitantList = self.db_cursor.fetchall()
			except:
				tmpInhabitantList = False
			finally:
				#database disconnection
				self.disconnect()
		else:
			tmpInhabitantList = False

		#transform all inhabitant in database on inhabitant instance classe
		if tmpInhabitantList != False:
			inhabitantList = []

			if len(tmpInhabitantList) > 0:
				for inhabitant in tmpInhabitantList:
					inhabitantProfil = False
					inhabitantProfil = self.get_profil_by_id(int(inhabitant[1]))

					if inhabitantProfil != False:
						try:
							if inhabitant[2] == "admin":
								inhabitantList.append(Administrator(inhabitant[0], inhabitantProfil, inhabitant[4], inhabitant[5], inhabitant[6]))
							else:
								inhabitantList.append(Inhabitant(inhabitant[0], inhabitantProfil, inhabitant[2], inhabitant[4], inhabitant[5], inhabitant[6]))
						except:
							pass
					else:
						pass
			else:
				inhabitantList = []
		else:
			succes = False

		#check inhabitant list conformity
		if inhabitantList != False:
			if len(inhabitantList) > 0:
				for inhabitant in inhabitantList:
					if isinstance(inhabitant, Inhabitant):
						succes = True
					else:
						succes = False
						break
			else:
				succes = True
		else:
			succes = False

		#return
		if succes:
			return inhabitantList
		else:
			return False


	def get_guests_list(self):
		"""
    		method called for get an list of guest

			functioning:
				1.connect to the database
				2.get all guest in database
				3.database disconnection
				4.transform all guest in database on guest instance classe
				5.check guest list conformity
				6.return
    		
			return:
    			list of guest class
    	"""

		succes = tmpGuestList = guestList = False

		request = """SELECT * FROM Users WHERE role = 'guest'"""

		#connect to the database
		if self.connect():
			try:
				#get all guest in database
				self.db_cursor.execute(request)
				tmpGuestList = self.db_cursor.fetchall()
			except:
				tmpGuestList = False
			finally:
				#database disconnection
				self.disconnect()
		else:
			tmpGuestList = False

		#transform all guest in database on guest instance classe
		if tmpGuestList != False:
			guestList = []

			if len(tmpGuestList) > 0:
				for guest in tmpGuestList:
					guestProfil = False
					guestProfil = self.get_profil_by_id(int(guest[1]))

					if guestProfil != False:
						try:
							guestList.append(Guest(guest[0], guestProfil, guest[4], guest[5], guest[6]))
						except:
							pass
					else:
						pass
			else:
				guestList = []
		else:
			succes = False

		#check guest list conformity
		if guestList != False:
			if len(guestList) > 0:
				for guest in guestList:
					if isinstance(guest, Guest):
						succes = True
					else:
						succes = False
						break
			else:
				succes = True
		else:
			succes = False

		#return
		if succes:
			return guestList
		else:
			return False


	def get_administrators_list(self):
		"""
    		method called for get an list of administator

			functioning:
				1.connect to the database
				2.get all administator in database
				3.database disconnection
				4.transform all inhabitant in administator on inhabitant instance classe
				5.check administator list conformity
				6.return
    		
			return:
    			list of administator class
    	"""

		succes = tmpAdministatorList = administatorList = False

		request = """SELECT * FROM Users WHERE grade = 'admin'"""

		#connect to the database
		if self.connect():
			try:
				#get all administator in database
				self.db_cursor.execute(request)
				tmpAdministatorList = self.db_cursor.fetchall()
			except:
				tmpAdministatorList = False
			finally:
				#database disconnection
				self.disconnect()
		else:
			tmpAdministatorList = False

		#transform all inhabitant in administator on inhabitant instance classe
		if tmpAdministatorList != False:
			administatorList = []

			if len(tmpAdministatorList) > 0:
				for administator in tmpAdministatorList:
					administatorProfil = False
					administatorProfil = self.get_profil_by_id(int(administator[1]))

					if administatorProfil != False:
						try:
							administatorList.append(Administrator(administator[0], administatorProfil, administator[4], administator[5], administator[6]))
						except:
							pass
					else:
						pass
			else:
				administatorList = []
		else:
			succes = False

		#check administator list conformity
		if administatorList != False:
			if len(administatorList) > 0:
				for administator in administatorList:
					if isinstance(administator, Administrator):
						succes = True
					else:
						succes = False
						break
			else:
				succes = True
		else:
			succes = False

		#return
		if succes:
			return administatorList
		else:
			return False


	def get_rooms_list(self):
		succes = tmpRoomsList = roomsList = False

		request = """SELECT * FROM Rooms"""

		#connect to the database
		if self.connect():
			try:
				#get all user in database
				self.db_cursor.execute(request)
				tmpRoomsList = self.db_cursor.fetchall()
			except:
				tmpRoomsList = False
			finally:
				#database disconnection
				self.disconnect()
		else:
			tmpRoomsList = False


		if tmpRoomsList != False:
			roomsList = []

			if len(tmpRoomsList) > 0:
				for room in tmpRoomsList:
					try:
						if room[2] == 'bathroom':
							roomsList.append(Bathroom(room[0], room[1]))
						elif room[2] == 'bedroom':
							roomsList.append(Bedroom(room[0], room[1]))
						elif room[2] == 'corridor':
							roomsList.append(Corridor(room[0], room[1]))
						elif room[2] == 'kitchen':
							roomsList.append(Kitchen(room[0], room[1]))
						elif room[2] == 'livingroom':
							roomsList.append(Livingroom(room[0], room[1]))
						elif room[2] == 'outside':
							roomsList.append(Outside(room[0], room[1]))
						else:
							roomsList.append(Room(room[0], room[1], room[2]))		
					except:
						pass

				for room in roomsList:
					room.events = self.get_room_events(room.id)
			else:
				roomsList = []
		else:
			succes = False

		#check room list conformity
		if roomsList != False:
			if len(roomsList) > 0:
				for room in roomsList:
					if isinstance(room, Room):
						succes = True
					else:
						succes = False
						break
			else:
				succes = True
		else:
			succes = False

		#return
		if succes:
			return roomsList
		else:
			return False


	def get_events_list(self):
		succes = tmpEventsList = eventsList = False

		request = """SELECT * FROM Events"""

		#connect to the database
		if self.connect():
			try:
				#get all event in database
				self.db_cursor.execute(request)
				tmpEventsList = self.db_cursor.fetchall()
			except:
				tmpEventsList = False
			finally:
				#database disconnection
				self.disconnect()
		else:
			tmpEventsList = False

		if tmpEventsList != False:
			eventsList = []

			if len(tmpEventsList) > 0:
				for event in tmpEventsList:
					try:
						eventsList.append(Event(event[0], event[1], event[2], event[3]))			
					except:
						pass
			else:
				eventsList = []
		else:
			succes = False

		#check event list conformity
		if eventsList != False:
			if len(eventsList) > 0:
				for event in eventsList:
					if isinstance(event, Event):
						succes = True
					else:
						succes = False
						break
			else:
				succes = True
		else:
			succes = False

		#return
		if succes:
			return eventsList
		else:
			return False


	def get_profil_by_id(self, profilId):
		"""
    		method called for get an specific profil
				functionning:
					1.connect to database
					2.ask to database to select the profil with an predefined id
					3.database disconnection
					4.transform alprofil in profil instance classe
					5.check profil conformity
					6.return
    			return:
    				profil class/False
    	"""

		profil = succes = False

		#connect to database
		if isinstance(profilId, int):
			if self.connect():
				request = "SELECT * FROM Profils WHERE id = {}".format(profilId)
				
				try:
					#ask to database to select the profil with an predefined id
					self.db_cursor.execute(request)
					profil = self.db_cursor.fetchall()
				except:
					profil = False
				finally:
					#database disconnection
					self.disconnect()

				if profil != False:
					#transform profil in profil instance classe
					if len(profil) > 0:
						profil = profil[0]
						profil = Profil(profil[0], profil[1], profil[2], profil[3], profil[4])
					else:
						profil = False
				else:
					profil = False
			else:
				profil = False
		else:
			profil = False

		#check profil conformity
		if profil != False:
			if isinstance(profil, Profil):
				succes = True
			else:
				succes = False
		else:
			succes = False

		#return
		if succes:
			return profil
		else:
			return False


	#a ajouter au test
	def get_user_by_id(self, userId):
		user = userProfil = succes = False

		#connect to database
		if isinstance(userId, int):
			if self.connect():
				request = "SELECT * FROM Users WHERE id = {}".format(userId)
				
				try:
					#ask to database to select the user with an predefined id
					self.db_cursor.execute(request)
					user = self.db_cursor.fetchall()
				except:
					user = False
				finally:
					#database disconnection
					self.disconnect()

				if user != False:
					#transform user in user instance classe
					if len(user) > 0:
						user = user[0]

						userProfil = self.get_profil_by_id(user[1])

						if userProfil != False:
							if user[2] == "admin":
								user = Administrator(user[0], userProfil, user[3], user[4], user[5], user[6])
							elif user[3] == "inhabitant":
								user = Inhabitant(user[0], userProfil, user[2], user[4], user[5], user[6])
							elif user[3] == 'guest':
								user = Guest(user[0], userProfil, user[2], user[4], user[5], user[6])
						else:
							user = False
					else:
						user = False
				else:
					user = False
			else:
				user = False
		else:
			user = False

		#check user conformity
		if user != False:
			if isinstance(user, User):
				succes = True
			else:
				succes = False
		else:
			succes = False

		#return
		if succes:
			return user
		else:
			return False


	def get_room_by_id(self, roomId):
		room = succes = False

		#connect to database
		if isinstance(roomId, int):
			if self.connect():
				request = "SELECT * FROM Rooms WHERE id = {}".format(roomId)
				
				try:
					#ask to database to select the user with an predefined id
					self.db_cursor.execute(request)
					room = self.db_cursor.fetchall()
				except:
					room = False
				finally:
					#database disconnection
					self.disconnect()

				if room != False:
					#transform room in room instance classe
					if len(room) > 0:
						try:
							if room[2] == 'bathroom':
								room = Bathroom(room[0], room[1])
							elif room[2] == 'bedroom':
								room = Bedroom(room[0], room[1])
							elif room[2] == 'corridor':
								room = Corridor(room[0], room[1])
							elif room[2] == 'kitchen':
								room = Kitchen(room[0], room[1])
							elif room[2] == 'livingroom':
								room = Livingroom(room[0], room[1])
							elif room[2] == 'outside':
								room = Outside(room[0], room[1])
							else:
								room = Room(room[0], room[1], room[2])

							room.events = self.get_room_events(room.id)
			
						except:
							pass
					else:
						room = False
				else:
					room = False
			else:
				room = False
		else:
			room = False

		
		if isinstance(room, Room):
			succes = True
		else:
			succes = False

		if succes:
			return room
		else:
			return False


	def get_event_by_id(self, eventId):
		event = succes = False

		#connect to database
		if isinstance(eventId, int):
			if self.connect():
				request = "SELECT * FROM Events WHERE id = {}".format(eventId)
				
				try:
					#ask to database to select the user with an predefined id
					self.db_cursor.execute(request)
					event = self.db_cursor.fetchall()
				except:
					event = False
				finally:
					#database disconnection
					self.disconnect()

				if event != False:
					#transform event in event instance classe
					if len(event) > 0:
						try:
							event = Event(event[0], event[1], event[2], event[3])
						except:
							pass
					else:
						event = False
				else:
					event = False
			else:
				event = False
		else:
			event = False

		
		if isinstance(event, Event):
			succes = True
		else:
			succes = False

		if succes:
			return event
		else:
			return False


	def get_room_events(self, roomId):
		eventsList = tmpEventsList = succes = False

		#connect to database
		if isinstance(roomId, int):
			if self.connect():
				request = "SELECT * FROM Events WHERE fk_room_id = {}".format(roomId)
				
				try:
					#get all event in database
					self.db_cursor.execute(request)
					tmpEventsList = self.db_cursor.fetchall()
				except:
					tmpEventsList = False
				finally:
					#database disconnection
					self.disconnect()
			else:
				tmpEventsList = False

			if tmpEventsList != False:
				eventsList = []

				if len(tmpEventsList) > 0:
					for event in tmpEventsList:
						try:
							eventsList.append(Event(event[0], event[1], event[2], event[3]))			
						except:
							pass
				else:
					eventsList = []
			else:
				succes = False
		else:
			succes = False

		if succes:
			return eventsList
		else:
			return False


	#add method
	def add_user(self, firstName, lastName, gender, dateOfBirth, grade, role, identifiant, password, mail):
		"""
            method used for create an user in database 

            functioning:
                1.check parametters conformity
				2.connect to the database
				3.add the profil of the user
				4.add the user
				5.commit change
				6.database disconnection
				7.check if the user is present in the users list
				8.return
                
            return:
				if succes return the user id
				else return false
                
        """

		succes = profilId = userId = requestExecuted = False

		#check parametters conformity
		if isinstance(firstName, str) \
			and isinstance(lastName, str) \
			and (gender == "f" or gender == "m")\
			and isinstance(dateOfBirth, str)\
			and isinstance(grade, str)\
			and (grade == "user" or grade == "admin")\
			and isinstance(role, str)\
			and (role == "guest" or role == "inhabitant")\
			and isinstance(identifiant, str)\
			and isinstance(password, str)\
			and isinstance(mail, str):

			#add the profil of the user
			profilId = self.add_profil(firstName, lastName, gender, dateOfBirth)

			if profilId != False:
				#connect to the database
				if self.connect():
					request = "INSERT INTO Users(fk_profil_id, grade, role, identifiant, password, mail) VALUES\
						({}, '{}', '{}', '{}', '{}')".format(profilId, grade, role, identifiant, password, mail)

					try:
						#add the user
						self.db_cursor.execute(request)
						requestExecuted = True
					except:
						requestExecuted = False

					if requestExecuted:
						#commit change
						if self.commit_change():
							try:
								userId = self.db_cursor.lastrowid
							except:
								userId = False
							finally:
								#database disconnection
								self.disconnect()
						else:
							userId = False
							self.disconnect()
					else:
						userId = False
						self.disconnect()
				else:
					userId = False
			else:
				userId = False
		else:
			userId = profil = False

		#check if the user is present in the users list
		if profilId != False and userId != False:
			for user in self.get_users_list():
				if user.id == userId and user.profil.id == profilId:
					succes = True
				else:
					succes = False

				if succes:
					break
		else:
			succes = False

		#return
		if succes:
			return userId
		else:
			return False


	def add_profil(self, firstName, lastName, gender, dateOfBirth):
		"""
    		method called for adding an profil
    		functionning:
				1.check parametters conformity
				2.connect to the database
				3.add profil in database
				4.commit change
				5.get id of the new profil
				6.diconnection of the database
				7.check if profil is in profils list
				8.return

    		return:
    			if succes return profil id
				else return false
    	"""

		succes = profilId = requestExecuted = False

		#check parametters conformity
		if isinstance(firstName, str) \
			and isinstance(lastName, str) \
			and (gender == "f" or gender == "m")\
			and isinstance(dateOfBirth, str):

			#connect to the database
			if self.connect():
				request = "INSERT INTO Profils(first_name, last_name, gender, date_of_birth) VALUES\
				('{}', '{}', '{}', '{}')".format(firstName, lastName, gender, dateOfBirth)

				try:
					#add profil in database
					self.db_cursor.execute(request)
					requestExecuted = True
				except:
					requestExecuted = False

				if requestExecuted:
					#commit change
					if self.commit_change():
						try:
							#get id of the new profil
							profilId = self.db_cursor.lastrowid
							#diconnection of the database
						except:
							profilId = False
						finally:
							self.disconnect()
					else:
						profilId = False
						self.disconnect()	
				else:
					profilId = False
					self.disconnect()
			else:
				profilId = False
		else:
			profilId = False

		if profilId != False:
			#check if profil is in profils list
			for profil in self.get_profils_list():
				if profil.id == profilId \
					and profil.firstName == firstName \
					and profil.lastName == lastName \
					and profil.gender == gender \
					and profil.dateOfBirth == dateOfBirth:

					succes = True
				else:
					succes = False

				if succes:
					break
		else:
			succes = False

		#return
		if succes:
			return profilId
		else:
			return False


	def add_room(self, roomName, roomType):
		succes = roomId = requestExecuted = False

		#check parametters conformity
		if isinstance(roomName, str) and isinstance(roomType, str):
			#connect to the database
			if self.connect():
				request = "INSERT INTO Rooms(name, type) VALUES ('{}', '{}')".format(roomName, roomType)

				try:
					#add room in database
					self.db_cursor.execute(request)
					requestExecuted = True
				except:
					requestExecuted = False

				if requestExecuted:
					#commit change
					if self.commit_change():
						try:
							#get id of the new profil
							profilId = self.db_cursor.lastrowid
							#diconnection of the database
						except:
							roomId = False
						finally:
							self.disconnect()
					else:
						profilId = False
						self.disconnect()	
				else:
					profilId = False
					self.disconnect()
			else:
				roomId = False
		else:
			roomId = False

		if roomId != False:
			for room in self.get_rooms_list():
				if room.id == roomId:
					succes = True
					break
				else:
					succes = False
		else:
			succes = False

		if succes:
			return roomId
		else:
			return False


	def add_event(self, eventType, eventDatetime, eventLocation):
		succes = eventId = requestExecuted = False

		#check parametters conformity
		if isinstance(eventType, str) and isinstance(eventDatetime, str) and isinstance(eventLocation, int):
			#connect to the database
			if self.connect():
				request = "INSERT INTO Events(type, datetime, fk_room_id) VALUES ('{}', '{}', {})".format(eventType, eventDatetime, eventLocation)

				try:
					#add event in database
					self.db_cursor.execute(request)
					requestExecuted = True
				except:
					requestExecuted = False

				if requestExecuted:
					#commit change
					if self.commit_change():
						try:
							#get id of the new profil
							eventId = self.db_cursor.lastrowid
							#diconnection of the database
						except:
							eventId = False
						finally:
							self.disconnect()
					else:
						eventId = False
						self.disconnect()	
				else:
					eventId = False
					self.disconnect()
			else:
				eventId = False
		else:
			eventId = False

		if eventId != False:
			for event in self.get_events_list():
				if event.id == eventId:
					succes = True
					break
				else:
					succes = False
		else:
			succes = False

		if succes:
			return eventId
		else:
			return False



	#del methods
	#a ajouter au test
	def del_user(self, userId):
		succes = user = False

		if isinstance(userId, int):
			user = self.get_user_by_id(userId)

			if user != False:
				if self.del_profil(user.profil.id):
					if self.connect():
						request = "DELETE FROM Users WHERE id = {}".format(userId)
						try:
							self.db_cursor.execute(request)
							if self.commit_change():
								succes = True
							else:
								succes = False
						except:
							succes = False
						finally:
							self.disconnect()
					else:
						succes = False
				else:
					succes = False
			else:
				succes = False
		else:
			succes = False

		return succes


	#a ajouter au test
	def del_profil(self, profilId):
		succes = False

		if isinstance(profilId, int):
			if self.connect():
				request = "DELETE FROM Profils WHERE id = {}".format(profilId)
				try:
					self.db_cursor.execute(request)
					if self.commit_change():
						succes = True
					else:
						succes = False
				except:
					succes = False
				finally:
					self.disconnect()
			else:
				succes = False
		else:
			succes = False

		return succes


	def del_room(self, roomId):
		succes = eventsDeleted = False

		if isinstance(roomId, int):
			for event in self.get_events_list():
				if event.location == roomId:
					self.del_event(event.id)

			for event in self.get_events_list():
				if event.location == roomId:
					eventsDeleted = False
					break
				else:
					eventsDeleted = True

			if eventsDeleted:
				if self.connect():
					request = "DELETE FROM Rooms WHERE id = {}".format(roomId)
					try:
						self.db_cursor.execute(request)
						if self.commit_change():
							succes = True
						else:
							succes = False
					except:
						succes = False
					finally:
						self.disconnect()
				else:
					succes = False
			else:
				succes = False
		else:
			succes = False

		return succes


	def del_event(self, eventId):
		succes = False

		if isinstance(eventId, int):
			if self.connect():
				request = "DELETE FROM Events WHERE id = {}".format(eventId)
				try:
					self.db_cursor.execute(request)
					if self.commit_change():
						succes = True
					else:
						succes = False
				except:
					succes = False
				finally:
					self.disconnect()
			else:
				succes = False
		else:
			succes = False

		return succes



	#set methods
	def set_profil_first_name(self, profilId, newFirstName):
		succes = False

		if isinstance(profilId, int) and isinstance(newFirstName, str):
			if self.connect():
				request = """UPDATE Profils SET first_name = '{}' where id = {}""".format(newFirstName, profilId)

				try:
					self.db_cursor.execute(request)
					if self.commit_change():
						succes = True
					else:
						succes = False
				except:
					succes = False
				finally:
					self.disconnect()
			else:
				succes = False
		else:
			succes = False

		return succes


	def set_profil_last_name(self, profilId, newLastName):
		succes = False

		if isinstance(profilId, int) and isinstance(newLastName, str):
			if self.connect():
				request = """UPDATE Profils SET last_name = '{}' where id = {}""".format(newLastName, profilId)

				try:
					self.db_cursor.execute(request)
					if self.commit_change():
						succes = True
					else:
						succes = False
				except:
					succes = False
				finally:
					self.disconnect()
			else:
				succes = False
		else:
			succes = False

		return succes


	def set_profil_gender(self, profilId, newGender):
		succes = False

		if isinstance(profilId, int) and isinstance(newGender, str):
			if newGender == "m" or newGender == "f":
				if self.connect():
					request = """UPDATE Profils SET gender = '{}' where id = {}""".format(newGender, profilId)

					try:
						self.db_cursor.execute(request)
						if self.commit_change():
							succes = True
						else:
							succes = False
					except:
						succes = False
					finally:
						self.disconnect()
				else:
					succes = False
			else:
				succes = False
		else:
			succes = False

		return succes


	def set_profil_date_of_birth(self, profilId, newDateOfBirth):
		succes = False

		if isinstance(profilId, int) and isinstance(newDateOfBirth, str):
			if self.connect():
				request = """UPDATE Profils SET date_of_birth = '{}' where id = {}""".format(newDateOfBirth, profilId)

				try:
					self.db_cursor.execute(request)
					if self.commit_change():
						succes = True
					else:
						succes = False
				except:
					succes = False
				finally:
					self.disconnect()
			else:
				succes = False
		else:
			succes = False

		return succes


	def set_user_first_name(self, userId, newFirstName):
		succes = user = False

		if isinstance(userId, int) and isinstance(newFirstName, str):
			user = self.get_user_by_id(userId)

			if user != False:
				if self.set_profil_first_name(user, newFirstName):
					succes = True
				else:
					succes = False
			else:
				succes = False
		else:
			succes = False

		return succes


	def set_user_last_name(self, userId, newLastName):
		succes = user = False

		if isinstance(userId, int) and isinstance(newLastName, str):
			user = self.get_user_by_id(userId)

			if user != False:
				if self.set_profil_last_name(user.profil.id, newLastName):
					succes = True
				else:
					succes = False
			else:
				succes = False
		else:
			succes = False

		return succes


	def set_user_gender(self, userId, newGender):
		succes = user = False

		if isinstance(userId, int) and isinstance(newGender, str):
			if newGender == "f" or newGender == "m":
				user = self.get_user_by_id(userId)

				if user != False:
					if self.set_profil_gender(user.profil.id, newGender):
						succes = True
					else:
						succes = False
				else:
					succes = False
			else:
				succes = False
		else:
			succes = False

		return succes


	def set_user_date_of_birth(self, userId, newDateOfBirth):
		succes = user = False

		if isinstance(userId, int) and isinstance(newDateOfBirth, str):
			user = self.get_user_by_id(userId)
			if user != False:
				if self.set_profil_date_of_birth(user.profil.id, newDateOfBirth):
					succes = True
				else:
					succes = False
			else:
				succes = False
		else:
			succes = False

		return succes


	def set_user_grade(self, userId, newGrade):
		succes = False

		if isinstance(userId, int) and isinstance(newGrade, str):
			if newGrade == "user" or newGrade == "admin":
				if self.connect():
					request = """UPDATE Users SET grade = '{}' where id = {}""".format(userId, newGrade)

					try:
						self.db_cursor.execute(request)
						if self.commit_change():
							succes = True
						else:
							succes = False
					except:
						succes = False
					finally:
						self.disconnect()
				else:
					succes = False
			else:
				succes = False
		else:
			succes = False

		return succes


	def set_user_role(self, userId, newRole):
		succes = False

		if isinstance(userId, int) and isinstance(newRole, str):
			if newRole == "guest" or newRole == "inhabitant":
				if self.connect():
					request = """UPDATE Users SET role = '{}' where id = {}""".format(userId, newRole)

					try:
						self.db_cursor.execute(request)
						if self.commit_change():
							succes = True
						else:
							succes = False
					except:
						succes = False
					finally:
						self.disconnect()
				else:
					succes = False
			else:
				succes = False
		else:
			succes = False

		return succes


	def set_user_identifiant(self, userId, newIdentifiant):
		succes = False

		if isinstance(userId, int) and isinstance(newIdentifiant, str):
			if self.connect():
				request = """UPDATE Users SET identifiant = '{}' where id = {}""".format(userId, newIdentifiant)

				try:
					self.db_cursor.execute(request)
					if self.commit_change():
						succes = True
					else:
						succes = False
				except:
					succes = False
				finally:
					self.disconnect()
			else:
				succes = False
		else:
			succes = False

		return succes


	def set_user_password(self, userId, newPassword):
		succes = False

		if isinstance(userId, int) and isinstance(newPassword, str):
			if self.connect():
				request = """UPDATE Users SET password = '{}' where id = {}""".format(userId, newPassword)

				try:
					self.db_cursor.execute(request)
					if self.commit_change():
						succes = True
					else:
						succes = False
				except:
					succes = False
				finally:
					self.disconnect()
			else:
				succes = False
		else:
			succes = False

		return succes


	def set_user_mail(self, userId, newMail):
		succes = False

		if isinstance(userId, int) and isinstance(newMail, str):
			if self.connect():
				request = """UPDATE Users SET mail = '{}' where id = {}""".format(userId, newMail)

				try:
					self.db_cursor.execute(request)
					if self.commit_change():
						succes = True
					else:
						succes = False
				except:
					succes = False
				finally:
					self.disconnect()
			else:
				succes = False
		else:
			succes = False

		return succes


	def set_room_name(self, roomId, newName):
		succes = False

		if isinstance(roomId, int) and isinstance(newName, str):
			if self.connect():
				request = """UPDATE Rooms SET name = '{}' where id = {}""".format(roomId, newName)

				try:
					self.db_cursor.execute(request)
					if self.commit_change():
						succes = True
					else:
						succes = False
				except:
					succes = False
				finally:
					self.disconnect()
			else:
				succes = False
		else:
			succes = False

		return succes


	def set_room_type(self, roomId, newType):
		succes = False

		if isinstance(roomId, int) and isinstance(newType, str):
			if self.connect():
				request = """UPDATE Rooms SET type = '{}' where id = {}""".format(roomId, newType)

				try:
					self.db_cursor.execute(request)
					if self.commit_change():
						succes = True
					else:
						succes = False
				except:
					succes = False
				finally:
					self.disconnect()
			else:
				succes = False
		else:
			succes = False

		return succes
	


	#checking methods
	def check_config_file_existence(self):
		"""
			Method used for checking the existence of the config file.

			functioning:
				1) the method try to open the databaseConfigFile
				2) if opening succes the method return True else the method return False

			return:
				succes (True/False)
		"""

		succes = False

		try:
			with open(self.configFilePath):
				pass
			succes = True
		except:
			succes = False

		return succes


	def check_database_connection(self):
		"""
			Method used for checking the connection with the database.

			functioning:
				1) the method try to connect to the database
				2) if connection succes the method return True else the method return False

			return:
				succes (True/False)
		"""

		succes = False

		if self.connect() is True:
			if self.disconnect():
				succes = True
			else:
				succes = False
		else:
			succes = False

		return succes