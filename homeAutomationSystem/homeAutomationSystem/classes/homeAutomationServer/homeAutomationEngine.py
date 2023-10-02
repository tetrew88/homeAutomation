import json
import sys
sys.path.append("..")

from homeAutomationSystem.classes.residence.modules.module import *

from homeAutomationSystem.classes.residence.modules.zWaveModules.zWaveModule import *

from homeAutomationSystem.classes.residence.modules.zWaveModules.zWaveLightControllers.zWaveLightController import *
from homeAutomationSystem.classes.residence.modules.zWaveModules.zWaveLightControllers.zWaveColorLightController import *

from homeAutomationSystem.classes.residence.modules.zWaveModules.zWaveRelays.zWaveRelay import *

from homeAutomationSystem.classes.residence.modules.zWaveModules.zWaveNetworkController import *

from homeAutomationSystem.classes.residence.modules.zWaveModules.zWaveSensors.zWaveSensor import *
from homeAutomationSystem.classes.residence.modules.zWaveModules.zWaveSensors.zWaveAccesControlSensor import *
from homeAutomationSystem.classes.residence.modules.zWaveModules.zWaveSensors.zWaveLuminanceSensor import *
from homeAutomationSystem.classes.residence.modules.zWaveModules.zWaveSensors.zWaveMotionSensor import *
from homeAutomationSystem.classes.residence.modules.zWaveModules.zWaveSensors.zWaveTemperatureSensor import *

from homeAutomationSystem.classes.residence.values.value import *

from homeAutomationSystem.classes.residence.values.zWaveValues.zWaveValue import *
from homeAutomationSystem.classes.residence.values.zWaveValues.zWaveParametter import *


