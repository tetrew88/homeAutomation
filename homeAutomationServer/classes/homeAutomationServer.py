import eventlet

import socketio
import sys
import os

import threading
import time

sys.path.append("..")

import json

from homeAutomationServer.homeAutomationEngine.classes.homeAutomationEngine import *

socketIoServer = socketio.Server(cors_allowed_origins="*", ping_timeout=60, logger=True, engineio_logger=True)
app = socketio.WSGIApp(socketIoServer, object)


class HomeAutomationServer(socketio.Namespace):
    """
        class representing the home automation server:
            property:

            methods:

            server event:
    """

    homeAutomationEngine = False
    running = False


    def __init__(self, scriptPath):
        self.scriptPath = scriptPath
        self.configFilePath = scriptPath + "/configs/homeAutomationServerConfig.json"

        self.load_home_automation_engine(self)

        socketio.Namespace.__init__(self, '/HomeAutomationServer')



    @staticmethod
    def load_home_automation_engine(self):
        HomeAutomationServer.homeAutomationEngine = HomeAutomationEngine(self.scriptPath + '/homeAutomationEngine', socketIoServer)


    @property
    def serverConfigured(self):
        serverConfigured = False

        try:
            with open(self.configFilePath) as configurationFile:
                data = json.load(configurationFile)
                serverConfigured = bool(data["serverConfigured"])
        except:
            serverConfigured = False

        return serverConfigured


    @property
    def engineConfigured(self):
        engineConfigured = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine):
            engineConfigured = self.homeAutomationEngine.engineConfigured
        else:
            engineConfigured = False

        return engineConfigured


    @property
    def zWaveNetworkStatus(self):
        zWaveNetworkStatus = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine):
            zWaveNetworkStatus = self.homeAutomationEngine.zWaveNetworkStatus
        else:
            zWaveNetworkStatus = False

        return zWaveNetworkStatus


    @property
    def zWaveNetworkConfigured(self):
        zWaveNetworkConfigured = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine):
            zWaveNetworkConfigured = self.homeAutomationEngine.zWaveNetworkConfigured
        else:
            zWaveNetworkConfigured = False

        return zWaveNetworkConfigured


    @property
    def zWaveHomeId(self):
        zWaveHomeId = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine):
            zWaveHomeId = self.homeAutomationEngine.zWaveHomeId
        else:
            zWaveHomeId = False

        return zWaveHomeId


    @property
    def zWaveNetworkState(self):
        zWaveNetworkState = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine):
            zWaveNetworkState = self.homeAutomationEngine.zWaveNetworkState
        else:
            zWaveNetworkState = False

        return zWaveNetworkState


    @property
    def zwaveNetworkIsReady(self):
        zwaveNetworkIsReady = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine):
            zwaveNetworkIsReady = self.homeAutomationEngine.zwaveNetworkIsReady
        else:
            zwaveNetworkIsReady = False

        return zwaveNetworkIsReady


    @property
    def zWaveNetworkControllerPath(self):
        zWaveNetworkControllerPath = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine):
            zWaveNetworkControllerPath = self.homeAutomationEngine.zWaveNetworkControllerPath
        else:
            zWaveNetworkControllerPath = False

        return zWaveNetworkControllerPath


    @property
    def zwaveConfigFolderPath(self):
        zwaveConfigFolderPath = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine):
            zwaveConfigFolderPath = self.homeAutomationEngine.zwaveConfigFolderPath
        else:
            zwaveConfigFolderPath = False

        return zwaveConfigFolderPath


    @property
    def zWaveNetworkIsRunning(self):
        zWaveNetworkIsRunning = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine):
            zWaveNetworkIsRunning = self.homeAutomationEngine.zWaveNetworkIsRunning
        else:
            zWaveNetworkIsRunning = False

        return zWaveNetworkIsRunning


    @property
    def zWaveModulesList(self):
        zWaveModulesList = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine):
            zWaveModulesList = self.homeAutomationEngine.zWaveModulesList
        else:
            zWaveModulesList = False

        return zWaveModulesList


    @property
    def zWaveEventsList(self):
        zWaveEventsList = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine):
            zWaveEventsList = self.homeAutomationEngine.zWaveEventsList
        else:
            zWaveEventsList = False

        return zWaveEventsList


    @property
    def modulesList(self):
        modulesList = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine):
            modulesList = self.homeAutomationEngine.modulesList
        else:
            modulesList = False

        return modulesList


    @property
    def eventsList(self):
        eventsList = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine):
            eventsList = self.homeAutomationEngine.eventsList
        else:
            eventsList = False

        return eventsList
        


    ###BASE METHODS###
    def start(self):
        succes = False

        if self.serverConfigured == True:
            if self.start_engine():
                succes = True
            else:
                succes = False
                pass
        else:
            succes = False

        if succes:
            self.running = True

        return succes


    def stop(self):
        succes = False

        if self.stop_engine():
            succes = True
        else:
            succes = False

        if succes:
            self.running = False

        return succes


    def restart(self):
        succes = False

        if self.stop():
            if self.start():
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def run(self):
        self.listen_clients()


    def serialize(self):
        data = {}
        zWaveModulesList = zWaveEventsList = []
        modulesList = eventsList = []

        #server informations
        data['serverConfigured'] = self.serverConfigured

        #engine informations
        data['engineConfigured'] = self.engineConfigured
        data['running'] = self.running

        #zWaveNetwork informations
        data['zWaveNetworkStatus'] = self.zWaveNetworkStatus
        data['zWaveNetworkConfigured'] = self.zWaveNetworkConfigured
        data['zWaveHomeId'] = self.zWaveHomeId
        data['zWaveNetworkState'] = self.zWaveNetworkState
        data['zwaveNetworkIsReady'] = self.zwaveNetworkIsReady
        data['zWaveNetworkControllerPath'] = self.zWaveNetworkControllerPath
        data['zwaveConfigFolderPath'] = self.zwaveConfigFolderPath
        data['zWaveNetworkIsRunning'] = self.zWaveNetworkIsRunning

        for module in self.zWaveModulesList:
            zWaveModulesList.append(module.serialize())
        data['zWaveModulesList'] = zWaveModulesList

        for event in self.zWaveEventsList:
            zWaveEventsList.append(event.serialize())
        data['zWaveEventsList'] = zWaveEventsList


        for module in self.modulesList:
            modulesList.append(module.serialize())
        data['modulesList'] = modulesList

        for event in self.eventsList:
            eventsList.append(event.serialize())
        data['eventsList'] = eventsList

        return data


    ###METHODS###
    """START METHODS"""
    def start_engine(self):
        succes = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine): 
            if self.homeAutomationEngine.start():
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def start_zWave_network(self):
        succes = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine):
            if self.homeAutomationEngine.start_zWave_network():
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes



    """STOP METHODS"""
    def stop_engine(self):
        succes = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine):  
            if self.homeAutomationEngine.stop():
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def stop_zWave_network(self):
        succes = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine):  
            if self.homeAutomationEngine.stop_zWave_network():
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes



    """RESTART METHODS"""
    def restart_zWave_network(self):
        succes = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine):  
            if self.homeAutomationEngine.restart_zWave_network():
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes



    """ACTIVATION METHODS"""
    def activate_zWave_network(self):
        succes = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine):  
            if self.homeAutomationEngine.activate_zWave_network():
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes



    """DEACTIVATE METHODS"""
    def deactivate_zWave_network(self):
        succes = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine):  
            if self.homeAutomationEngine.deactivate_zWave_network():
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes



    """GET METHODS"""
    def get_module(self, moduleId):
        succes = module = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine) and isinstance(moduleId, int):  
            module = self.homeAutomationEngine.get_module(moduleId)

            if module != False:
                succes = True
            else:
                succes = False
        else:
            succes = False

        if succes != False:
            return module
        else:
            return False



    """ADD METHODS"""
    def add_zWave_module(self):
        succes = moduleId = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine):  
            moduleId = self.homeAutomationEngine.add_zWave_module()

            if moduleId != False:
                succes = True
            else:
                succes = False
        else:
            succes = False

        if succes != False:
            return moduleId
        else:
            return False



    """DEL METHODS"""
    def del_zWave_module(self, moduleId):
        succes = module = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine) and isinstance(moduleId, int):  
            if self.homeAutomationEngine.del_zWave_module(moduleId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes



    """SET METHODS"""
    def set_zWaveNetwork_status(self, newStatus):
        succes = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine) and newStatus == "activated" or newStatus == "disabled":
            if self.homeAutomationEngine.set_zWaveNetwork_status(newStatus):
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def set_module_name(self, moduleId, newModuleName):
        succes = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine) and isinstance(moduleId, int) and isinstance(newModuleName, str):
            if self.homeAutomationEngine.set_module_name(moduleId, newModuleName):
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def set_module_location(self, moduleId, newModuleLocation):
        succes = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine) and isinstance(moduleId, int) and isinstance(newModuleLocation, int):
            if self.homeAutomationEngine.set_module_location(moduleId, newModuleLocation):
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def set_module_value(self, moduleId, valueId, newData):
        succes = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine) and isinstance(moduleId, int) and isinstance(valueId, int):
            if self.homeAutomationEngine.set_module_value(moduleId, valueId, newData):
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def set_light_controller_level(self, moduleId, newLevel):
        succes = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine) and isinstance(moduleId, int) and isinstance(newLevel, int):
            if self.homeAutomationEngine.set_light_controller_level(moduleId, newLevel):
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def set_light_controller_color_by_label(self, moduleId, colorLabel):
        succes = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine) and isinstance(moduleId, int) and isinstance(colorLabel, str):
            if self.homeAutomationEngine.set_light_controller_color_by_label(moduleId, colorLabel):
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def set_light_controller_color_by_rgbw(self, moduleId, rgbwValue):
        succes = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine) and isinstance(moduleId, int) and isinstance(rgbwValue, str):
            if self.homeAutomationEngine.set_light_controller_color_by_rgbw(moduleId, rgbwValue):
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes



    ###SWITCH METHODS###
    def switch_light_controller_on(self, moduleId):
        succes = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine) and isinstance(moduleId, int):
            if self.homeAutomationEngine.switch_light_controller_on(moduleId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def switch_light_controller_off(self, moduleId):
        succes = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine) and isinstance(moduleId, int):
            if self.homeAutomationEngine.switch_light_controller_off(moduleId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def switch_relay_on(self, moduleId):
        succes = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine) and isinstance(moduleId, int):
            if self.homeAutomationEngine.switch_relay_on(moduleId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def switch_relay_off(self, moduleId):
        succes = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine) and isinstance(moduleId, int):
            if self.homeAutomationEngine.switch_relay_off(moduleId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes



    """HEAL METHODS"""
    def heal_zWave_network(self):
        succes = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine):
            if self.homeAutomationEngine.heal_zWave_network():
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def heal_zWave_module(self, moduleId):
        succes = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine) and isinstance(moduleId, int):
            if self.homeAutomationEngine.heal_zWave_module(moduleId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes



    """DESTROY METHOD"""
    def destroy_zWave_network(self):
        succes = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine):
            if self.homeAutomationEngine.destroy_zWave_network():
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes



    """UPDATE METHOD"""
    def update_zWave_module_return_route(self, moduleId):
        succes = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine) and isinstance(moduleId, int):
            if self.homeAutomationEngine.update_zWave_module_return_route(moduleId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def update_zWave_module_neighbors(self, moduleId):
        succes = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine) and isinstance(moduleId, int):
            if self.homeAutomationEngine.update_zWave_module_neighbors(moduleId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def update_zWave_module_network(self, moduleId):
        succes = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine) and isinstance(moduleId, int):
            if self.homeAutomationEngine.update_zWave_module_network(moduleId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes



    """REFRESH METHODS"""
    def refresh_zWave_module_informations(self, moduleId):
        succes = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine) and isinstance(moduleId, int):
            if self.homeAutomationEngine.refresh_zWave_module_informations(moduleId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def refresh_zWave_module_value(self, moduleId, valueId):
        succes = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine) and isinstance(moduleId, int) and isinstance(valueId, int):
            if self.homeAutomationEngine.refresh_zWave_module_value(moduleId, valueId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def refresh_module_values(self, moduleId):
        succes = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine) and isinstance(moduleId, int):
            if self.homeAutomationEngine.refresh_module_values(moduleId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes



    """RESET METHOD"""
    def soft_reset_zWave_network(self):
        succes = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine):
            if self.homeAutomationEngine.soft_reset_zWave_network():
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def hard_reset_zWave_network(self):
        succes = False

        if isinstance(self.homeAutomationEngine, HomeAutomationEngine):
            if self.homeAutomationEngine.hard_reset_zWave_network():
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes



    ###SERVER METHODS###
    """LISTEN METHOD"""
    def listen_clients(self):
        eventlet.wsgi.server(eventlet.listen(('', 5000)), app)



    ###CLIENTS REQUESTS###
    """CONNECTION EVENT"""
    @socketIoServer.event(namespace='/HomeAutomationServer')
    def connect(sid, environ, auth):
        print('client connecté ', sid)
        HomeAutomationServer.homeAutomationEngine.zWaveNetwork.send_light_controller_color_updated_event(False)
                


    """GET REQUESTS"""
    @socketIoServer.event(namespace='/HomeAutomationServer')
    def get_home_automation_engine_informations(sid, data):
        succes = homeAutomationEngineInformation = False

        homeAutomationEngineInformation = HomeAutomationServer.homeAutomationEngine.serialize()

        if homeAutomationEngineInformation:
            socketIoServer.emit('post_home_automation_engine_information', {'data': json.dumps(homeAutomationEngineInformation, default=HomeAutomationServer.set_default)}, namespace='/HomeAutomationServer', room = sid)
            succes = True

        else:
            socketIoServer.emit('failed_getting_home_automation_engine_information', {}, namespace='/HomeAutomationServer', room = sid)
            succes = False

        return succes


    @socketIoServer.event(namespace='/HomeAutomationServer')
    def get_zWave_network_status(sid, data):
        succes = zWaveNetworkStatus = False

        zWaveNetworkStatus = HomeAutomationServer.homeAutomationEngine.zWaveNetworkStatus
        
        if zWaveNetworkStatus:
            socketIoServer.emit('post_zWave_network_status', {'data': zWaveNetworkStatus}, namespace='/HomeAutomationServer', room = sid)
            succes = True
        else:
            socketIoServer.emit('failed_getting_zWave_network_status', {}, namespace='/HomeAutomationServer', room = sid)
            succes = False

        return succes


    @socketIoServer.event(namespace='/HomeAutomationServer')
    def get_zWave_network_isRunning(sid, data):
        succes = zWaveNetworkIsRunning = False

        zWaveNetworkIsRunning = HomeAutomationServer.homeAutomationEngine.zWaveNetworkIsRunning
        
        if zWaveNetworkIsRunning:
            socketIoServer.emit('post_zWave_network_isRunning', {'data': zWaveNetworkIsRunning}, namespace='/HomeAutomationServer', room = sid)
            succes = True
        else:
            socketIoServer.emit('failed_getting_zWave_network_isRunning', {}, namespace='/HomeAutomationServer', room = sid)
            succes = False

        return succes


    @socketIoServer.event(namespace='/HomeAutomationServer')
    def get_home_automation_engine_isRunning(sid, data):
        succes = homeAutomationEngineIsRunning = False

        homeAutomationEngineIsRunning = HomeAutomationServer.homeAutomationEngine.running
        
        if homeAutomationEngineIsRunning:
            socketIoServer.emit('post_home_automation_engine_isRunning', {'data': homeAutomationEngineIsRunning}, namespace='/HomeAutomationServer', room = sid)
            succes = True
        else:
            socketIoServer.emit('failed_getting_home_automation_engine_isRunning', {}, namespace='/HomeAutomationServer', room = sid)
            succes = False

        return succes



    @socketIoServer.event(namespace='/HomeAutomationServer')
    def get_zWave_home_id(sid, data):
        succes = zWaveHomeId = False

        zWaveHomeId = HomeAutomationServer.homeAutomationEngine.zWaveHomeId

        if zWaveHomeId:
            socketIoServer.emit('post_zWave_HomeId', {'data': zWaveHomeId}, namespace='/HomeAutomationServer', room = sid)
            succes = True
        else:
            socketIoServer.emit('failed_getting_zWave_HomeId', {}, namespace='/HomeAutomationServer', room = sid)
            succes = False

        return succes


    @socketIoServer.event(namespace='/HomeAutomationServer')
    def get_zWave_network_state(sid, data):
        succes = zWaveNetworkState = False

        zWaveNetworkState = HomeAutomationServer.homeAutomationEngine.zWaveNetworkState

        if zWaveNetworkState:
            socketIoServer.emit('post_zWave_network_state', {'data': zWaveNetworkState}, namespace='/HomeAutomationServer', room = sid)
            succes = True
        else:
            socketIoServer.emit('failed_getting_zWave_network_state', {}, namespace='/HomeAutomationServer', room = sid)
            succes = False

        return succes


    @socketIoServer.event(namespace='/HomeAutomationServer')
    def get_zWave_network_isReady(sid, data):
        zWaveNetworkIsReady = False

        zWaveNetworkIsReady = HomeAutomationServer.homeAutomationEngine.zwaveNetworkIsReady

        socketIoServer.emit('post_zWave_network_isReady', {'data': zWaveNetworkIsReady}, namespace='/HomeAutomationServer', room = sid)
        succes = True

        return succes


    @socketIoServer.event(namespace='/HomeAutomationServer')
    def get_zWave_network_controller_path(sid, data):
        succes = zWaveNetworkControllerPath = False

        zWaveNetworkControllerPath = HomeAutomationServer.homeAutomationEngine.zWaveNetworkControllerPath

        if zWaveNetworkControllerPath:
            socketIoServer.emit('post_zWave_network_controller_path', {'data': zWaveNetworkControllerPath}, namespace='/HomeAutomationServer', room = sid)
            succes = True
        else:
            socketIoServer.emit('failed_getting_zWave_network_controller_path', {}, namespace='/HomeAutomationServer', room = sid)
            succes = False

        return succes


    @socketIoServer.event(namespace='/HomeAutomationServer')
    def get_zWave_config_folder_path(sid, data):
        succes = zwaveConfigFolderPath = False

        zwaveConfigFolderPath = HomeAutomationServer.homeAutomationEngine.zwaveConfigFolderPath

        if zwaveConfigFolderPath:
            socketIoServer.emit('post_zWave_config_folder_path', {'data': zwaveConfigFolderPath}, namespace='/HomeAutomationServer', room = sid)
            succes = True
        else:
            socketIoServer.emit('failed_getting_zWave_config_folder_path', {}, namespace='/HomeAutomationServer', room = sid)
            succes = False

        return succes


    @socketIoServer.event(namespace='/HomeAutomationServer')
    def get_zWave_network_configured(sid, data):
        succes = zWaveNetworkConfigured = False

        zWaveNetworkConfigured = HomeAutomationServer.homeAutomationEngine.zWaveNetworkConfigured

        if zWaveNetworkConfigured:
            socketIoServer.emit('post_zWave_network_configured', {'data': zWaveNetworkConfigured}, namespace='/HomeAutomationServer', room = sid)
            succes = True
        else:
            socketIoServer.emit('failed_getting_zWave_network_configured', {}, namespace='/HomeAutomationServer', room = sid)
            succes = False

        return succes

        
    @socketIoServer.event(namespace='/HomeAutomationServer')
    def get_zWave_modules_list(sid, data):
        succes = zWaveModulesList = modulesListSerialized = False

        zWaveModulesList = HomeAutomationServer.homeAutomationEngine.zWaveModulesList

        if isinstance(zWaveModulesList, list):
            for zWaveModule in zWaveModulesList:
                modulesListSerialized.append(zWaveModule.serialize())

            socketIoServer.emit('post_zWave_modules_list', {'data': modulesListSerialized}, namespace='/HomeAutomationServer', room = sid)
            succes = True
        else:
            socketIoServer.emit('failed_getting_zWave_modules_list', {}, namespace='/HomeAutomationServer', room = sid)
            succes = False

        return succes


    @socketIoServer.event(namespace='/HomeAutomationServer')
    def get_modules_list(sid, data):
        succes = modulesList = serializedModuleList = False

        modulesList = HomeAutomationServer.homeAutomationEngine.modulesList

        if isinstance(modulesList, list):
            for module in modulesList:
                serializedModuleList.append(module.serialize())
                
            socketIoServer.emit('post_modules_list', {'data': serializedModuleList}, namespace='/HomeAutomationServer', room = sid)
            succes = True
        else:
            socketIoServer.emit('failed_getting_modules_list', {}, namespace='/HomeAutomationServer', room = sid)
            succes = False

        return succes

        
    @socketIoServer.event(namespace='/HomeAutomationServer')
    def get_module(sid, data):
        succes = module = moduleId = False

        try:
            moduleId = data["moduleId"]
        except:
            moduleId = False

        if moduleId != False:
            module = HomeAutomationServer.homeAutomationEngine.get_module(moduleId)

            if module != False:
                module = module.serialize()

                socketIoServer.emit('post_module', {'data':module.serialize()}, namespace='/HomeAutomationServer', room = sid)
                succes = True
            else:
                socketIoServer.emit('failed_getting_module', {}, namespace='/HomeAutomationServer', room = sid)
                succes = False
        else:
            succes = False

        return succes



    """ADD REQUESTS"""
    @socketIoServer.event(namespace='/HomeAutomationServer')
    def add_zWave_module(sid, data):
        succes = newModuleId = False

        newModuleId = HomeAutomationServer.homeAutomationEngine.add_zWave_module()

        if newModuleId != False:
            succes = True
        else:
            socketIoServer.emit('failed_adding_module', {}, namespace='/HomeAutomationServer', room = sid)
            succes = False

        return succes



    """DEL REQUESTS"""
    @socketIoServer.event(namespace='/HomeAutomationServer')
    def del_zWave_module(sid, data):
        succes = moduleId = False

        try:
            moduleId = ['moduleId']
        except:
            moduleId = False

        if moduleId != False:
            if HomeAutomationServer.homeAutomationEngine.del_zWave_module(moduleId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        if succes:
            pass
        else:
            socketIoServer.emit('failed_deletting_module', {}, namespace='/HomeAutomationServer', room = sid)
        
        return succes



    """SET REQUESTS"""
    @socketIoServer.event(namespace='/HomeAutomationServer')
    def set_module_name(sid, data):
        succes = moduleId = newName = False

        try:
            moduleId = data['moduleId']
            newName = data['newName']
        except:
            moduleId = False
            newName = False

        if moduleId != False and newName != False:
            if HomeAutomationServer.homeAutomationEngine.module_renamed(moduleId, newName):
                succes = True
            else:
                succes = False
        else:
            succes = False

        if succes:
            socketIoServer.emit('succes_setting_module_name', {}, namespace='/HomeAutomationServer', room = sid)
       
            if HomeAutomationServer.module_updated(HomeAutomationServer, moduleId):
                succes = True
            else:
                succes = False
        else:
            socketIoServer.emit('failed_setting_module_name', {}, namespace='/HomeAutomationServer', room = sid)

        return succes


    @socketIoServer.event(namespace='/HomeAutomationServer')
    def set_module_location(sid, data):
        succes = moduleId = newLocation = False

        try:
            moduleId = data['moduleId']
            newLocation = data['newLocation']
        except:
            moduleId = False
            newLocation = False

        if moduleId != False and newLocation != False:
            if HomeAutomationServer.homeAutomationEngine.set_module_location(moduleId, newLocation):
                succes = True
            else:
                succes = False
        else:
            succes = False

        if succes:
            socketIoServer.emit('succes_setting_module_location', {}, namespace='/HomeAutomationServer', room = sid)
        
            if HomeAutomationServer.module_relocated(HomeAutomationServer, moduleId):
                succes = True
            else:
                succes = False
        else:
            socketIoServer.emit('failed_setting_module_location', {}, namespace='/HomeAutomationServer', room = sid)
        

        return succes


    @socketIoServer.event(namespace='/HomeAutomationServer')
    def set_module_value(sid, data):
        succes = moduleId = valueId = newData = False

        try:
            moduleId = data['moduleId']
            valueId = data['valueId']
            newData = data['newData']
        except:
            moduleId = False
            valueId = False
            newData = False

        if moduleId != False and valueId != False:
            if HomeAutomationServer.homeAutomationEngine.set_module_value(moduleId, valueId, newData):
                succes = True
            else:
                succes = False
        else:
            succes = False

        if succes:
            socketIoServer.emit('succes_setting_module_value', {}, namespace='/HomeAutomationServer', room = sid)
       
            if HomeAutomationServer.module_value_update(HomeAutomationServer, moduleId):
                succes = True
            else:
                succes = False
        else:
            socketIoServer.emit('failed_setting_module_value', {}, namespace='/HomeAutomationServer', room = sid)
        
        return succes


    @socketIoServer.event(namespace='/HomeAutomationServer')
    def set_light_controller_level(sid, data):
        succes = moduleId = newLevel = False

        try:
            moduleId = data['moduleId']
            newLevel = data['newLevel']
        except:
            moduleId = False
            newLevel = False

        if moduleId != False and newLevel != False:
            if HomeAutomationServer.homeAutomationEngine.set_light_controller_level(moduleId, newLevel):
                succes = True
            else:
                succes = False
        else:
            succes = False

        if succes:
            socketIoServer.emit('succes_setting_light_controller_level', {}, namespace='/HomeAutomationServer', room = sid)
        
            if HomeAutomationServer.light_controller_level_updated(HomeAutomationServer, moduleId):
                succes = True
            else:
                succes = False
        else:
            socketIoServer.emit('failed_setting_light_controller_level', {}, namespace='/HomeAutomationServer', room = sid)
        
        return succes


    @socketIoServer.event(namespace='/HomeAutomationServer')
    def set_light_controller_color_by_label(sid, data):
        succes = moduleId = newColorLabel = False

        try:
            moduleId = data['moduleId']
            newColorLabel = data['newColorLabel']
        except:
            moduleId = False
            newColorLabel = False

        if moduleId != False and newColorLabel != False:
            if HomeAutomationServer.homeAutomationEngine.set_light_controller_color_by_label(moduleId, newColorLabel):
                succes = True
            else:
                succes = False
        else:
            succes = False

        if succes:
            socketIoServer.emit('succes_setting_light_controller_color_by_label', {}, namespace='/HomeAutomationServer', room = sid)
        
            if HomeAutomationServer.light_controller_color_updated(HomeAutomationServer, moduleId):
                succes = True
            else:
                succes = False
        else:
            socketIoServer.emit('failed_setting_light_controller_color_by_label', {}, namespace='/HomeAutomationServer', room = sid)
        
        return succes


    @socketIoServer.event(namespace='/HomeAutomationServer')
    def set_light_controller_color_by_rgbw(sid, data):
        succes = moduleId = newRgbwValue = False

        try:
            moduleId = data['moduleId']
            newRgbwValue = data['newRgbwValue']
        except:
            moduleId = False
            newRgbwValue = False

        if moduleId != False and newRgbwValue != False:
            if HomeAutomationServer.homeAutomationEngine.set_light_controller_color_by_rgbw(moduleId, newRgbwValue):
                succes = True
            else:
                succes = False
        else:
            succes = False

        if succes:
            socketIoServer.emit('succes_setting_light_controller_color_by_rgbw', {}, namespace='/HomeAutomationServer', room = sid)
        
            if HomeAutomationServer.light_controller_color_updated(HomeAutomationServer, moduleId):
                succes = True
            else:
                succes = False
        else:
            socketIoServer.emit('failed_setting_light_controller_color_by_rgbw', {}, namespace='/HomeAutomationServer', room = sid)
        
        return succes


        
    """SWITCH REQUEST"""
    @socketIoServer.event(namespace='/HomeAutomationServer')
    def switch_light_controller_on(sid, data):
        succes = moduleId = False

        try:
            moduleId = data['moduleId']
        except:
            moduleId = False

        if moduleId != False:
            if HomeAutomationServer.homeAutomationEngine.switch_light_controller_on(moduleId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        if succes:
            socketIoServer.emit('succes_switching_light_controller_on', {}, namespace='/HomeAutomationServer', room = sid)
        
            if HomeAutomationServer.light_controller_switching_on(HomeAutomationServer, moduleId):
                succes = True
            else:
                succes = False
        else:
            socketIoServer.emit('failed_switching_light_controller_on', {}, namespace='/HomeAutomationServer', room = sid)
        
        return succes


    @socketIoServer.event(namespace='/HomeAutomationServer')
    def switch_light_controller_off(sid, data):
        succes = moduleId = False

        try:
            moduleId = data['moduleId']
        except:
            moduleId = False

        if moduleId != False:
            if HomeAutomationServer.homeAutomationEngine.switch_light_controller_off(moduleId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        if succes:
            socketIoServer.emit('succes_switching_light_controller_off', {}, namespace='/HomeAutomationServer', room = sid)
        
            if HomeAutomationServer.light_controller_switching_off(HomeAutomationServer, moduleId):
                succes = True
            else:
                succes = False
        else:
            socketIoServer.emit('failed_switching_light_controller_off', {}, namespace='/HomeAutomationServer', room = sid)
        
        return succes


    @socketIoServer.event(namespace='/HomeAutomationServer')
    def switch_relay_on(sid, data):
        succes = moduleId = False

        try:
            moduleId = data['moduleId']
        except:
            moduleId = False

        if moduleId != False:
            if HomeAutomationServer.homeAutomationEngine.switch_relay_on(moduleId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        if succes:
            socketIoServer.emit('succes_switching_relay_on', {}, namespace='/HomeAutomationServer', room = sid)
        
            if HomeAutomationServer.relay_switching_on(HomeAutomationServer, moduleId):
                succes = True
            else:
                succes = False
        else:
            socketIoServer.emit('failed_switching_relay_on', {}, namespace='/HomeAutomationServer', room = sid)
        
        return succes


    @socketIoServer.event(namespace='/HomeAutomationServer')
    def switch_relay_off(sid, data):
        succes = moduleId = False

        try:
            moduleId = data['moduleId']
        except:
            moduleId = False

        if moduleId != False:
            if HomeAutomationServer.homeAutomationEngine.switch_relay_off(moduleId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        if succes:
            socketIoServer.emit('succes_switching_relay_off', {}, namespace='/HomeAutomationServer', room = sid)
        
            if HomeAutomationServer.relay_switching_off(HomeAutomationServer, moduleId):
                succes = True
            else:
                succes = False
        else:
            socketIoServer.emit('failed_switching_relay_off', {}, namespace='/HomeAutomationServer', room = sid)
        
        return succes



    """HEAL REQUEST"""
    @socketIoServer.event(namespace='/HomeAutomationServer')
    def heal_zWave_network(sid, data):
        succes = False
            
        if HomeAutomationServer.homeAutomationEngine.heal_zWave_network():
            succes = True
        else:
            succes = False

        if succes:
            socketIoServer.emit('succes_healing_zWave_network', {}, namespace='/HomeAutomationServer', room = sid)
        
            if HomeAutomationServer.zWave_network_healed():
                succes = True
            else:
                succes = False
        else:
            socketIoServer.emit('failed_healing_zWave_network', {}, namespace='/HomeAutomationServer', room = sid)
        
        return succes


    @socketIoServer.event(namespace='/HomeAutomationServer')
    def heal_zWave_module(sid, data):
        succes = moduleId = False

        try:
            moduleId = data['moduleId']
        except:
            moduleId = False

        if moduleId != False:
            if HomeAutomationServer.homeAutomationEngine.heal_zWave_module(moduleId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        if succes:
            socketIoServer.emit('succes_healing_zWave_module', {}, namespace='/HomeAutomationServer', room = sid)
        
            if HomeAutomationServer.zWave_module_healed(HomeAutomationServer, moduleId):
                succes = True
            else:
                succes = False
        else:
            socketIoServer.emit('failed_healing_zWave_module', {}, namespace='/HomeAutomationServer', room = sid)
        
        return succes



    """DESTROY REQUEST"""
    @socketIoServer.event(namespace='/HomeAutomationServer')
    def destroy_zWave_network(sid, data):
        succes = False
            
        if HomeAutomationServer.homeAutomationEngine.destroy_zWave_network():
            succes = True
        else:
            succes = False

        if succes:
            socketIoServer.emit('succes_destroying_zWave_network', {}, namespace='/HomeAutomationServer', room = sid)
        
            if HomeAutomationServer.zWave_network_destroyed():
                succes = True
            else:
                succes = False
        else:
            socketIoServer.emit('failed_destroying_zWave_network', {}, namespace='/HomeAutomationServer', room = sid)
        
        return succes



    """UPDATE REQUEST"""
    @socketIoServer.event(namespace='/HomeAutomationServer')
    def update_zWave_module_return_route(sid, data):
        succes = moduleId = False

        try:
            moduleId = data['moduleId']
        except:
            moduleId = False

        if moduleId != False:
            if HomeAutomationServer.homeAutomationEngine.update_zWave_module_return_route(moduleId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        if succes:
            socketIoServer.emit('succes_updating_zWave_module_return_route', {}, namespace='/HomeAutomationServer', room = sid)
        
            if HomeAutomationServer.zWave_module_return_route_updated(HomeAutomationServer, moduleId):
                succes = True
            else:
                succes = False
        else:
            socketIoServer.emit('failed_updating_zWave_module_return_route', {}, namespace='/HomeAutomationServer', room = sid)
        
        return succes


    @socketIoServer.event(namespace='/HomeAutomationServer')
    def update_zWave_module_neighbors(sid, data):
        succes = moduleId = False

        try:
            moduleId = data['moduleId']
        except:
            moduleId = False

        if moduleId != False:
            if HomeAutomationServer.homeAutomationEngine.update_zWave_module_neighbors(moduleId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        if succes:
            socketIoServer.emit('succes_updating_zWave_module_neighbors', {}, namespace='/HomeAutomationServer', room = sid)
        
            if HomeAutomationServer.zWave_module_neighbors_updated(HomeAutomationServer, moduleId):
                succes = True
            else:
                succes = False
        else:
            socketIoServer.emit('failed_updating_zWave_module_neighbors', {}, namespace='/HomeAutomationServer', room = sid)
        
        return succes


    @socketIoServer.event(namespace='/HomeAutomationServer')
    def update_zWave_module_network(sid, data):
        succes = moduleId = False

        try:
            moduleId = data['moduleId']
        except:
            moduleId = False

        if moduleId != False:
            if HomeAutomationServer.homeAutomationEngine.update_zWave_module_network(moduleId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        if succes:
            socketIoServer.emit('succes_updating_zWave_module_network', {}, namespace='/HomeAutomationServer', room = sid)
        
            if HomeAutomationServer.module_updated(HomeAutomationServer, moduleId):
                succes = True
            else:
                succes = False
        else:
            socketIoServer.emit('failed_updating_zWave_module_network', {}, namespace='/HomeAutomationServer', room = sid)
        
        return succes



    """REFRESH REQUESTS"""
    @socketIoServer.event(namespace='/HomeAutomationServer')
    def refresh_zWave_module_informations(sid, data):
        succes = moduleId = False

        try:
            moduleId = data['moduleId']
        except:
            moduleId = False

        if moduleId != False:
            if HomeAutomationServer.homeAutomationEngine.refresh_zWave_module_informations(moduleId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        if succes:
            socketIoServer.emit('succes_refreshing_zWave_module_informations', {}, namespace='/HomeAutomationServer', room = sid)
        
            if HomeAutomationServer.zWave_module_informations_refreshed(HomeAutomationServer, moduleId):
                succes = True
            else:
                succes = False
        else:
            socketIoServer.emit('failed_refreshing_zWave_module_informations', {}, namespace='/HomeAutomationServer', room = sid)
        
        return succes


    @socketIoServer.event(namespace='/HomeAutomationServer')
    def refresh_zWave_module_value(sid, data):
        succes = moduleId = valueId = False

        try:
            moduleId = data['moduleId']
            valueId = data['valueId']
            
        except:
            moduleId = False
            valueId = False

        if moduleId != False:
            if HomeAutomationServer.homeAutomationEngine.refresh_zWave_module_value(moduleId, valueId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        if succes:
            socketIoServer.emit('succes_refreshing_zWave_module_value', {}, namespace='/HomeAutomationServer', room = sid)
        
            if HomeAutomationServer.module_updated(HomeAutomationServer, moduleId):
                succes = True
            else:
                succes = False
        else:
            socketIoServer.emit('failed_refreshing_zWave_module_value', {}, namespace='/HomeAutomationServer', room = sid)
        
        return succes


    @socketIoServer.event(namespace='/HomeAutomationServer')
    def refresh_zWave_module_values(sid, data):
        succes = moduleId = False

        try:
            moduleId = data['moduleId']
        except:
            moduleId = False

        if moduleId != False:
            if HomeAutomationServer.homeAutomationEngine.refresh_module_values(moduleId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        if succes:
            socketIoServer.emit('succes_refreshing_zWave_module_values', {}, namespace='/HomeAutomationServer', room = sid)
        
            if HomeAutomationServer.zWave_module_values_refreshed(HomeAutomationServer, moduleId):
                succes = True
            else:
                succes = False
        else:
            socketIoServer.emit('failed_refreshing_zWave_module_values', {}, namespace='/HomeAutomationServer', room = sid)
        
        return succes



    """RESET REQUESTS"""
    @socketIoServer.event(namespace='/HomeAutomationServer')
    def soft_reset_zWave_network(sid, data):
        succes = False
            
        if HomeAutomationServer.homeAutomationEngine.soft_reset_zWave_network():
            succes = True
        else:
            succes = False

        if succes:
            socketIoServer.emit('succes_soft_resetting_zWave_network', {}, namespace='/HomeAutomationServer', room = sid)
        
            if HomeAutomationServer.zWave_network_soft_resetted():
                succes = True
            else:
                succes = False
        else:
            socketIoServer.emit('failed_soft_resetting_zWave_network', {}, namespace='/HomeAutomationServer', room = sid)
        
        return succes


    @socketIoServer.event(namespace='/HomeAutomationServer')
    def hard_reset_zWave_network(sid, data):
        succes = False
            
        if HomeAutomationServer.homeAutomationEngine.hard_reset_zWave_network():
            succes = True
        else:
            succes = False

        if succes:
            socketIoServer.emit('succes_hard_resetting_zWave_network', {}, namespace='/HomeAutomationServer', room = sid)
        
            if HomeAutomationServer.zWave_network_hard_resetted():
                succes = True
            else:
                succes = False
        else:
            socketIoServer.emit('failed_hard_resetting_zWave_network', {}, namespace='/HomeAutomationServer', room = sid)
        
        return succes



    """ACTIVATION REQUESTS"""
    @socketIoServer.event(namespace='/HomeAutomationServer')
    def activate_zWave_network(sid, data):
        succes = False
            
        if HomeAutomationServer.homeAutomationEngine.activate_zWave_network():
            succes = True
        else:
            succes = False

        if succes:
            socketIoServer.emit('succes_activating_zWave_network', {}, namespace='/HomeAutomationServer', room = sid)
       
            if HomeAutomationServer.zWave_network_activated():
                succes = True
            else:
                succes = False
        else:
            socketIoServer.emit('failed_activating_zWave_network', {}, namespace='/HomeAutomationServer', room = sid)
        
        return succes



    """DEACTIVATE REQUESTS"""
    @socketIoServer.event(namespace='/HomeAutomationServer')
    def deactivate_zWave_network(sid, data):
        succes = False
            
        if HomeAutomationServer.homeAutomationEngine.deactivate_zWave_network():
            succes = True
        else:
            succes = False

        if succes:
            socketIoServer.emit('succes_deactivating_zWave_network', {}, namespace='/HomeAutomationServer', room = sid)
        
            if HomeAutomationServer.zWave_network_deactivated():
                succes = True
            else:
                succes = False
        else:
            socketIoServer.emit('failed_deactivating_zWave_network', {}, namespace='/HomeAutomationServer', room = sid)
        
        return succes



    """START REQUESTS"""
    @socketIoServer.event(namespace='/HomeAutomationServer')
    def start_zWave_network(sid, data):
        succes = False
            
        if HomeAutomationServer.homeAutomationEngine.start_zWave_network():
            succes = True
        else:
            succes = False

        if succes:
            socketIoServer.emit('succes_starting_zWave_network', {}, namespace='/HomeAutomationServer', room = sid)
        
            if HomeAutomationServer.zWave_network_started():
                succes = True
            else:
                succes = False
        else:
            socketIoServer.emit('failed_starting_zWave_network', {}, namespace='/HomeAutomationServer', room = sid)
        
        return succes


    @socketIoServer.event(namespace='/HomeAutomationServer')
    def start_home_automation_engine(sid, data):
        succes = False
            
        if HomeAutomationServer.homeAutomationEngine.start():
            succes = True
        else:
            succes = False

        if succes:
            socketIoServer.emit('succes_starting_home_automation_engine', {}, namespace='/HomeAutomationServer', room = sid)
        
            if HomeAutomationServer.home_automation_engine_started():
                succes = True
            else:
                succes = False
        else:
            socketIoServer.emit('failed_starting_home_automation_engine', {}, namespace='/HomeAutomationServer', room = sid)
        
        return succes


        
    """STOP REQUESTS"""
    @socketIoServer.event(namespace='/HomeAutomationServer')
    def stop_zWave_network(sid, data):
        succes = False
            
        if HomeAutomationServer.homeAutomationEngine.stop_zWave_network():
            succes = True
        else:
            succes = False

        if succes:
            socketIoServer.emit('succes_stopping_zWave_network', {}, namespace='/HomeAutomationServer', room = sid)
        
            if HomeAutomationServer.zWave_network_stopped():
                succes = True
            else:
                succes = False
        else:
            socketIoServer.emit('failed_stopping_zWave_network', {}, namespace='/HomeAutomationServer', room = sid)
        
        return succes


    @socketIoServer.event(namespace='/HomeAutomationServer')
    def stop_home_automation_engine(sid, data):
        succes = False
            
        if HomeAutomationServer.homeAutomationEngine.stop():
            succes = True
        else:
            succes = False

        if succes:
            socketIoServer.emit('succes_stopping_home_automation_engine', {}, namespace='/HomeAutomationServer', room = sid)
        
            if HomeAutomationServer.home_automation_engine_stopped():
                succes = True
            else:
                succes = False
        else:
            socketIoServer.emit('failed_stopping_home_automation_engine', {}, namespace='/HomeAutomationServer', room = sid)
        
        return succes



    """RESTART REQUESTS"""
    @socketIoServer.event(namespace='/HomeAutomationServer')
    def restart_zWave_network(sid, data):
        succes = False
            
        if HomeAutomationServer.homeAutomationEngine.restart_zWave_network():
            succes = True
        else:
            succes = False

        if succes:
            socketIoServer.emit('succes_restarting_zWave_network', {}, namespace='/HomeAutomationServer', room = sid)
        
            if HomeAutomationServer.zWave_network_restarted():
                succes = True
            else:
                succes = False
        else:
            socketIoServer.emit('failed_restarting_zWave_network', {}, namespace='/HomeAutomationServer', room = sid)
        
        return succes


    @socketIoServer.event(namespace='/HomeAutomationServer')
    def restart_home_automation_engine(sid, data):
        succes = False
            
        if HomeAutomationServer.homeAutomationEngine.restart():
            succes = True
        else:
            succes = False

        if succes:
            socketIoServer.emit('succes_restarting_home_automation_engine', {}, namespace='/HomeAutomationServer', room = sid)
        
            if HomeAutomationServer.home_automation_engine_restarted():
                succes = True
            else:
                succes = False
        else:
            socketIoServer.emit('failed_restarting_home_automation_engine', {}, namespace='/HomeAutomationServer', room = sid)
        
        return succes


 
    ###SERVER EVENT###



    ####
    def set_default(obj):
        if isinstance(obj, set):
            return list(obj)
        raise TypeError

