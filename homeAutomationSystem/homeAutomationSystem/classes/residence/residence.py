import sys
import os
import json

sys.path.append("..")

from homeAutomationSystem.homeDatabase.classes.homeDatabase import *


class Residence:
    def __init__(self, databaseConfigFilePath):
        self.homeDatabase = HomeDatabase(databaseConfigFilePath)

    
    
    ###PROPERTYS###
    """HOME DATABASE INFORMATION"""
    @property
    def homeDatabaseName(self):
        return self.homeDatabase.databaseName


    @property
    def homeDatabaseUsername(self):
        return self.homeDatabase.username


    @property
    def homeDatabasePassword(self):
        return self.homeDatabase.password


    """USERS"""
    @property
    def usersList(self):
        usersList = []

        for user in self.homeDatabase.get_users_list():
            usersList.append(user)

        return usersList


    @property
    def profilsList(self):
        profilsList = []

        for profil in self.homeDatabase.get_profils_list():
            profilsList.append(profil)

        return profilsList


    @property
    def inhabitantsList(self):
        inhabitantsList = []

        for inhabitant in self.homeDatabase.self.homeDatabase.self.homeDatabase.get_inhabitants_list():
            inhabitantsList.append(inhabitant)

        return inhabitantsList


    @property
    def guestsList(self):
        guestList = []

        for guest in self.homeDatabase.self.homeDatabase.self.homeDatabase.get_guests_list():
            guestList.append(guest)

        return guestList


    @property
    def administratorsList(self):
        adminList = []

        for admin in self.homeDatabase.self.homeDatabase.self.homeDatabase.get_administrator_list():
            adminList.append(admin)

        return adminList


    """ROOMS"""
    @property
    def roomsList(self):
        roomList = []

        for room in self.homeDatabase.self.homeDatabase.get_rooms_list():
            roomList.append(room)

        return roomList


    """EVENTS"""
    @property
    def eventsList(self):
        eventList = []

        for event in self.homeDatabase.get_events_list():
            eventList.append(event)

        return eventList



    ###METHODS###
    """GET METHODS"""
    def get_profil(self, profilId):
        return self.homeDatabase.get_profil_by_id(profilId)


    def get_user(self, userId):
        return self.homeDatabase.get_user_by_id(userId)


    def get_room(self, roomId):
        room = roomId = False

        try:
            roomId = data["roomId"]
        except:
            roomId = False

        room = self.homeDatabase.get_room_by_id(roomId)

        if room != False:
            moduleList = []
            for module in self.homeAutomationServeur.moduleList:
                if module.location == room.id:
                    moduleList.append(module)

            room.content = moduleList
        else:
            room = False

        return room


    def get_event(self, eventId):
        return self.homeDatabase.get_event_by_id(eventId)



    """ADD REQUEST"""
    def add_user(self, userFirstName, userLastName, userGender, userDateOfBirth, userGrade, userRole, userIdentifiant, userPassword, userMail):
        
        userId = self.homeDatabase.add_user(userFirstName, userLastName, 
        userGender,userDateOfBirth, userGrade, userRole, 
        userIdentifiant, userPassword, userMail)

        return userId


    def add_room(self, roomName, roomType):
        roomId = self.homeDatabase.add_room(roomName, roomType)

        return roomId


    def add_event(self, eventType, eventDatetime, eventLocation):
        eventId = self.homeDatabase.add_event(eventType, eventDatetime, eventLocation)

        return eventId



    """DEL METHODS"""
    def del_user(self, userId):
        return self.homeDatabase.del_user(userId)


    def del_room(self, roomId):
        return self.homeDatabase.del_room(roomId)


    def del_event(self, eventId):
        return self.homeDatabase.del_event(eventId)



    """SET METHODS"""
    def set_user_first_name(self, userId, newFirstName):
        return self.homeDatabase.set_user_first_name(userId, newFirstName)
    

    def set_user_last_name(self, userId, newLastName):
        return self.homeDatabase.set_user_last_name(userId, newLastName)


    def set_user_gender(self, userId, newGender):
        return self.homeDatabase.set_user_gender(userId, newGender)


    def set_user_date_of_birth(self, userId, newDateOfBirth):
        return self.homeDatabase.set_user_date_of_birth(userId, newDateOfBirth)


    def set_user_grade(self, userId, newGrade):
        return self.homeDatabase.set_user_grade(userId, newGrade)


    def set_user_role(self, userId, newRole):
        return self.homeDatabase.set_user_role(userId, newRole)


    def set_user_identifiant(self, userId, newIdentifiant):
        return self.homeDatabase.set_user_identifiant(userId, newIdentifiant)


    def set_user_password(self, userId, newPassword):
        return self.homeDatabase.set_user_password(userId, newPassword)


    def set_user_mail(self, userId, newMail):
        return self.homeDatabase.set_user_password(userId, newMail)


    def set_room_name(self, roomId, newName):
        return self.homeDatabase.set_room_name(roomId, newName)


    def set_room_type(self, roomId, newType):
        return self.homeDatabase.set_room_type(roomId, newType)



    """CHECK Methods"""
    def check_homeDatabase_connection(self):
        return self.homeDatabase.check_database_connection()


    """serialize method"""
    def serialize(self):
        pass