class HomeAutomationEngine:
    """
        class representing the home automation server:
            property:

            methods:

            server event:
    """


    def __init__(self, homeAutomationServer = False):
        self.running = False
        self.zWaveNetworkStatus = False
        self.zWaveNetworkIsRunning = False
        self.zWaveHomeId = False
        self.zWaveNetworkState = False
        self.zwaveNetworkIsReady = False
        self.zWaveNetworkControllerPath = False
        self.zwaveConfigFolderPath = False
        self.modulesList = False

        self.homeAutomationServer = homeAutomationServer


    ###METHODS###
    """ASK METHODS"""
    def ask_home_automation_engine_information(self):
        succes = True

        self.homeAutomationServer.emit('get_home_automation_engine_informations', {}, namespace='/HomeAutomationServer')

        return succes


    """GET METHODS"""
    def get_home_automation_engine_isRunning(self):
        homeAutomationEngineIsRunning = False

        self.homeAutomationServer.emit('get_home_automation_engine_isRunning', {}, namespace='/HomeAutomationServer')

        homeAutomationEngineIsRunning = self.running
        
        return homeAutomationEngineIsRunning


    def get_zWave_network_status(self):
        zWaveNetworkStatus = False

        self.homeAutomationServer.emit('get_zWave_network_status', {}, namespace='/HomeAutomationServer')

        zWaveNetworkStatus = self.zWaveNetworkStatus
        
        return zWaveNetworkStatus


    def get_zWave_network_isRunning(self):
        zWaveNetworkIsRunning = False

        self.homeAutomationServer.emit('get_zWave_network_isRunning', {}, namespace='/HomeAutomationServer')

        zWaveNetworkIsRunning = self.zWaveNetworkIsRunning
        
        return zWaveNetworkIsRunning


    def get_zWave_home_id(self):
        zWaveNetworkIsRunning = False

        self.homeAutomationServer.emit('get_zWave_home_id', {}, namespace='/HomeAutomationServer')

        zWaveHomeId = self.zWaveHomeId
        
        return zWaveHomeId


    def get_zWave_network_state(self):
        zWaveNetworkState = False

        self.homeAutomationServer.emit('get_zWave_network_state', {}, namespace='/HomeAutomationServer')

        zWaveNetworkState = self.zWaveNetworkState
        
        return zWaveNetworkState


    def get_zWave_network_isReady(self):
        zWaveNetworkIsReady = False

        self.homeAutomationServer.emit('get_zWave_network_isReady', {}, namespace='/HomeAutomationServer')

        zWaveNetworkIsReady = self.zWaveNetworkIsReady
        
        return zWaveNetworkIsReady


    def get_zWave_network_controller_path(self):
        zWaveNetworkControllerPath = False

        self.homeAutomationServer.emit('get_zWave_network_controller_path', {}, namespace='/HomeAutomationServer')

        zWaveNetworkControllerPath = self.zWaveNetworkControllerPath
        
        return zWaveNetworkControllerPath


    def get_zWave_config_folder_path(self):
        zwaveConfigFolderPath = False

        self.homeAutomationServer.emit('get_zWave_network_controller_path', {}, namespace='/HomeAutomationServer')

        zwaveConfigFolderPath = self.zwaveConfigFolderPath
        
        return zwaveConfigFolderPath


    def get_modules_list(self):
        modulesList = False

        self.homeAutomationServer.emit('get_modules_list', {}, namespace='/HomeAutomationServer')

        modulesList = self.modulesList
        
        return modulesList


    def get_module(self, moduleId):
        module = False

        self.homeAutomationServer.emit('get_module', {'moduleId': moduleId}, namespace='/HomeAutomationServer')

        for module in self.modulesList:
            if module.id == moduleId:
                module = module
                break
            else:
                module = False

        return module



    """ADD METHODS"""
    def add_zWave_module(self):
        succes = False

        if self.zwaveNetworkIsReady:
            self.homeAutomationServer.emit('add_zWave_module', {}, namespace='/HomeAutomationServer')
            succes = True
        else:
            succes = False

        return succes



    """DEL METHODS"""
    def del_zWave_module(self):
        succes = False

        if self.zwaveNetworkIsReady:
            self.homeAutomationServer.emit('del_zWave_module', {}, namespace='/HomeAutomationServer')
            succes = True
        else:
            succes = False

        return succes


    
    """SET METHODS"""
    def set_module_name(self, moduleId, newName):
        succes = False
        data = {}

        if self.running:
            if isinstance(moduleId, int) and isinstance(newName, str):
                data["moduleId"] = moduleId
                data["newName"] = newName
                self.homeAutomationServer.emit('set_module_name', data, namespace='/HomeAutomationServer')
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def set_module_location(self, moduleId, newLocation):
        succes = False
        data = {}

        if self.running:
            if isinstance(moduleId, int) and isinstance(newLocation, int):
                data["moduleId"] = moduleId
                data["newLocation"] = newLocation
                self.homeAutomationServer.emit('set_module_location', data, namespace='/HomeAutomationServer')
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def set_module_value(self, moduleId, valueId, newData):
        succes = False
        data = {}

        if self.running:
            if isinstance(moduleId, int) and isinstance(valueId, int):
                data["moduleId"] = moduleId
                data["valueId"] = valueId
                data["newData"] = newData
                self.homeAutomationServer.emit('set_module_value', data, namespace='/HomeAutomationServer')
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def set_light_controller_level(self, moduleId, newLevel):
        succes = False
        data = {}

        if self.running:
            if isinstance(moduleId, int) and isinstance(newLevel, int):
                data["moduleId"] = moduleId
                data["newLevel"] = newLevel
                self.homeAutomationServer.emit('set_light_controller_level', data, namespace='/HomeAutomationServer')
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def set_light_controller_color_by_label(self, moduleId, newColorLabel):
        succes = False
        data = {}

        if self.running:
            if isinstance(moduleId, int) and isinstance(newColorLabel, str):
                data["moduleId"] = moduleId
                data["newColorLabel"] = newColorLabel
                self.homeAutomationServer.emit('set_light_controller_color_by_label', data, namespace='/HomeAutomationServer')
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def set_light_controller_color_by_rgbw(self, moduleId, newRgbwValue):
        succes = False
        data = {}

        if self.running:
            if isinstance(moduleId, int) and isinstance(newRgbwValue, str):
                data["moduleId"] = moduleId
                data["newRgbwValue"] = newRgbwValue
                self.homeAutomationServer.emit('set_light_controller_color_by_rgbw', data, namespace='/HomeAutomationServer')
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    
    """SWITCH METHODS"""
    def switch_light_controller_on(self, moduleId):
        succes = False
        data = {}

        if self.running:
            if isinstance(moduleId, int):
                data["moduleId"] = moduleId
                self.homeAutomationServer.emit('switch_light_controller_on', data, namespace='/HomeAutomationServer')
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def switch_light_controller_off(self, moduleId):
        succes = False
        data = {}

        if self.running:
            if isinstance(moduleId, int):
                data["moduleId"] = moduleId
                self.homeAutomationServer.emit('switch_light_controller_off', data, namespace='/HomeAutomationServer')
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def switch_relay_on(self, moduleId):
        succes = False
        data = {}

        if self.running:
            if isinstance(moduleId, int):
                data["moduleId"] = moduleId
                self.homeAutomationServer.emit('switch_relay_on', data, namespace='/HomeAutomationServer')
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def switch_relay_off(self, moduleId):
        succes = False
        data = {}

        if self.running:
            if isinstance(moduleId, int):
                data["moduleId"] = moduleId
                self.homeAutomationServer.emit('switch_relay_off', data, namespace='/HomeAutomationServer')
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes



    """HEAL METHODS"""
    def heal_zWave_network(self):
        succes = False

        if self.zwaveNetworkIsReady:
            self.homeAutomationServer.emit('heal_zWave_network', {}, namespace='/HomeAutomationServer')
            succes = True
        else:
            succes = False

        return succes


    def heal_zWave_module(self, moduleId):
        succes = False
        data = {}

        if self.zwaveNetworkIsReady:
            if isinstance(moduleId, int):
                data["moduleId"] = moduleId
                self.homeAutomationServer.emit('heal_zWave_module', data, namespace='/HomeAutomationServer')
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes



    """DESTROY METHODS"""
    def destroy_zWave_network(self):
        succes = False

        if self.zwaveNetworkIsReady:
            self.homeAutomationServer.emit('destroy_zWave_network', {}, namespace='/HomeAutomationServer')
            succes = True
        else:
            succes = False

        return succes



    """UPDATE METHODS"""
    def update_zWave_module_return_route(self, moduleId):
        succes = False
        data = {}

        if self.zwaveNetworkIsReady:
            if isinstance(moduleId, int):
                data["moduleId"] = moduleId
                self.homeAutomationServer.emit('update_zWave_module_return_route', data, namespace='/HomeAutomationServer')
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def update_zWave_module_neighbors(self, moduleId):
        succes = False
        data = {}

        if self.zwaveNetworkIsReady:
            if isinstance(moduleId, int):
                data["moduleId"] = moduleId
                self.homeAutomationServer.emit('update_zWave_module_neighbors', data, namespace='/HomeAutomationServer')
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def update_zWave_module_network(self, moduleId):
        succes = False
        data = {}

        if self.zwaveNetworkIsReady:
            if isinstance(moduleId, int):
                data["moduleId"] = moduleId
                self.homeAutomationServer.emit('update_zWave_module_network', data, namespace='/HomeAutomationServer')
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes



    """REFRESH METHODS"""
    def refresh_zWave_module_informations(self, moduleId):
        succes = False
        data = {}

        if self.zwaveNetworkIsReady:
            if isinstance(moduleId, int):
                data["moduleId"] = moduleId
                self.homeAutomationServer.emit('refresh_zWave_module_informations', data, namespace='/HomeAutomationServer')
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def refresh_zWave_module_value(self, moduleId, valueId):
        succes = False
        data = {}

        if self.zwaveNetworkIsReady:
            if isinstance(moduleId, int) and isinstance(valueId, int):
                data["moduleId"] = moduleId
                data["valueId"] = valueId
                self.homeAutomationServer.emit('refresh_zWave_module_value', data, namespace='/HomeAutomationServer')
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def refresh_zWave_module_values(self, moduleId):
        succes = False
        data = {}

        if self.zwaveNetworkIsReady:
            if isinstance(moduleId, int):
                data["moduleId"] = moduleId
                self.homeAutomationServer.emit('refresh_zWave_module_values', data, namespace='/HomeAutomationServer')
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes



    """RESET METHODS"""
    def soft_reset_zWave_network(self):
        succes = False
        data = {}

        if self.zwaveNetworkIsReady:
            self.homeAutomationServer.emit('soft_reset_zWave_network', data, namespace='/HomeAutomationServer')
            succes = True
        else:
            succes = False

        return succes


    def hard_reset_zWave_network(self):
        succes = False
        data = {}

        if self.zwaveNetworkIsReady:
            self.homeAutomationServer.emit('hard_reset_zWave_network', data, namespace='/HomeAutomationServer')
            succes = True
        else:
            succes = False

        return succes



    """ACTIVATION METHODS"""
    def activate_zWave_network(self):
        succes = False
        data = {}

        if self.zwaveNetworkIsReady:
            self.homeAutomationServer.emit('activate_zWave_network', data, namespace='/HomeAutomationServer')
            succes = True
        else:
            succes = False

        return succes


    def deactivate_zWave_network(self):
        succes = False
        data = {}

        if self.zwaveNetworkIsReady:
            self.homeAutomationServer.emit('deactivate_zWave_network', data, namespace='/HomeAutomationServer')
            succes = True
        else:
            succes = False

        return succes



    """START METHODS"""
    def start_zWave_network(self):
        succes = False
        data = {}

        if self.zwaveNetworkIsReady:
            self.homeAutomationServer.emit('start_zWave_network', data, namespace='/HomeAutomationServer')
            succes = True
        else:
            succes = False

        return succes


    def start_home_automation_engine(self):
        succes = False
        data = {}

        if self.zwaveNetworkIsReady:
            self.homeAutomationServer.emit('start_home_automation_engine', data, namespace='/HomeAutomationServer')
            succes = True
        else:
            succes = False

        return succes



    """STOP METHODS"""
    def stop_zWave_network(self):
        succes = False
        data = {}

        if self.zwaveNetworkIsReady:
            self.homeAutomationServer.emit('stop_zWave_network', data, namespace='/HomeAutomationServer')
            succes = True
        else:
            succes = False

        return succes


    def stop_home_automation_engine(self):
        succes = False
        data = {}

        if self.zwaveNetworkIsReady:
            self.homeAutomationServer.emit('stop_home_automation_engine', data, namespace='/HomeAutomationServer')
            succes = True
        else:
            succes = False

        return succes



    """RESTART METHODS"""
    def restart_zWave_network(self):
        succes = False
        data = {}

        if self.zwaveNetworkIsReady:
            self.homeAutomationServer.emit('restart_zWave_network', data, namespace='/HomeAutomationServer')
            succes = True
        else:
            succes = False

        return succes


    def restart_home_automation_engine(self):
        succes = False
        data = {}

        if self.zwaveNetworkIsReady:
            self.homeAutomationServer.emit('restart_home_automation_engine', data, namespace='/HomeAutomationServer')
            succes = True
        else:
            succes = False

        return succes



    """UPDATED METHODS"""
    def home_automation_engine_updated(self, newHomeAutomationEngineInformation):
        succes = False

        try:
            self.running = newHomeAutomationEngineInformation['running']
            succes = True
        except Exception as e:
            succes = False
            
        return succes


    def zWave_network_updated(self, newZwaveNetworkInformations):
        succes = False

        try:
            self.zWaveNetworkStatus = newZwaveNetworkInformations['zWaveNetworkStatus']
            self.zWaveNetworkIsRunning = newZwaveNetworkInformations['zWaveNetworkIsRunning']
            self.zWaveHomeId = newZwaveNetworkInformations['zWaveHomeId']
            self.zWaveNetworkState = newZwaveNetworkInformations['zWaveNetworkState']
            self.zwaveNetworkIsReady = newZwaveNetworkInformations['zwaveNetworkIsReady']
            self.zWaveNetworkControllerPath = newZwaveNetworkInformations['zWaveNetworkControllerPath']
            self.zwaveConfigFolderPath = newZwaveNetworkInformations['zwaveConfigFolderPath']
            
            succes = True
        except:
            succes = False

        return succes


    def modules_list_updated(self, modulesListData):
        tmpModulesList = succes = False
        modulesList = []

        try:
            tmpModulesList = modulesListData['modulesList']
        except:
            tmpModulesList = False

        if tmpModulesList != False:
            moduleId = moduleName = moduleLocation = moduleRole = moduleProtocol = False

            for moduleData in tmpModulesList:
                try: 
                    moduleId = moduleData["id"]
                    moduleName = moduleData["name"]
                    moduleLocation = moduleData['location']
                    moduleRole = moduleData["role"]
                    moduleProtocol = moduleData["protocol"]

                    succes = True
                except Exception as e:
                    succes = False

                if succes:
                    if moduleData['protocol'] == 'zWave':
                        moduleValues = moduleParametters = moduleManufacturerName = moduleProductName = False
                        moduleDeviceType = moduleCanWakeUp = moduleIsAwake = moduleIsFailed = False
                        moduleIsReady = moduleIsSleeping = moduleBatteryLevel = moduleCommandClassAsString = False

                        tmpModuleValues = tmpModuleParametters = False

                        valueId = valueLabel = valueData = valueDataItems = valueNetworkId = valueMax = valueMin = False
                        valueNodeId = valueType = ValueUnits = False

                        parametterId = parametterLabel = parametterData = parametterDataItems = False
                        parametterNetworkId = parametterMax = parametterMin = False
                        parametterNodeId = parametterType = parametterUnits = False

                        moduleValues = moduleParametters = []

                        try:
                            tmpModuleValues = moduleData['values']
                            tmpModuleParametters = moduleData['parametters']

                            for value in tmpModuleValues:
                                moduleValues = []

                                try:
                                    valueId = value['id']
                                    valueLabel = value['label']
                                    valueData = value['data']
                                    valueDataItems = value['dataItems']
                                    valueNetworkId = value['networkId']
                                    valueMax = value['max']
                                    valueMin = value['min']
                                    valueNodeId = value['nodeId']
                                    valueType = value['type']
                                    ValueUnits = value["units"]
                                    moduleValues.append(ZWaveValue(valueId, valueLabel, valueData, valueDataItems, valueNetworkId, valueMax, valueMin, valueNodeId, valueType, ValueUnits))

                                except:
                                    succes = False
                                    break
                                
                            for parametter in tmpModuleParametters:
                                moduleParametters = []

                                try:
                                    parametterId = parametter['id']
                                    parametterLabel = parametter['label']
                                    parametterData = parametter['data']
                                    parametterDataItems = parametter['dataItems']
                                    parametterNetworkId = parametter['networkId']
                                    parametterMax = parametter['max']
                                    parametterMin = parametter['min']
                                    parametterNodeId = parametter['nodeId']
                                    parametterType = parametter['type']
                                    parametterUnits = parametter["units"]

                                    moduleParametters.append(ZWaveParametter(parametterId, parametterLabel, parametterData, parametterDataItems, parametterNetworkId, parametterMax, parametterMin, parametterNodeId, parametterType, parametterUnits))

                                except:
                                    succes = False
                                    break

                                
                            moduleManufacturerName = moduleData['manufacturerName']
                            moduleProductName = moduleData['productName']
                            moduleProductType = moduleData['productType']
                            moduleDeviceType = moduleData["deviceType"]
                            moduleType = moduleData["type"]
                            moduleCanWakeUp = moduleData['canWakeUp']
                            moduleIsAwake = moduleData['isAwake']
                            moduleIsFailed = moduleData['isFailed']
                            moduleIsReady = moduleData['isReady']
                            moduleIsSleeping = moduleData['isSleeping']
                            moduleBatteryLevel = moduleData['batteryLevel']
                            moduleCommandClassAsString = moduleData['commandClassAsString']

                            succes = True
                        except Exception as e:
                            print(e)
                            succes = False

                        if succes:
                            if moduleData['role'] == 'relay':
                                relayState = False
                                        
                                try:
                                    relayState = moduleData['state']
                                    module = ZWaveRelay(moduleId, moduleName, moduleLocation, moduleRole, moduleValues, moduleParametters, moduleManufacturerName, moduleProductName, moduleProductType, moduleDeviceType, moduleType, moduleCanWakeUp, moduleIsAwake, moduleIsFailed, moduleIsReady, moduleIsSleeping, moduleBatteryLevel, moduleCommandClassAsString, relayState)
                                
                                    succes = True
                                except:
                                    succes = False

                                
                            elif moduleData['role'] == 'light controller' or moduleData['role'] == 'color light controller':
                                lightControllerLevel = lightControllerLightUp = lightControllerMaxLevel = lightControllerMinLevel = lightControllerStartLevel = False

                                try:        
                                    lightControllerLevel = moduleData['level']
                                    lightControllerLightUp = moduleData['lightUp']
                                    lightControllerMaxLevel = moduleData['maxLevel']
                                    lightControllerMinLevel = moduleData['minLevel']
                                    lightControllerStartLevel = moduleData['startLevel']

                                    if moduleData['role'] == 'color light controller':
                                        lightControllerColorLabel = lightControllerColorValue = lightControllerColorPalette = False
                                        lightControllerColorLabel = moduleData["colorLabel"]
                                        lightControllerColorValue = moduleData["colorValue"]
                                        lightControllerColorPalette = moduleData["colorPalette"]

                                        module = ZWaveColorLightController(moduleId, moduleName, moduleLocation, moduleRole, moduleValues, moduleParametters, moduleManufacturerName, moduleProductName, moduleProductType, moduleDeviceType, moduleType, moduleCanWakeUp, moduleIsAwake, moduleIsFailed, moduleIsReady, moduleIsSleeping, moduleBatteryLevel, moduleCommandClassAsString, lightControllerLevel, lightControllerLightUp, lightControllerMaxLevel, lightControllerMinLevel, lightControllerStartLevel, lightControllerColorLabel, lightControllerColorValue, lightControllerColorPalette)                       
                                        succes = True  

                                    else:
                                        module = ZWaveLightController(moduleId, moduleName, moduleLocation, moduleRole, moduleValues, moduleParametters, moduleManufacturerName, moduleProductName, moduleProductType, moduleDeviceType, moduleType, moduleCanWakeUp, moduleIsAwake, moduleIsFailed, moduleIsReady, moduleIsSleeping, moduleBatteryLevel, moduleCommandClassAsString, lightControllerLevel, lightControllerLightUp, lightControllerMaxLevel, lightControllerMinLevel, lightControllerStartLevel)                    
                                        succes = True
                                except Exception as e:
                                    print(e)
                                    succes = False

                            elif moduleData['role'] == 'sensor':
                                tmpSubSensors = False
                                subSensorsList = []

                                try:
                                    tmpSubSensors = moduleData['sensors']
                                    succes = True
                                except:
                                    succes = False

                                for sensor in tmpSubSensors:
                                    if sensor['role'] == "temperature sensor":
                                        temperature = False

                                        try:
                                            temperature = sensor["temperature"]
                                            subSensorsList.append(ZWaveTemperatureSensor(moduleId, moduleName, moduleLocation, moduleRole, moduleValues, moduleParametters, moduleManufacturerName, moduleProductName, moduleProductType, moduleDeviceType, moduleType, moduleCanWakeUp, moduleIsAwake, moduleIsFailed, moduleIsReady, moduleIsSleeping, moduleBatteryLevel, moduleCommandClassAsString, temperature))
                                            
                                            succes = True
                                        except:
                                            succes = False
                                            break

                                        
                                    elif sensor['role'] == "motion sensor":
                                        try:
                                            subSensorsList.append(ZWaveMotionSensor(moduleId, moduleName, moduleLocation, moduleRole, moduleValues, moduleParametters, moduleManufacturerName, moduleProductName, moduleProductType, moduleDeviceType, moduleType, moduleCanWakeUp, moduleIsAwake, moduleIsFailed, moduleIsReady, moduleIsSleeping, moduleBatteryLevel, moduleCommandClassAsString))
                                            succes = True
                                        except:
                                            succes = False
                                            break

                                    elif sensor['role'] == "luminance sensor":
                                        luminance = False

                                        try:
                                            luminance = sensor["temperature"]
                                            subSensorsList.append(ZWaveTemperatureSensor(moduleId, moduleName, moduleLocation, moduleRole, moduleValues, moduleParametters, moduleManufacturerName, moduleProductName, moduleProductType, moduleDeviceType, moduleType, moduleCanWakeUp, moduleIsAwake, moduleIsFailed, moduleIsReady, moduleIsSleeping, moduleBatteryLevel, moduleCommandClassAsString, luminance))
                                            succes = True
                                        except:
                                            succes = False
                                            break
                                                
                                    elif sensor['role'] == "acces control sensor":
                                        accesState = False

                                        try:
                                            accesState = sensor['accesState']
                                            subSensorsList.append(ZWaveAccesControlSensor(moduleId, moduleName, moduleLocation, moduleRole, moduleValues, moduleParametters, moduleManufacturerName, moduleProductName, moduleProductType, moduleDeviceType, moduleType, moduleCanWakeUp, moduleIsAwake, moduleIsFailed, moduleIsReady, moduleIsSleeping, moduleBatteryLevel, moduleCommandClassAsString, accesState))
                                            succes = True
                                        except:
                                            succes = False
                                            break           
                                    else:
                                        pass

                                if succes:
                                    module = ZWaveSensor(moduleId, moduleName, moduleLocation, moduleRole, moduleValues, moduleParametters, moduleManufacturerName, moduleProductName, moduleProductType, moduleDeviceType, moduleType, moduleCanWakeUp, moduleIsAwake, moduleIsFailed, moduleIsReady, moduleIsSleeping, moduleBatteryLevel, moduleCommandClassAsString, subSensorsList)
                                else:
                                    module = False 
                            else:
                                if succes:
                                    module = ZWaveModule(moduleId, moduleName, moduleLocation, moduleRole, moduleValues, moduleParametters, moduleManufacturerName, moduleProductName, moduleProductType, moduleDeviceType, moduleType, moduleCanWakeUp, moduleIsAwake, moduleIsFailed, moduleIsReady, moduleIsSleeping, moduleBatteryLevel, moduleCommandClassAsString)
                                else:
                                    succes = False
                        else:
                            module = False
                    else:
                        if succes:
                            module = Module(moduleId, moduleName, moduleLocation, moduleRole, moduleProtocol)
                        else:
                            module = False
                else:
                    module = False
            
                if module != False:
                    modulesList.append(module)
                else:
                    succes = False
                    break
            
        else:
            succes = False


        if succes:
            self.modulesList = modulesList
        else:
            pass

        return succes


    def module_updated(self, moduleData):
        succes = module = False
        moduleId = moduleName = moduleLocation = moduleRole = moduleProtocol = False

        try: 
            moduleId = module["id"]
            moduleName = module["name"]
            moduleLocation = module['location']
            moduleRole = module["role"]
            moduleProtocol = module["protocol"]

            succes = True
        except:
            succes = False

        if succes:
            if moduleData['protocol'] == 'zWave':
                moduleValues = moduleParametters = moduleManufacturerName = moduleProductName = False
                moduleDeviceType = moduleCanWakeUp = moduleIsAwake = moduleIsFailed = False
                moduleIsReady = moduleIsSleeping = moduleBatteryLevel = moduleCommandClassAsString = False

                tmpModuleValues = tmpModuleParametters = False

                valueId = valueLabel = valueData = valueDataItems = valueNetworkId = valueMax, valueMin = False
                valueNodeId = valueType = ValueUnits = False

                parametterId = parametterLabel = parametterData = parametterDataItems = False
                parametterNetworkId = parametterMax, parametterMin = False
                parametterNodeId = parametterType = parametterUnits = False

                moduleValues = moduleParametters = []

                try:
                    tmpModuleValues = module['values']
                    tmpModuleParametters = module['parametters']

                    for value in tmpModuleValues:
                        moduleValues = []

                        try:
                            valueId = value['id']
                            valueLabel = value['label']
                            valueData = value['data']
                            valueDataItems = value['dataItems']
                            valueNetworkId = value['networkId']
                            valueMax = value['max']
                            valueMin = value['min']
                            valueNodeId = value['nodeId']
                            valueType = value['type']
                            ValueUnits = value["units"]

                            moduleValues.append(ZWaveValue(valueId, valueLabel, valueData, valueDataItems, valueNetworkId, valueMax, valueMin, valueNodeId, valueType, ValueUnits))

                        except:
                            succes = False
                            break
                        
                    for parametter in tmpModuleParametters:
                        moduleParametters = []

                        try:
                            parametterId = parametter['id']
                            parametterLabel = parametter['label']
                            parametterData = parametter['data']
                            parametterDataItems = parametter['dataItems']
                            parametterNetworkId = parametter['networkId']
                            parametterMax = parametter['max']
                            parametterMin = parametter['min']
                            parametterNodeId = parametter['nodeId']
                            parametterType = parametter['type']
                            parametterUnits = parametter["units"]

                            moduleParametters.append(ZWaveParametter(parametterId, parametterLabel, parametterData, parametterDataItems, parametterNetworkId, parametterMax, parametterMin, parametterNodeId, parametterType, parametterUnits))

                        except:
                            succes = False
                            break

                        
                        moduleManufacturerName = moduleData['manufacturerName']
                        moduleProductName = moduleData['productName']
                        moduleProductType = moduleData['productType']
                        moduleDeviceType = moduleData["deviceType"]
                        moduleType = moduleData["type"]
                        moduleCanWakeUp = moduleData['canWakeUp']
                        moduleIsAwake = moduleData['isAwake']
                        moduleIsFailed = moduleData['isFailed']
                        moduleIsReady = moduleData['isReady']
                        moduleIsSleeping = moduleData['isSleeping']
                        moduleBatteryLevel = moduleData['batteryLevel']
                        moduleCommandClassAsString = moduleData['commandClassAsString']

                    succes = True
                except:
                    succes = False

                if succes:
                    if moduleData['role'] == 'relay':
                        relayState = False
                                
                        try:
                            relayState = moduleData['state']
                            module = ZWaveRelay(moduleId, moduleName, moduleLocation, moduleRole, moduleValues, moduleParametters, moduleManufacturerName, moduleProductName, moduleProductType, moduleDeviceType, moduleType, moduleCanWakeUp, moduleIsAwake, moduleIsFailed, moduleIsReady, moduleIsSleeping, moduleBatteryLevel, moduleCommandClassAsString, relayState)
                        
                            succes = True
                        except:
                            succes = False

                        
                    elif moduleData['role'] == 'light controller' or moduleData['role'] == 'color light controller':
                        lightControllerLevel = lightControllerLightUp = lightControllerMaxLevel = lightControllerMinLevel = lightControllerStartLevel = False

                        try:        
                            lightControllerLevel = moduleData['level']
                            lightControllerLightUp = moduleData['lightUp']
                            lightControllerMaxLevel = moduleData['maxLevel']
                            lightControllerMinLevel = moduleData['minLevel']
                            lightControllerStartLevel = moduleData['startLevel']

                            if moduleData['role'] == 'color light controller':
                                lightControllerColorLabel = lightControllerColorValue = lightControllerColorPalette = False
                                lightControllerColorLabel = moduleData["colorLabel"]
                                lightControllerColorValue = moduleData["colorValue"]
                                lightControllerColorPalette = moduleData["colorPalette"]

                                module = ZWaveColorLightController(moduleId, moduleName, moduleLocation, moduleRole, moduleValues, moduleParametters, moduleManufacturerName, moduleProductName, moduleProductType, moduleDeviceType, moduleType, moduleCanWakeUp, moduleIsAwake, moduleIsFailed, moduleIsReady, moduleIsSleeping, moduleBatteryLevel, moduleCommandClassAsString, lightControllerLevel, lightControllerLightUp, lightControllerMaxLevel, lightControllerMinLevel, lightControllerStartLevel, lightControllerColorLabel, lightControllerColorValue, lightControllerColorPalette)                       
                                succes = True  

                            else:
                                module = ZWaveLightController(moduleId, moduleName, moduleLocation, moduleRole, moduleValues, moduleParametters, moduleManufacturerName, moduleProductName, moduleProductType, moduleDeviceType, moduleType, moduleCanWakeUp, moduleIsAwake, moduleIsFailed, moduleIsReady, moduleIsSleeping, moduleBatteryLevel, moduleCommandClassAsString, lightControllerLevel, lightControllerLightUp, lightControllerMaxLevel, lightControllerMinLevel, lightControllerStartLevel)                    
                                succes = True
                        except:
                            succes = False

                    elif moduleData['role'] == 'sensor':
                        tmpSubSensors = False
                        subSensorsList = []

                        try:
                            tmpSubSensors = moduleData['sensors']
                            succes = True
                        except:
                            succes = False

                        for sensor in tmpSubSensors:
                            if sensor['role'] == "temperature sensor":
                                temperature = False

                                try:
                                    temperature = sensor["temperature"]
                                    subSensorsList.append(ZWaveTemperatureSensor(moduleId, moduleName, moduleLocation, moduleRole, moduleValues, moduleParametters, moduleManufacturerName, moduleProductName, moduleProductType, moduleDeviceType, moduleType, moduleCanWakeUp, moduleIsAwake, moduleIsFailed, moduleIsReady, moduleIsSleeping, moduleBatteryLevel, moduleCommandClassAsString, temperature))
                                    
                                    succes = True
                                except:
                                    succes = False
                                    break

                                
                            elif sensor['role'] == "motion sensor":
                                try:
                                    subSensorsList.append(ZWaveMotionSensor(moduleId, moduleName, moduleLocation, moduleRole, moduleValues, moduleParametters, moduleManufacturerName, moduleProductName, moduleProductType, moduleDeviceType, moduleType, moduleCanWakeUp, moduleIsAwake, moduleIsFailed, moduleIsReady, moduleIsSleeping, moduleBatteryLevel, moduleCommandClassAsString))
                                    succes = True
                                except:
                                    succes = False
                                    break

                            elif sensor['role'] == "luminance sensor":
                                luminance = False

                                try:
                                    luminance = sensor["temperature"]
                                    subSensorsList.append(ZWaveTemperatureSensor(moduleId, moduleName, moduleLocation, moduleRole, moduleValues, moduleParametters, moduleManufacturerName, moduleProductName, moduleProductType, moduleDeviceType, moduleType, moduleCanWakeUp, moduleIsAwake, moduleIsFailed, moduleIsReady, moduleIsSleeping, moduleBatteryLevel, moduleCommandClassAsString, luminance))
                                    succes = True
                                except:
                                    succes = False
                                    break
                                         
                            elif sensor['role'] == "acces control sensor":
                                accesState = False

                                try:
                                    accesState = sensor['accesState']
                                    subSensorsList.append(ZWaveAccesControlSensor(moduleId, moduleName, moduleLocation, moduleRole, moduleValues, moduleParametters, moduleManufacturerName, moduleProductName, moduleProductType, moduleDeviceType, moduleType, moduleCanWakeUp, moduleIsAwake, moduleIsFailed, moduleIsReady, moduleIsSleeping, moduleBatteryLevel, moduleCommandClassAsString, accesState))
                                    succes = True
                                except:
                                    succes = False
                                    break           
                            else:
                                pass

                        if succes:
                            module = ZWaveSensor(moduleId, moduleName, moduleLocation, moduleRole, moduleValues, moduleParametters, moduleManufacturerName, moduleProductName, moduleProductType, moduleDeviceType, moduleType, moduleCanWakeUp, moduleIsAwake, moduleIsFailed, moduleIsReady, moduleIsSleeping, moduleBatteryLevel, moduleCommandClassAsString, subSensorsList)
                        else:
                            module = False 
                    else:
                        if succes:
                            module = ZWaveModule(moduleId, moduleName, moduleLocation, moduleRole, moduleValues, moduleParametters, moduleManufacturerName, moduleProductName, moduleProductType, moduleDeviceType, moduleType, moduleCanWakeUp, moduleIsAwake, moduleIsFailed, moduleIsReady, moduleIsSleeping, moduleBatteryLevel, moduleCommandClassAsString)
                        else:
                            succes = False
                else:
                    module = False
            else:
                if succes:
                    module = Module(moduleId, moduleName, moduleLocation, moduleRole, moduleProtocol)
                else:
                    module = False
        else:
            module = False


        if module != False:
            for element in self.modulesList:
                if element.id == module.id:
                    element = module
                    succes = True
                    break
                else:
                    succes = False
        else:
            succes = False

        return succes
