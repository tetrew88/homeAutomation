import sys
import os

import json

import time
import datetime

sys.path.append("..")

from homeAutomationEngine.homeAutomationNetworks.zWaveNetwork.classes.zWaveNetwork import *

from .engineEvents.engineEvent import *
from .engineEvents.engineStarted import *
from .engineEvents.engineStopped import *



class HomeAutomationEngine:

    homeAutomationEngine = False

    def __init__(self, scriptPath, server=False):
        self.scriptPath = scriptPath
        self.configFilePath = scriptPath + "/configs/homeAutomationEngineConfig.json"
        self.zWaveNetwork = Network(self.scriptPath + '/homeAutomationNetworks/zWaveNetwork', server)
        self.running = False
        self.server = server
        self.events = []

    

    """PROPERTY"""
    ###ENGINE INFORMATIONS###
    @property
    def engineConfigured(self):
        engineConfigured = False

        try:
            with open(self.configFilePath) as configurationFile:
                data = json.load(configurationFile)
                engineConfigured = bool(data["engineConfigured"])
        except:
            engineConfigured = False

        return engineConfigured


    ###ZWAVE NETWORK INFORMATIONS###
    @property
    def zWaveNetworkStatus(self):
        """
            property allows to know if the zwave Network was enabled or disabled
        """

        status = False
        
        if isinstance(self.zWaveNetwork, Network):
            status = self.zWaveNetwork.status
        else:
            status = False

        return status


    @property
    def zWaveNetworkConfigured(self):
        zWaveNetworkConfigured = False

        if isinstance(self.zWaveNetwork, Network):
            zWaveNetworkConfigured = self.zWaveNetwork.networkConfigured
        else:
            zWaveNetworkConfigured = False

        return zWaveNetworkConfigured


    @property
    def zWaveHomeId(self):
        zWaveHomeId = False

        if isinstance(self.zWaveNetwork, Network):
            zWaveHomeId = self.zWaveNetwork.homeId
        else:
            zWaveHomeId = False

        return zWaveHomeId


    @property
    def zWaveNetworkState(self):
        state = False

        if isinstance(self.zWaveNetwork, Network):
            state = self.zWaveNetwork.strState
        else:
            state = False

        return state


    @property
    def zwaveNetworkIsReady(self):
        zwaveNetworkIsReady = False

        if isinstance(self.zWaveNetwork, Network):
            zwaveNetworkIsReady = self.zWaveNetwork.isReady
        else:
            zwaveNetworkIsReady = False

        return zwaveNetworkIsReady


    @property
    def zWaveNetworkControllerPath(self):
        zWaveNetworkControllerPath = False

        if isinstance(self.zWaveNetwork, Network):
            zWaveNetworkControllerPath = self.zWaveNetwork.controllerPath
        else:
            zWaveNetworkControllerPath = False

        return zWaveNetworkControllerPath


    @property
    def zwaveConfigFolderPath(self):
        zwaveConfigFolderPath = False

        if isinstance(self.zWaveNetwork, Network):
            zwaveConfigFolderPath = self.zWaveNetwork.zwaveConfigFolderPath
        else:
            zwaveConfigFolderPath = False

        return zwaveConfigFolderPath


    @property
    def zWaveNetworkIsRunning(self):
        zWaveNetworkIsRunning = False

        if isinstance(self.zWaveNetwork, Network):
            zWaveNetworkIsRunning = self.zWaveNetwork.running
        else:
            zWaveNetworkIsRunning = False

        return zWaveNetworkIsRunning


    @property
    def zWaveModulesList(self):
        zWaveModuleList = []

        if isinstance(self.zWaveNetwork, Network):
            zWaveModuleList = self.zWaveNetwork.modulesList
        else:
            zWaveModuleList = []

        return zWaveModuleList


    @property
    def zWaveEventsList(self):
        zWaveEventsList = []

        if isinstance(self.zWaveNetwork, Network):
            zWaveEventsList = self.zWaveNetwork.eventList
        else:
            zWaveEventsList = []

        return zWaveEventsList


    @property
    def modulesList(self):
        modulesList = []

        modulesList = self.zWaveNetwork.modulesList

        return modulesList


    @property
    def eventsList(self):
        eventsList = []

        eventsList = self.zWaveEventsList + self.events

        return eventsList




    ###BASE METHODS###
    def start(self):
        succes = False

        if self.engineConfigured:
            if isinstance(self.zWaveNetwork, Network):
                if self.zWaveNetworkStatus == "activated":
                    if self.start_zWave_network():
                        succes = True
                    else:
                        succes = False
                else:
                    succes = True
            else:
                succes = False
        else:
            succes = False

        if succes:
            self.running = True

        return succes

    
    def stop(self):
        succes = False

        if self.running:
            if isinstance(self.zWaveNetwork, Network):
                if self.stop_zWave_network():
                    succes = True
                else:
                    succes = False
            else:
                succes = False
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


    def serialize(self):
        data = {}
        zWaveModulesList = zWaveEventsList = []
        modulesList = eventsList = []

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
    """GET METHODS"""
    def get_module(self, moduleId):
        moduleList = selectedModule = False

        moduleList = self.modulesList

        if isinstance(moduleId, int):
            if isinstance(moduleList, list):
                for module in moduleList:
                    if module.id == moduleId:
                        selectedModule = module
                        break
            else:
                selectedModule = False
        else:
            succes = False

        return selectedModule



    """ADD METHODS"""
    def add_zWave_module(self):
        succes = False

        if isinstance(self.zWaveNetwork, Network):
            if self.zWaveNetworkIsRunning:
                moduleId = self.zWaveNetwork.add_module()

                if isinstance(moduleId, int):
                    succes = True
                else:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        if succes:
            return moduleId
        else:
            return False



    """DEL METHODS"""
    def del_zWave_module(self, moduleId):
        succes = False

        if isinstance(self.zWaveNetwork, Network):
            if self.zWaveNetworkIsRunning:
                if self.zWaveNetwork.del_module(moduleId):
                    succes = True
                else:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        return succes



    """SET METHODS"""
    def set_zWaveNetwork_status(self, newStatus):
        succes = data = False

        if isinstance(newStatus, str) and newStatus == "activated" or newStatus == "disabled":
            if isinstance(self.zWaveNetwork, Network):
                if self.zWaveNetwork.set_status(newStatus):
                    succes = True
                else:
                    succes = False
            else:
                succes = False 
        else:
            succes = False
        
        return succes


    def set_module_name(self, moduleId, newModuleName):
        succes = selectedModule = False

        if isinstance(moduleId, int) and isinstance(newModuleName, str):
            selectedModule = self.get_module(moduleId)

            if selectedModule != False:
                if selectedModule.protocol == "zWave":
                    if self.zWaveNetworkIsRunning:
                        if isinstance(self.zWaveNetwork, Network):
                            if self.zWaveNetwork.set_module_name(moduleId, newModuleName):
                                succes = True
                            else:
                                succes = False
                        else:
                            succes = False
                    else:
                        succes = False
                else:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        return succes


    def set_module_location(self, moduleId, newModuleLocation):
        succes = selectedModule = False

        if isinstance(moduleId, int) and isinstance(newModuleLocation, int):
            selectedModule = self.get_module(moduleId)

            if selectedModule != False:
                if selectedModule.protocol == "zWave":
                    if self.zWaveNetworkIsRunning:
                        if isinstance(self.zWaveNetwork, Network):
                            if self.zWaveNetwork.set_module_location(moduleId, newModuleLocation):
                                succes = True
                            else:
                                succes = False
                        else:
                            succes = False
                    else:
                        succes = False
                else:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        return succes


    def set_module_value(self, moduleId, valueId, newData):
        succes = selectedModule = False

        if isinstance(moduleId, int) and isinstance(valueId, int):
            selectedModule = self.get_module(moduleId)

            if selectedModule != False:
                if selectedModule.protocol == "zWave":
                    if self.zWaveNetworkIsRunning:
                        if isinstance(self.zWaveNetwork, Network):
                            if self.zWaveNetwork.set_module_value(moduleId, valueId, newData):
                                succes = True
                            else:
                                succes = False
                        else:
                            succes = False
                    else:
                        succes = False
                else:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        return succes


    def set_light_controller_level(self, moduleId, newLevel):
        succes = selectedModule = False

        if isinstance(moduleId, int) and isinstance(newLevel, int):
            selectedModule = self.get_module(moduleId)

            if selectedModule.protocol == "zWave":
                if isinstance(selectedModule, ZWaveLightController):
                    if self.zWaveNetworkIsRunning:
                        if isinstance(self.zWaveNetwork, Network):
                            if self.zWaveNetwork.set_light_controller_level(moduleId, newLevel):
                                succes = True
                            else:
                                succes = False
                        else:
                            succes = False
                    else:
                        succes = False
                else:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        return succes


    def set_light_controller_color_by_label(self, moduleId, colorLabel):
        succes = selectedModule = False

        if isinstance(moduleId, int) and isinstance(colorLabel, str):
            selectedModule = self.get_module(moduleId)

            if selectedModule.protocol == "zWave":
                if isinstance(selectedModule, ZWaveColorLightController):
                    if self.zWaveNetworkIsRunning:
                        if isinstance(self.zWaveNetwork, Network):
                            if colorLabel in selectedModule.colorPalette:
                                if self.zWaveNetwork.set_light_controller_color_by_label(moduleId, colorLabel):
                                    succes = True
                                else:
                                    succes = False
                            else:
                                succes = False
                        else:
                            succes = False
                    else:
                        succes = False
                else:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        return succes


    def set_light_controller_color_by_rgbw(self, moduleId, rgbwValue):
        succes = selectedModule = False

        if isinstance(moduleId, int) and isinstance(rgbwValue, str):
            selectedModule = self.get_module(moduleId)

            if selectedModule.protocol == "zWave":
                if isinstance(selectedModule, ZWaveColorLightController):
                    if self.zWaveNetworkIsRunning:
                        if isinstance(self.zWaveNetwork, Network):
                            if self.zWaveNetwork.set_light_controller_color_by_rgbw(moduleId, rgbwValue):
                                succes = True
                            else:
                                succes = False
                        else:
                            succes = False
                    else:
                        succes = False
                else:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        return succes



    ###SWITCH METHODS###
    def switch_light_controller_on(self, moduleId):
        succes = False

        succes = selectedModule = False

        if isinstance(moduleId, int) :
            selectedModule = self.get_module(moduleId)

            if selectedModule.protocol == "zWave":
                if isinstance(selectedModule, ZWaveLightController):
                    if self.zWaveNetworkIsRunning:
                        if isinstance(self.zWaveNetwork, Network):
                            if self.zWaveNetwork.switch_light_controller_on(moduleId):
                                succes = True
                            else:
                                succes = False
                        else:
                            succes = False
                    else:
                        succes = False
                else:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        return succes


    def switch_light_controller_off(self, moduleId):
        succes = False

        succes = selectedModule = False

        if isinstance(moduleId, int) :
            selectedModule = self.get_module(moduleId)

            if selectedModule.protocol == "zWave":
                if isinstance(selectedModule, ZWaveLightController):
                    if self.zWaveNetworkIsRunning:
                        if isinstance(self.zWaveNetwork, Network):
                            if self.zWaveNetwork.switch_light_controller_off(moduleId):
                                succes = True
                            else:
                                succes = False
                        else:
                            succes = False
                    else:
                        succes = False
                else:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        return succes


    def switch_relay_on(self, moduleId):
        succes = False

        succes = selectedModule = False

        if isinstance(moduleId, int) :
            selectedModule = self.get_module(moduleId)

            if selectedModule.protocol == "zWave":
                if isinstance(selectedModule, ZWaveRelay):
                    if self.zWaveNetworkIsRunning:
                        if isinstance(self.zWaveNetwork, Network):
                            if self.zWaveNetwork.switch_relay_on(moduleId):
                                succes = True
                            else:
                                succes = False
                        else:
                            succes = False
                    else:
                        succes = False
                else:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        return succes


    def switch_relay_off(self, moduleId):
        succes = False

        succes = selectedModule = False

        if isinstance(moduleId, int) :
            selectedModule = self.get_module(moduleId)

            if selectedModule.protocol == "zWave":
                if isinstance(selectedModule, ZWaveRelay):
                    if self.zWaveNetworkIsRunning:
                        if isinstance(self.zWaveNetwork, Network):
                            if self.zWaveNetwork.switch_relay_off(moduleId):
                                succes = True
                            else:
                                succes = False
                        else:
                            succes = False
                    else:
                        succes = False
                else:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        return succes



    """HEAL METHODS"""
    def heal_zWave_network(self):
        succes = False

        if self.zWaveNetworkIsRunning:
            if isinstance(self.zWaveNetwork, Network):
                if self.zWaveNetwork.heal_network():
                    succes = True
                else:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        return succes


    def heal_zWave_module(self, moduleId):
        succes = selectedModule = False

        if isinstance(moduleId, int):
            if selectedModule.protocol == "zWave":
                if self.zWaveNetworkIsRunning:
                    if isinstance(self.zWaveNetwork, Network):
                        selectedModule = False

                        selectedModule = self.get_module(moduleId)

                        if isinstance(selectedModule, ZWaveModule):
                            if self.zWaveNetwork.heal_module(selectedModule.id):
                                succes = True
                            else:
                                succes = False
                        else:
                            succes = False
                    else:
                        succes = False
                else:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        return succes



    """DESTROY METHOD"""
    def destroy_zWave_network(self):
        succes = False

        if self.zWaveNetworkIsRunning:
            if isinstance(self.zWaveNetwork, Network):
                if self.zWaveNetwork.destroy_network():
                    succes = True
                else:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        return succes



    """UPDATE METHOD"""
    def update_zWave_module_return_route(self, moduleId):
        succes = False

        succes = selectedModule = False

        if isinstance(moduleId, int) :
            selectedModule = self.get_module(moduleId)

            if selectedModule.protocol == "zWave":
                if self.zWaveNetworkIsRunning:
                    if isinstance(self.zWaveNetwork, Network):
                        if self.zWaveNetwork.update_module_return_route(moduleId):
                            succes = True
                        else:
                            succes = False
                    else:
                        succes = False
                else:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        return succes


    def update_zWave_module_neighbors(self, moduleId):
        succes = False

        succes = selectedModule = False

        if isinstance(moduleId, int) :
            selectedModule = self.get_module(moduleId)

            if selectedModule.protocol == "zWave":
                if self.zWaveNetworkIsRunning:
                    if isinstance(self.zWaveNetwork, Network):
                        if self.zWaveNetwork.update_module_neighbors(moduleId):
                            succes = True
                        else:
                            succes = False
                    else:
                        succes = False
                else:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        return succes


    def update_zWave_module_network(self, moduleId):
        succes = False

        succes = selectedModule = False

        if isinstance(moduleId, int) :
            selectedModule = self.get_module(moduleId)

            if selectedModule.protocol == "zWave":
                if self.zWaveNetworkIsRunning:
                    if isinstance(self.zWaveNetwork, Network):
                        if self.zWaveNetwork.update_module_network(moduleId):
                            succes = True
                        else:
                            succes = False
                    else:
                        succes = False
                else:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        return succes



    """REFRESH METHODS"""
    def refresh_zWave_module_informations(self, moduleId):
        succes = False

        succes = selectedModule = False

        if isinstance(moduleId, int) :
            selectedModule = self.get_module(moduleId)

            if selectedModule.protocol == "zWave":
                if self.zWaveNetworkIsRunning:
                    if isinstance(self.zWaveNetwork, Network):
                        if self.zWaveNetwork.refresh_module_informations(moduleId):
                            succes = True
                        else:
                            succes = False
                    else:
                        succes = False
                else:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        return succes


    def refresh_zWave_module_value(self, moduleId, valueId):
        succes = False

        succes = selectedModule = False

        if isinstance(moduleId, int) and isinstance(valueId, int):
            selectedModule = self.get_module(moduleId)

            if selectedModule.protocol == "zWave":
                if self.zWaveNetworkIsRunning:
                    if isinstance(self.zWaveNetwork, Network):
                        if self.zWaveNetwork.refresh_module_value(moduleId, valueId):
                            succes = True
                        else:
                            succes = False
                    else:
                        succes = False
                else:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        return succes


    def refresh_module_values(self, moduleId):
        succes = False

        succes = selectedModule = False

        if isinstance(moduleId, int) :
            selectedModule = self.get_module(moduleId)

            if selectedModule.protocol == "zWave":
                if self.zWaveNetworkIsRunning:
                    if isinstance(self.zWaveNetwork, Network):
                        if self.zWaveNetwork.refresh_module_values(moduleId):
                            succes = True
                        else:
                            succes = False
                    else:
                        succes = False
                else:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        return succes



    """RESET METHOD"""
    def soft_reset_zWave_network(self):
        succes = False

        if self.zWaveNetworkIsRunning:
            if isinstance(self.zWaveNetwork, Network):
                if self.zWaveNetwork.soft_reset_network():
                    succes = True
                else:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        return succes


    def hard_reset_zWave_network(self):
        succes = False

        if self.zWaveNetworkIsRunning:
            if isinstance(self.zWaveNetwork, Network):
                if self.zWaveNetwork.hard_reset_network():
                    succes = True
                else:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        return succes



    """ACTIVATION METHODS"""
    def activate_zWave_network(self):
        succes = False

        if isinstance(self.zWaveNetwork, Network):
            if self.zWaveNetwork.activate():
                succes = True
        else:
            succes = False

        return succes



    """DEACTIVATION METHODS"""
    def deactivate_zWave_network(self):
        succes = False

        if isinstance(self.zWaveNetwork, Network):
            if self.zWaveNetwork.deactivate():
                succes = True
        else:
            succes = False

        return succes

    

    """START METHODS"""
    def start_zWave_network(self):
        succes = False

        if isinstance(self.zWaveNetwork, Network):
            if self.zWaveNetwork.running == False:
                if self.zWaveNetworkStatus == "activated":
                    if self.zWaveNetworkConfigured:
                        if self.zWaveNetwork.start():
                            succes = True
                        else:
                            succes = False
                    else:
                        succes = False
                else:
                    succes = False
            else:
                succes = True
        else:
            succes = False

        return succes



    """STOP METHODS"""
    def stop_zWave_network(self):
        succes = False

        if isinstance(self.zWaveNetwork, Network):
            if self.zWaveNetwork.running:
                if self.zWaveNetwork.stop():
                    succes = True
                else:
                    succes = False
            else:
                succes = True
        else:
            succes = False

        return succes



    """RESTART METHODS"""
    def restart_zWave_network(self):
        succes = False

        if isinstance(self.zWaveNetwork, Network):
            if self.zWaveNetworkIsRunning:
                if self.stop_zWave_network():
                    if self.start_zWave_network():
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

    

    ###ENGINE EVENT###
    def engine_started(self):
        succes = eventDatetime = event = False
        
        try:
            eventDatetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            event = EngineStarted(eventDatetime)
            self.events.append(event)

            if event in self.events:
                succes = True
            else:
                succes = False

            if self.server != False and succes:
                if self.send_home_automation_engine_started_event(event):
                    succes = True
                else:
                    succes = False
                pass
            else:
                pass
        except:
            succes = False

        return succes


    def engine_stopped(self):
        succes = eventDatetime = event = False
        
        try:
            eventDatetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            event = EngineStopped(eventDatetime)
            self.events.append(event)

            if event in self.events:
                succes = True
            else:
                succes = False

            if self.server != False and succes:
                if self.send_home_automation_engine_stopped_event(event):
                    succes = True
                else:
                    succes = False
                pass
            else:
                pass
        except:
            succes = False

        return succes



    ###SERVER EVENT###
    def send_home_automation_engine_started_event(self, event):
        succes = False

        if self.server != False and isinstance(event, EngineStarted):
            self.server.emit('home_automation_engine_started', event.serialize(), namespace='/HomeAutomationServer')
                
            if self.send_home_automation_engine_informations():
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def send_home_automation_engine_stopped_event(self, event):
        succes = False

        if self.server != False and isinstance(event, EngineStopped):
            self.server.emit('home_automation_engine_stopped', event.serialize(), namespace='/HomeAutomationServer')
                
            if self.send_home_automation_engine_informations():
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes



    ###SEND INFORMATIONS###
    def send_home_automation_engine_informations(self):
        succes = False

        if self.server != False and isinstance(self.zWaveNetwork, Network):
            self.server.emit('send_home_automation_engine_informations', self.serialize(), namespace='/HomeAutomationServer')
            
            if self.zWaveNetwork.send_zWave_network_informations():
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes
