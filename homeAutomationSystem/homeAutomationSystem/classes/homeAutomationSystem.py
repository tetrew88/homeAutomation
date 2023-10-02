from .residence.residence import *
from .homeAutomationServer.homeAutomationEngine import *


class HomeAutomationSystem:
    def __init__(self, scriptPath, homeAutomationServer = False):
        self.scriptPath = scriptPath
        self.configFilePath = scriptPath + '/configs/homeAutomationSystemConfig.json'        
        self.residence = Residence(scriptPath + '/homeDatabase/configs/databaseConfig.json')
        self.running = False

        self.homeAutomationEngine = HomeAutomationEngine(homeAutomationServer)



    ###PROPERTYS###
    """HOME AUTOMATION ENGINE INFORMATION"""
    @property
    def homeAutomationEngineIsRunning(self):
        return self.homeAutomationEngine.get_home_automation_engine_isRunning()


    @property
    def zWaveNetworkStatus(self):
        return self.homeAutomationEngine.get_zWave_network_status()

    
    @property
    def zWaveNetworkIsRunning(self):
        return self.homeAutomationEngine.get_zWave_network_isRunning()

    @property
    def zWaveHomeId(self):
        return self.homeAutomationEngine.get_zWave_home_id()

    @property
    def zWaveNetworkState(self):
        return self.homeAutomationEngine.get_zWave_network_state()


    @property
    def zWaveNetworkIsReady(self):
        return self.homeAutomationEngine.get_zWave_network_isReady()


    @property
    def zWaveNetworkControllerPath(self):
        return self.homeAutomationEngine.get_zWave_network_controller_path()

    @property
    def zWaveConfigFolderPath(self):
        return self.homeAutomationEngine.get_zWave_config_folder_path()


    @property
    def modulesList(self):
        return self.homeAutomationEngine.get_modules_list()




    """HOME DATABASE INFORMATIONS"""
    @property
    def homeDatabaseName(self):
        return self.residence.homeDatabaseName


    @property
    def homeDatabaseUsername(self):
        return self.residence.homeDatabaseUsername


    @property
    def homeDatabasePassword(self):
        return self.residence.homeDatabasePassword


    @property
    def usersList(self):
        return self.residence.usersList


    @property
    def profilsList(self):
        return self.residence.profilsList


    @property
    def inhabitantsList(self):
        return self.residence.inhabitantsList


    @property
    def guestsList(self):
        return self.residence.guestsList


    @property
    def administratorsList(self):
        return self.residence.administratorsList


    @property
    def roomsList(self):
        roomsList = self.residence.roomsList

        for room in roomsList:
            room.content = []

            for module in self.modulesList:
                if module.location == room.id:
                    room.content.append(module)
                else:
                    pass

        return roomsList


    @property
    def eventsList(self):
        return self.residence.eventsList


    
    ###METHODS###
    """ASK METHODS"""
    def ask_home_automation_engine_information(self):
        return self.homeAutomationEngine.ask_home_automation_engine_information()



    """GET METHODS"""
    def get_module(self, moduleId):
        return self.homeAutomationEngine.get_module(moduleId)


    def get_profil(self, profilId):
        return self.residence.get_profil(profilId)


    def get_user(self, userId):
        return self.residence.get_user(userId)


    def get_room(self, roomId):
        return self.residence.get_room(roomId)

    
    def get_event(self, eventId):
        return self.residence.get_event(eventId)



    """ADD METHODS"""
    def add_zWave_module(self):
        return self.homeAutomationEngine.add_zWave_module()

    
    def add_user(self, userFirstName, userLastName, userGender, userDateOfBirth, userGrade, userRole, userIdentifiant, userPassword, userMail):
       return self.residence.add_user(userFirstName, userLastName, userGender, userDateOfBirth, userGrade, userRole, userIdentifiant, userPassword, userMail)
       

    def add_room(self, roomName, roomType):
        return self.residence.add_room(roomName, roomType)


    def add_event(self, eventType, eventDatetime, eventLocation):
        return self.residence.add_event(eventType, eventDatetime, eventLocation)



    """DEL METHODS"""
    def del_zWave_module(self):
        return self.homeAutomationEngine.del_zWave_module()


    def del_user(self, userId):
        return self.residence.del_user(userId)


    def del_room(self, roomId):
        return self.residence.del_room(roomId)


    def del_event(self, eventId):
        return self.residence.del_event(eventId)



    """SET METHODS"""
    def set_module_name(self, moduleId, newName):
        return self.homeAutomationEngine.set_module_name(moduleId, newName)


    def set_module_location(self, moduleId, newLocation):
        return self.homeAutomationEngine.set_module_location(moduleId, newLocation)


    def set_module_value(self, moduleId, valueId, newData):
        return self.homeAutomationEngine.set_module_value(moduleId, valueId, newData)


    def set_light_controller_level(self, moduleId, newLevel):
        return self.homeAutomationEngine.set_light_controller_level(moduleId, newLevel)


    def set_light_controller_color_by_label(self, moduleId, newColorLabel):
        return self.homeAutomationEngine.set_light_controller_color_by_label(moduleId, newColorLabel)


    def set_light_controller_color_by_rgbw(self, moduleId, newRgbwValue):
        return self.homeAutomationEngine.set_light_controller_color_by_rgbw(moduleId, newRgbwValue)


    def set_user_first_name(self, userId, newFirstName):
        return self.residence.set_user_first_name(userId, newFirstName)


    def set_user_last_name(self, userId, newLastName):
        return self.residence.set_user_last_name(userId, newLastName)


    def set_user_gender(self, userId, newGender):
        return self.residence.set_user_gender(userId, newGender)


    def set_user_date_of_birth(self, userId, newDateOfBirth):
        return self.residence.set_user_date_of_birth(userId, newDateOfBirth)


    def set_user_grade(self, userId, newGrade):
        return self.residence.set_user_grade(userId, newGrade)

    
    def set_user_role(self, userId, newRole):
        return self.residence.set_user_role(userId, newRole)


    def set_user_identifiant(self, userId, newIdentifiant):
        return self.residence.set_user_identifiant(userId, newIdentifiant)


    def set_user_password(self, userId, newPassword):
        return self.residence.set_user_password(userId, newPassword)

    
    def set_user_mail(self, userId, newMail):
        return self.residence.set_user_password(userId, newMail)


    def set_room_name(self, roomId, newName):
        return self.residence.set_room_name(roomId, newName)


    def set_room_type(self, roomId, newType):
        return self.residence.set_room_type(roomId, newType)



    """SWITCH METHODS"""
    def switch_light_controller_on(self, moduleId):
        return self.homeAutomationEngine.switch_light_controller_on(moduleId)


    def switch_light_controller_off(self, moduleId):
        return self.homeAutomationEngine.switch_light_controller_off(moduleId)


    def switch_relay_on(self, moduleId):
        return self.homeAutomationEngine.switch_relay_on(moduleId)


    def switch_relay_off(self, moduleId):
        return self.homeAutomationEngine.switch_relay_off(moduleId)



    """HEAL METHODS"""
    def heal_zWave_network(self):
        return self.homeAutomationEngine.heal_zWave_network()


    def heal_zWave_module(self, moduleId):
        return self.homeAutomationEngine.heal_zWave_module(moduleId)



    """DESTROY METHODS"""
    def destroy_zWave_network(self):
        return self.homeAutomationEngine.destroy_zWave_network()



    """UPDATE METHODS"""
    def update_zWave_module_return_route(self, moduleId):
        return self.homeAutomationEngine.update_zWave_module_return_route(moduleId)


    def update_zWave_module_neighbors(self, moduleId):
        return self.homeAutomationEngine.update_zWave_module_neighbors(moduleId)


    def update_zWave_module_network(self, moduleId):
        return self.homeAutomationEngine.update_zWave_module_network(moduleId)



    """REFRESH METHODS"""
    def refresh_zWave_module_informations(self, moduleId):
        return self.homeAutomationEngine.refresh_zWave_module_informations(moduleId)


    def refresh_zWave_module_value(self, moduleId, valueId):
        return self.homeAutomationEngine.refresh_zWave_module_value(moduleId, valueId)


    def refresh_zWave_module_values(self, moduleId):
        return self.homeAutomationEngine.refresh_zWave_module_values(moduleId)



    """RESET METHODS"""
    def soft_reset_zWave_network(self):
        return self.homeAutomationEngine.soft_reset_zWave_network()


    def hard_reset_zWave_network(self):
        return self.homeAutomationEngine.hard_reset_zWave_network()



    """ACTIVATION METHODS"""
    def activate_zWave_network(self):
        return self.homeAutomationEngine.activate_zWave_network()



    """DEACTIVATION METHODS"""
    def deactivate_zWave_network(self):
        return self.homeAutomationEngine.deactivate_zWave_network()



    """START METHODS"""
    def start(self):
        succes = False
        
        self.running = True
        succes = True

        return succes


    def start_zWave_network(self):
        return self.homeAutomationEngine.start_zWave_network()


    def start_home_automation_engine(self):
        return self.homeAutomationEngine.start_home_automation_engine()



    """STOP METHODS"""
    def stop(self):
        self.running = False

        return True


    def stop_zWave_network(self):
        return self.homeAutomationEngine.stop_zWave_network()


    def stop_home_automation_engine(self):
        return self.homeAutomationEngine.stop_home_automation_engine()



    """RESTART METHODS"""
    def restart(self):
        succes = True

        if self.stop():
            if self.start():
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes

        
    def restart_zWave_network(self):
        return self.homeAutomationEngine.restart_zWave_network()


    def restart_home_automation_engine(self):
        return self.homeAutomationEngine.restart_home_automation_engine()



    """UPDATED METHODS"""
    def home_automation_engine_updated(self, newHomeAutomationEngineInformation):
        return self.homeAutomationEngine.home_automation_engine_updated(newHomeAutomationEngineInformation)


    def zWave_network_updated(self, newZwaveNetworkInformations):
        return self.homeAutomationEngine.zWave_network_updated(newZwaveNetworkInformations)


    def modules_list_updated(self, modulesListData):
        return self.homeAutomationEngine.modules_list_updated(modulesListData)


    def module_updated(self, moduleData):
        return self.homeAutomationEngine.module_updated(self, moduleData)



    """CHECK Methods"""
    def check_homeDatabase_connection(self):
        return self.residence.check_homeDatabase_connection()