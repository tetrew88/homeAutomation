import json
import sys

import time
import datetime

#openzwave import
import openzwave

from openzwave.node import ZWaveNode
from openzwave.value import ZWaveValue
from openzwave.scene import ZWaveScene
from openzwave.controller import ZWaveController

from openzwave.network import ZWaveNetwork
from openzwave.option import ZWaveOption


#dispatcher import
from pydispatch import dispatcher


#module import
from .zWaveModules.zWaveModule import *

from .zWaveModules.zWaveNetworkController import *

from .zWaveModules.zWaveLightControllers.zWaveLightController import *
from .zWaveModules.zWaveLightControllers.zWaveColorLightController import *

from .zWaveModules.zWaveSensors.zWaveSensor import *
from .zWaveModules.zWaveSensors.zWaveLuminanceSensor import *
from .zWaveModules.zWaveSensors.zWaveTemperatureSensor import *
from .zWaveModules.zWaveSensors.zWaveMotionSensor import *
from .zWaveModules.zWaveSensors.zWaveAccesControlSensor import *

from .zWaveModules.zWaveRelays.zWaveRelay import *


#module event import
from .zWaveEvents.zWaveModuleEvents.zWaveModuleEvent import *
from .zWaveEvents.zWaveModuleEvents.zWaveModuleHealed import *
from .zWaveEvents.zWaveModuleEvents.zWaveModuleInformationsRefreshed import *
from .zWaveEvents.zWaveModuleEvents.zWaveModuleMoved import *
from .zWaveEvents.zWaveModuleEvents.zWaveModuleNeighborsUpdated import *
from .zWaveEvents.zWaveModuleEvents.zWaveModuleReady import *
from .zWaveEvents.zWaveModuleEvents.zWaveModuleRenamed import *
from .zWaveEvents.zWaveModuleEvents.zWaveModuleReturnRouteUpdated import *
from .zWaveEvents.zWaveModuleEvents.zWaveModuleUpdated import *
from .zWaveEvents.zWaveModuleEvents.zWaveModuleValueModified import *
from .zWaveEvents.zWaveModuleEvents.zWaveModuleValueRefreshed import *
from .zWaveEvents.zWaveModuleEvents.zWaveModuleValuesUpdated import *
from .zWaveEvents.zWaveModuleEvents.zWaveModuleValueUpdated import *
from .zWaveEvents.zWaveModuleEvents.zWaveModuleNetworkUpdated import *

#sensors event
from .zWaveEvents.zWaveModuleEvents.zWaveSensorEvents.zWaveAccesControlEvents.zWaveAccesControlEvent import *
from .zWaveEvents.zWaveModuleEvents.zWaveSensorEvents.zWaveAccesControlEvents.zWaveAccesOpened import *
from .zWaveEvents.zWaveModuleEvents.zWaveSensorEvents.zWaveAccesControlEvents.zWaveAccesClosed import *
from .zWaveEvents.zWaveModuleEvents.zWaveSensorEvents.zWaveMotionDetection import *

#light controller event
from .zWaveEvents.zWaveModuleEvents.zWaveLightEvents.zWaveLightEvent import*
from .zWaveEvents.zWaveModuleEvents.zWaveLightEvents.zWaveLightSettingOn import *
from .zWaveEvents.zWaveModuleEvents.zWaveLightEvents.zWaveLightSettingOff import *
from .zWaveEvents.zWaveModuleEvents.zWaveLightEvents.zWaveLightIntensityModified import *
from .zWaveEvents.zWaveModuleEvents.zWaveLightEvents.zWaveLightColorModified import *

#relay event
from .zWaveEvents.zWaveModuleEvents.zWaveRelayEvents.zWaveRelayEvent import *
from .zWaveEvents.zWaveModuleEvents.zWaveRelayEvents.zWaveRelaySettingOn import *
from .zWaveEvents.zWaveModuleEvents.zWaveRelayEvents.zWaveRelaySettingOff import *


#network event import
from .zWaveEvents.zWaveNetworkEvents.zWaveNetworkUpdated import *
from .zWaveEvents.zWaveNetworkEvents.zWaveNetworkModulesListUpdated import *
from .zWaveEvents.zWaveNetworkEvents.zWaveNetworkEvent import *
from .zWaveEvents.zWaveNetworkEvents.zWaveNetworkActivated import *
from .zWaveEvents.zWaveNetworkEvents.zWaveNetworkAwaked import *
from .zWaveEvents.zWaveNetworkEvents.zWaveNetworkDeactivated import *
from .zWaveEvents.zWaveNetworkEvents.zWaveNetworkDestroyed import *
from .zWaveEvents.zWaveNetworkEvents.zWaveNetworkFailed import *
from .zWaveEvents.zWaveNetworkEvents.zWaveNetworkHardResetted import *
from .zWaveEvents.zWaveNetworkEvents.zWaveNetworkHealed import *
from .zWaveEvents.zWaveNetworkEvents.zWaveNetworkModuleAdded import *
from .zWaveEvents.zWaveNetworkEvents.zWaveNetworkModuleRemoved import *
from .zWaveEvents.zWaveNetworkEvents.zWaveNetworkReady import *
from .zWaveEvents.zWaveNetworkEvents.zWaveNetworkResetted import *
from .zWaveEvents.zWaveNetworkEvents.zWaveNetworkSoftResetted import *
from .zWaveEvents.zWaveNetworkEvents.zWaveNetworkStarted import *
from .zWaveEvents.zWaveNetworkEvents.zWaveNetworkStopped import *


#controller event
from .zWaveEvents.zWaveControllerEvents.zWaveControllerEvent import *
from .zWaveEvents.zWaveControllerEvents.zWaveControllerReady import *
from .zWaveEvents.zWaveControllerEvents.zWaveControllerFailed import *
from .zWaveEvents.zWaveControllerEvents.zWaveControllerRemoved import *
from .zWaveEvents.zWaveControllerEvents.zWaveControllerResetted import *



class Network:
    """
        class bringing all the information and functionality of the zwave network.
            Attributes:
                logPath: path to the log file
                configFilePath: path to the config file
                running: booleean allows to know if the network running
                
                network: zwaveNetwork

                event list: list of event class

            Property:
                homeId: identifiant of the residence (zwave security)
                state: state of the network
                isReady: boolean allow to know if network is ready
                controller: controller of the network

                controllerPath: path to the controller ("/dev/...")
                zwaveConfigFolderPath: path to the zwave config folder

                modulesList: list of module connected on the network

            Methods:
                base methods:
                    load: Method used for connect network interaction with zwave signal
                    start: method used for start the network
                    stop: method used for stop the network
                    save_modification: method used for save modification on the network
                    restart: method used for restart the network

                get methods:
                    get_module: method used for getting an precise module

                add methods:
                    add_module: method used for adding an module on the network

                del methods:
                    del_module: method used for deletting an module of the network

                set methods:
                    set_module_name: method used for modify the name of an node
                    set_module_location: method used for modify the location of an node
                    set_module_value: method used for modify an value of an module
                    set_light_controller_level: method used for modify the level of an light controller (intensity)
                    set_light_controller_color_by_label: method used for modify the color of an color light controller by label(name) of the color
                    set_light_controller_color_by_rgbw: method used for modify the color of an color light controller by rgbw value of the color

                switch methods:
                    #light controller switches
                    switch_light_controller: method used for switch the state of an light controller (on/off)
                    switch_light_controller_on: method used for switch an light controller on
                    switch_light_controller_off: method used for switch an light controller off

                    #relay switches
                    switch_relay: method used for switch the state of an module
                    switch_relay_on: method used for switch an relay on
                    switch_relay_off: method used for switch an relay off

                heal methods:
                    heal_network: method use for heal the network
                    heal_module: method used for heal an module

                destroy methods:
                    destroy network: method used for destroy the network

                update methods:
                    update_module_return_route: method used for update the return route of an module
                    update_module_neighbors: method called for update an module neighbors
                    update_module_network: method used for update the network of an module

                refresh methods:
                    refresh_module_info: method called for update the information of an module
                    refresh_module_value: method called for update an value of an module
                    refresh_module_values: method called for update all value of an module

                reset methods:
                    soft_reset_network: method called for soft reset network
                    hard_reset_network: method called for hard reset network

                serialize methods:
                    serialize method used for serialize the class


            network interaction:
                succes network establishement:
                    network_started: call when the network was succesfully started
                    network_ready: call when network was ready
                    network_awake: call when network was awake
                
                error network establishement:
                    network_failed: call when network as failed

                network stop/reset:
                    network_stopped: call when network was stopped
                    network_resetted: call when network was resetted

                driver succes:
                    driver_ready: call when driver of network or of an module was ready
    
                driver error:
                    driver_failed: call when driver of network or of an module has failed
                    driver_removed: call when driver of network or of an module has been removed

                driver reset:
                    driver_resetted: call when driver of network or of an module has been resetted
    
                module interaction:
                    base interaction:
                        node_added: call when an module was added to the network
                        node_removed: call when an module was removed of the network
                        node_ready: call when an module is ready
                    
                    value interaction:
                        value_changed: call when an value of an module was modificated
                        
                event:
                    sensor event:
                        motion_detection_event: call when an motion detection sensor was triggered
                        acces_open: call when an acces was openned(door)
                        acces_close: call when an acces was closed(door)

                    light event:
                        light_turning_on: call when an light was turnning on
                        light_turning_off: call when an light was turnong off
                        light_color_modified: call when the color of an light was modified
                        light_intensity_modified: call when the intensity of an light was modified

                    relay event:
                        relay_setting_on: call when an relay was setting on
                        relay_setting_off: call when an relay was setting off
    
            ToDO:
    
    """



    def __init__(self, scriptPath, server=False):
        """constructor"""

        self.logPath = "log.log"
        self.configFilePath = scriptPath + "/configs/zWaveNetworkConfig.json"
        self.scriptPath = scriptPath
        
        self.running = False

        self.network = False
        self.eventList = []

        self.server = server



    ###PROPERTY###
    @property
    def status(self):
        """
            property allows to know if the zwave Network was enabled or disabled
        """

        data = status = False
        
        try:
            with open(self.configFilePath) as configurationFile:
                data = json.load(configurationFile)
                status = str(data["status"])
        except:
            status = False

        return status


    @property
    def networkConfigured(self):
        networkConfigured = False

        try:
            with open(self.configFilePath) as configurationFile:
                data = json.load(configurationFile)
                networkConfigured = bool(data["networkConfigured"])
        except:
            networkConfigured = False

        return networkConfigured


    @property
    def homeId(self):
        """
            property representing the home identifier
                return: int
        """

        homeId = False

        if isinstance(self.network, ZWaveNetwork):
            try:
                homeId = self.network.home_id
            except:
                homeId = False
        else:
            homeId = False

        return homeId


    @property
    def state(self):
        """
            property representing the state of the network

                STATE_STOPPED = 0, 
                STATE_FAILED = 1, 
                STATE_RESETTED = 3, 
                STATE_STARTED = 5, 
                STATE_AWAKED = 7, 
                STATE_READY = 10

                return: 
                    if succes return state(int)
                    else return false
        """

        state = False
        
        if isinstance(self.network, ZWaveNetwork):
            try:
                state = int(self.network.state)
            except:
                state = False
        else:
            state = False

        return state


    @property
    def strState(self):
        state = strState = False

        state = self.state

        if state != False:
            if state == 0:
                strState = "stopped"
            elif state == 1:
                strState = "failed"
            elif state == 3:
                strState == "resetted"
            elif state == 5:
                strState = "started"
            elif state == 7:
                strState = "awaked"
            elif state == 10:
                strState = "ready"
            else:
                strState = "error"
        else:
            strState = False

        return strState


    @property
    def isReady(self):
        """
            property representing if the network is ready or not
                return: False/True
        """

        isReady = False
        
        if isinstance(self.network, ZWaveNetwork):
            try:
                isReady = self.network.is_ready
            except:
                isReady = False
        else:
            isReady = False

        return isReady


    @property
    def controller(self):
        """
            property representing the main controller of the network.
                return:
                    if succes return zwaveController
                    else return False
        """

        controller = False
        
        if isinstance(self.network, ZWaveNetwork):
            try:
                controller = ZWaveNetworkController(self.network.controller)
            except:
                controller = False
        else:
            controller = False

        return controller


    @property
    def controllerPath(self):
        """
            used for get the zwave controller path in the config file
                return:
                    path of the controller
        """

        controllerPath = False
        
        try:
            with open(self.configFilePath) as configurationFile:
                data = json.load(configurationFile)
                controllerPath = data["assignedZwaveControllerPath"]
        except:
            controllerPath = False

        return controllerPath


    @property
    def zwaveConfigFolderPath(self):
        """
            used for get the zwave config folder path in the config file
                return:
                    path of the controller
        """

        zwaveConfigFolderPath = False

        try:
            with open(self.configFilePath) as configurationFile:
                data = json.load(configurationFile)
                zwaveConfigFolderPath = data["zWaveConfigFolderPath"]
        except:
            zwaveConfigFolderPath = False

        return zwaveConfigFolderPath


    @property
    def modulesList(self):
        """
            method used for list modules contained on the network.
                functionning:
                    asks to the automation network to list the node contained in
                        transtype each node to his associated class
                return:
                    list of modules classe
        """

        modulesList = []

        if isinstance(self.network, ZWaveNetwork) and self.isReady:
            try: 
                for node in self.network.nodes.values():
                    #NETWORK CONTROLLER
                    if node.node_id == self.controller.id:
                        try:
                            modulesList.append(self.controller)
                        except:
                            pass

                    #LIGHT CONTROLLER
                    elif node.type.lower() == 'light dimmer switch' or node.device_type.lower() == 'light dimmer switch':
                        if 'COMMAND_CLASS_COLOR' in node.command_classes_as_string:
                            try:
                                modulesList.append(ZWaveColorLightController(node))
                            except:
                                pass
                        else:
                            try:
                                modulesList.append(ZWaveLightController(node))
                            except:
                                pass

                    #RELAY
                    elif 'power switch' in node.type.lower() or 'power switch' in node.device_type.lower():
                        try:
                            modulesList.append(ZWaveRelay(node))
                        except:
                            pass

                    #SENSOR
                    elif "sensor" in node.type.lower() or "sensor" in node.device_type.lower():
                        tmpSensorList = []
                        sensors = {}

                        nodeValues = node.get_values(class_id='All', genre='All', type='All', readonly='All', writeonly='All', index='All', label='All')

                        if "motion sensor" in node.product_name.lower():
                            tmpSensorList.append(ZWaveMotionSensor(node))

                        for value in nodeValues:
                            if nodeValues[value].label.lower() == "temperature":
                                try:
                                    tmpSensorList.append(ZWaveTemperatureSensor(node))
                                except:
                                    pass
                            elif nodeValues[value].label.lower() == "luminance":
                                try:
                                    tmpSensorList.append(ZWaveLuminanceSensor(node))
                                except:
                                    pass
                            elif nodeValues[value].label.lower() == "access control":
                                try:
                                    tmpSensorList.append(ZWaveAccesControlSensor(node))
                                except:
                                    pass
                            else:
                                pass

                        for tmpSensor in tmpSensorList:
                            sensors[tmpSensor.role] = tmpSensor

                        try:
                            modulesList.append(ZWaveSensor(node, sensors))
                        except:
                            pass

                    #MODULE(else)
                    else:
                        try:
                            modulesList.append(ZWaveModule(node))
                        except:
                            pass
            
            except:
                modulesList = []
        else:
            modulesList = []

        return modulesList



    ###METHODS###
    """BASE METHOD"""
    def load(self):
        """
            Method used for connect network interaction with zwave signal

            return:
                if succes return TRUE 
                else return false
        """

        succes = False
        
        if isinstance(self.network, ZWaveNetwork):
            try:
                dispatcher.connect(self.network_started, self.network.SIGNAL_NETWORK_STARTED)
                dispatcher.connect(self.network_ready, self.network.SIGNAL_NETWORK_READY)
                dispatcher.connect(self.network_awake, self.network.SIGNAL_NETWORK_AWAKED)
                
                dispatcher.connect(self.network_failed, self.network.SIGNAL_NETWORK_FAILED)
                dispatcher.connect(self.network_stopped, self.network.SIGNAL_NETWORK_STOPPED)
                dispatcher.connect(self.network_resetted, self.network.SIGNAL_NETWORK_RESETTED)

                dispatcher.connect(self.driver_ready, self.network.SIGNAL_DRIVER_READY)
                dispatcher.connect(self.driver_failed, self.network.SIGNAL_DRIVER_FAILED)
                dispatcher.connect(self.driver_removed, self.network.SIGNAL_DRIVER_REMOVED)
                dispatcher.connect(self.driver_resetted, self.network.SIGNAL_DRIVER_RESET)

                dispatcher.connect(self.node_added, self.network.SIGNAL_NODE_ADDED)
                dispatcher.connect(self.node_removed, self.network.SIGNAL_NODE_REMOVED) 
                dispatcher.connect(self.node_ready, self.network.SIGNAL_NODE_READY) 
                
                dispatcher.connect(self.value_changed, self.network.SIGNAL_VALUE_CHANGED)
                
                succes = True
                
            except:
                succes = False
        else:
            succes = False

        return succes


    def start(self):
        """
            method used for start the zwave network

                return:
                    if succes return True
                    else retun false
        """
        
        succes = networkStarted = False

        if self.status == 'activated':
            if self.controllerPath != False and self.zwaveConfigFolderPath != False and self.networkConfigured != False:
                device = self.controllerPath
                log = "Debug"

                try:
                    # configuration of the logs
                    options = ZWaveOption(device, self.zwaveConfigFolderPath, user_path=".", cmd_line="")
                    options.set_log_file(self.logPath)
                    options.set_append_log_file(True)
                    options.set_console_output(False)
                    options.set_save_log_level(log)
                    options.set_logging(True)
                    options.lock()

                    # Construction of the zwave network
                    self.network = ZWaveNetwork(options, autostart=False)
                    
                    if isinstance(self.network, ZWaveNetwork):
                        #network starting
                        if self.load():
                            try:
                                self.network.start()
                                networkStarted = True
                            except:
                                networkStarted = False

                            if networkStarted:
                                print("Démarage")
                                print("astuce: penser a réveiller vos noeuds endormis\n\n")
                                
                                print("Etablissement du serveur ZWave: ")
                                
                                if not self.isReady:
                                    #requesting module
                                    for i in range(0, 300):
                                        if self.state >= self.network.STATE_READY:
                                            print("Le serveur ZWave est prêt\n\n")
                                            succes = True
                                            break
                                        else:
                                            sys.stdout.write(".")
                                            sys.stdout.flush()
                                            time.sleep(1.0)
                                            succes = False
                                else:
                                    succes = True
                            else:
                                succes = False
                        else:
                            succes = True
                    else:
                        succes = False
                except:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        if succes:
            self.running = True
        else:
            self.running = False

        # succes return
        return succes


    def stop(self):
        """
            method used for stop the network

                return:
                    if succes return true
                    else return false
        """
        
        succes = False

        if isinstance(self.network, ZWaveNetwork):
            if self.save_modification():
                if self.network.stop():
                    self.network = False
                    self.running = False

                    succes = True
                else:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        return succes


    def save_modification(self):
        """
            Method used for save network modification in zwave config folder
        
            return:
                if succes return true
                else return false
        """

        succes = False

        if isinstance(self.network, ZWaveNetwork):
            if self.isReady:
                try:
                    self.network.write_config()
                    succes = True
                except:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        return succes


    def restart(self):
        """
            Method used for restart the zwave network
        
            return:
                if succes return true
                else return false
        """

        succes = False

        if isinstance(self.network, ZWaveNetwork):
            if self.stop():
                if self.load():
                    if self.start():
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


    def activate(self):
        succes = False

        if self.set_status('activated'):
            succes = True
        else:
            succes = False

        if succes:
            if self.network_activated():
                succes = True
            else:
                succes = False
        else:
            pass

        return succes

    
    def deactivate(self):
        succes = False

        if self.running:
            self.stop()
            
        if self.set_status('disabled'):
            succes = True
        else:
            succes = False

        if succes:
            if self.network_deactivated():
                succes = True
            else:
                succes = False
        else:
            pass

        return succes


    def serialize(self):
        data = {}
        modulesList = []

        data['status'] = self.status
        data['running'] = self.running
        data['homeId'] = self.homeId
        data['state'] = self.state
        data['strState'] = self.strState
        data['isReady'] = self.isReady
        data['controllerPath'] = self.controllerPath
        data['zwaveConfigFolderPath'] = self.zwaveConfigFolderPath
        data['networkConfigured'] = self.networkConfigured

        for module in self.modulesList:
            modulesList.append(module.serialize())

        data['modulesList'] = modulesList

        return data



    """GET METHODS"""
    def get_module(self, moduleId):
        """
            method called for get an specific module on the network
                Parametters:
                    moduleId: int
                functionning:
                    - search for the module linked to the id
                        if the module was found:
                            return the module class
                        else:
                            return False
                return:
                    if succes module class
                    else return False
        """

        selectedModule = False

        if isinstance(moduleId, int) and isinstance(self.network, ZWaveNetwork):
            for module in self.modulesList:
                if module.id == moduleId:
                    selectedModule = module
                    break
                else:
                    selectedModule = False
        else:
            selectedModule = False

        return selectedModule



    """ADD METHODS""" 
    def add_module(self):
        """
            method called for adding an module on the network.
                Parametters:
                    newModuleName: str
                    newModuleLocation: int
                functionning::
                    -list module already on the network
                    ask to  add the module
                    -check if a new module was added
                    -save modification
                return:
                    if succes return module id
                    else return False
        """
        
        succes = False
        moduleIdListBeforeAddition = []
        newModule = False


        if isinstance(self.network, ZWaveNetwork) and self.isReady:
            for module in self.modulesList:
                moduleIdListBeforeAddition.append(module.id)

            if self.controller.add_node():
                print("Mettez le module en état d'inclusion")
                time.sleep(10)

                for module in self.modulesList:
                    if module.id in moduleIdListBeforeAddition:
                        newModule = False
                    else:
                        newModule = module
                        break
            else:
                newModule = False
        else:
            newModule = False


        if newModule != False:
            if self.save_modification():
                succes = True
            else:
                succes = False
        else:
            succes = False


        if succes is not False:
            return newModule.id
        else:
            return False



    """DEL METHODS"""
    def del_module(self, moduleId):
        """
            method called for del an specific module
                functionning:
                    -set controller on exclusion mode
                    -save modification
                return:
                    if succes return True
                    else return False
        """
        succes = False

        beforeModuleIdList = afterModuleIdList = []
        deleteState = False

        if isinstance(self.network, ZWaveNetwork) and self.isReady:
            if isinstance(moduleId, int):
                for module in self.modulesList:
                    beforeModuleIdList.append(module.id)

                if moduleId in beforeModuleIdList:
                    if self.controller.remove_node():
                        print("Mettez le module en état d'exclusion")
                        time.sleep(10)

                        for module in self.modulesList:
                            afterModuleIdList.append(module.id)

                        if moduleId in afterModuleIdList:
                            succes = False
                        else:
                            if self.save_modification():
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



    """SET METHODS"""
    def set_status(self, newStatus):
        succes = data = False

        if isinstance(newStatus, str) and newStatus == "activated" or newStatus == "disabled":
            try:
                with open(self.configFilePath) as configurationFile:
                    data = json.load(configurationFile)
            except:
                succes = data = False

            if data != False:
                data["state"] = newStatus

                try:
                    with open(self.configFilePath, 'w') as configurationFile:
                        #write data dictionnary in file
                        json.dump(data, configurationFile, indent=4)
                    succes = True
                except:
                    succes = False
            else:
                succes = False   
        else:
            succes = False
        
        return succes


    def set_module_name(self, moduleId, newName):
        """
            methods called for set an module's name.
                Parametters:
                    moduleId: int
                    newName: str
                functionning:
                    -ask to the module to change is name
                    -save modification
                return:
                    if succes return True
                    else return False
        """

        selectedModule = False
        succes = False

        if isinstance(self.network, ZWaveNetwork) and self.isReady:
            if isinstance(moduleId, int) and isinstance(newName, str):
                selectedModule = self.get_module(moduleId)

                if selectedModule is not False:
                    if selectedModule.set_name(newName):
                        if self.save_modification():
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


    def set_module_location(self, moduleId, newLocation):
        """
            methods called for set an module's location.
                Parametters:
                    moduleId: int
                    newLocation: int(roomId)
                functionning:
                    -ask to the module to change is location
                    -save modificaton
                return:
                    if succes return True
                    else return False
        """

        selectedModule = False
        succes = False

        if isinstance(self.network, ZWaveNetwork) and self.isReady:
            if isinstance(moduleId, int) and isinstance(newLocation, int):
                selectedModule = self.get_module(moduleId)

                if selectedModule is not False:
                    if selectedModule.set_location(newLocation):
                        if self.save_modification():
                            succes=  True
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


    def set_module_value(self, moduleId, valueId, data):
        """
            methods called for set an module value.
                Parametters:
                    moduleId: int
                    valueId: int
                    value data: 
                functionning:
                    -ask to the module to change is value
                    -save modification
                return:
                    if succes return True
                    else return False
        """

        succes = selectedModule = False

        if isinstance(self.network, ZWaveNetwork) and self.isReady:
            if isinstance(moduleId, int) and isinstance(valueId, int):
                selectedModule = self.get_module(moduleId)

                if selectedModule != False:
                    if selectedModule.set_value_data(valueId, data):
                        if self.save_modification():
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



    def set_light_controller_level(self, lightControllerId, newLevel):
        """
            Method called for set the level of an light controller
        
            Parametters:
                    lightControllerId: int
                    newLevel: int
                functionning:
                    -ask to the module to change is level
                    -save modification
                return:
                    if succes return True
                    else return False
        """
        
        succes = selectedModule = False
        
        if isinstance(self.network, ZWaveNetwork) and self.isReady:
            if isinstance(lightControllerId, int) and isinstance(newLevel, int):
                selectedModule = self.get_module(lightControllerId)
                
                if isinstance(selectedModule, ZWaveLightController):
                    if selectedModule.set_level(newLevel):
                        if self.save_modification():
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

    
    def set_light_controller_color_by_label(self, lightControllerId, colorLabel):
        """
            Method called for set the color of an color light controller by is label
        
            Parametters:
                    lightControllerId: int
                    color label: str
                functionning:
                    -ask to the module to change is color
                    -save modification
                return:
                    if succes return True
                    else return False
        """
        
        succes = selectedModule = False

        if isinstance(self.network, ZWaveNetwork) and self.isReady:
            if isinstance(lightControllerId, int) and isinstance(colorLabel, str):
                selectedModule = self.get_module(lightControllerId)

                if isinstance(selectedModule, ZWaveColorLightController):
                    if colorLabel in selectedModule.colorPalette:
                        if selectedModule.set_color_by_label(colorLabel):
                            if self.save_modification():
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


    def set_light_controller_color_by_rgbw(self, lightControllerId, colorValue):
        """
            Method called for set the color of an color light controller by is rgbw value
        
            Parametters:
                    lightControllerId: int
                    color Value: str
                functionning:
                    -ask to the module to change is color
                    -save modification
                return:
                    if succes return True
                    else return False
        """
        
        if isinstance(self.network, ZWaveNetwork) and self.isReady:
            if isinstance(lightControllerId, int) and isinstance(colorValue, str):
                selectedModule = self.get_module(lightControllerId)

                if isinstance(selectedModule, ZWaveColorLightController):
                    if selectedModule.set_color_by_rgbw(colorValue):
                        if self.save_modification():
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



    """SWITCH METHOD"""
    #light switches
    def switch_light_controller(self, lightControllerId, value):
        """
            Method called for switch the state of an light controller
        
            Parametters:
                    lightControllerId: int
                    value: bool
                functionning:
                    -ask to the module to change is state
                    -save modification
                return:
                    if succes return True
                    else return False
        """
        
        succes = selectedModule = False

        if isinstance(self.network, ZWaveNetwork) and self.isReady:
            if isinstance(lightControllerId, int) and isinstance(value, bool):
                selectedModule = self.get_module(lightControllerId)

                if isinstance(selectedModule, ZWaveLightController):
                    if value == True:
                        if selectedModule.switch_on():
                            if self.save_modification():
                                succes = True
                            else:
                                suces = False
                        else:
                            succes = False

                    elif value == False:
                        if selectedModule.switch_off():
                            if self.save_modification():
                                succes = True
                            else:
                                suces = False
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

    
    def switch_light_controller_on(self, lightControllerId):
        """
            Method called for set an light controller on
        
            Parametters:
                    lightControllerId: int
                functionning:
                    -change state of the module
                return:
                    if succes return True
                    else return False
        """
        
        succes = False

        if isinstance(self.network, ZWaveNetwork) and self.isReady:
            if isinstance(lightControllerId, int):
                if self.switch_light_controller(lightControllerId, True):
                    succes = True
                else:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        return succes


    def switch_light_controller_off(self, lightControllerId):
        """
            Method called for set an light controller off
        
            Parametters:
                    lightControllerId: int
                functionning:
                    -change state of the module
                return:
                    if succes return True
                    else return False
        """

        succes = False

        if isinstance(self.network, ZWaveNetwork) and self.isReady:
            if isinstance(lightControllerId, int):
                if self.switch_light_controller(lightControllerId, False):
                    succes = True
                else:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        return succes



    #relay switches
    def switch_relay(self, relayId, value):
        """
            Method called for switch the state of an relay
        
            Parametters:
                    relayId: int
                    value: bool
                functionning:
                    -ask to the module to change is state
                    -save modification
                return:
                    if succes return True
                    else return False
        """

        succes = selectedModule = False

        if isinstance(self.network, ZWaveNetwork) and self.isReady:
            if isinstance(relayId, int) and isinstance(value, bool):
                selectedModule = self.get_module(relayId)

                if isinstance(selectedModule, ZWaveRelay):
                    if value == True:
                        if selectedModule.switch_on():
                            if self.save_modification():
                                succes = True
                            else:
                                succes = False
                        else:
                            succes = False

                    elif value == False:
                        if selectedModule.switch_off():
                            if self.save_modification():
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


    def switch_relay_on(self, relayId):
        """
            Method called for set an relay on
        
            Parametters:
                    relayId: int
                functionning:
                    -change state of the module
                return:
                    if succes return True
                    else return False
        """

        succes = False

        if isinstance(self.network, ZWaveNetwork) and self.isReady:
            if isinstance(relayId, int):
                if self.switch_relay(relayId, True):
                    succes = True
                else:
                    succes = False
            else:
                succes = False
        else:
            succes = False
        
        return succes


    def switch_relay_off(self, relayId):
        """
            Method called for set an relay off
        
            Parametters:
                    relayId: int
                functionning:
                    -change state of the module
                return:
                    if succes return True
                    else return False
        """

        succes = False

        if isinstance(self.network, ZWaveNetwork) and self.isReady:
            if isinstance(relayId, int):
                if self.switch_relay(relayId, False):
                    succes = True
                else:
                    succes = False
            else:
                succes = False
        else:
            succes = False
        
        return succes



    """HEAL METHOD"""
    def heal_network(self):
        """
            method used for heal the network

                return:
                    if succes return true 
                    else return false
        """

        succes = False

        if isinstance(self.network, ZWaveNetwork):
            try:
                self.network.heal()
                
                succes = True
            except:
                succes = False
        else:
            succes = False

        
        if succes:
            if self.network_healed():
                succes = True
            else:
                succes = False
        else:
            pass

        return succes


    def heal_module(self, moduleId):
        """
            method used for heal an network

                parametters:
                    moduleId: int

                functionning:
                    -ask to module to heal itself

                return:
                    true if succes
                    else false
        """

        succes = selectedModule = False

        if isinstance(self.network, ZWaveNetwork) and self.isReady:
            if isinstance(moduleId, int):
                selectedModule = self.get_module(moduleId)

                if selectedModule != False:
                    if selectedModule.heal():
                        succes = True
                    else:
                        succes = False
                else:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        if succes:
            if self.module_healed(selectedModule):
                succes = True
            else:
                succes = False
        else:
            pass

        return succes



    """DESTROY METHODS"""
    def destroy_network(self):
        """
            method used for destroy the network

            return
                true if succes
                else false
        """

        succes = False

        if isinstance(self.network, ZWaveNetwork) and self.isReady:
            try:
                self.network.destroy()

                succes = True
            except:
                succes = False
        else:
            succes = False

        if succes:
            if self.network_destroyed():
                succes = True
            else:
                succes = False
        else:
            pass

        return succes



    """UPDATE METHOD"""
    def update_module_return_route(self, moduleId):
        """
            method called for update an module return route

                parametters:
                    moduleId: int

                functionning:
                    -ask to module to update is return route

                return:
                    true if succes
                    else false
        """

        succes = selectedModule = False

        if isinstance(self.network, ZWaveNetwork) and self.isReady:
            if isinstance(moduleId, int):
                selectedModule = self.get_module(moduleId)

                if selectedModule != False:
                    if selectedModule.update_return_route():
                        succes = True
                    else:
                        succes = False
                else:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        if succes:
            if self.module_return_route_updated(selectedModule):
                succes = True
            else:
                succes = False
        else:
            pass

        return succes


    def update_module_neighbors(self, moduleId):
        """
            method called for update an module neighbor

                parametters:
                    moduleId: int

                functionning:
                    -ask to module to update is neighbor

                return:
                    true if succes
                    else false
        """

        succes = selectedModule = False

        if isinstance(self.network, ZWaveNetwork) and self.isReady:
            if isinstance(moduleId, int):
                selectedModule = self.get_module(moduleId)

                if selectedModule != False:
                    if selectedModule.update_neighbors():
                        succes = True
                    else:
                        succes = False
                else:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        if succes:
            if self.module_neighbors_updated(selectedModule):
                succes = True
            else:
                succes = False
        else:
            pass

        return succes


    def update_module_network(self, moduleId):
        """
            method called for update an module network

                parametters:
                    moduleId: int

                functionning:
                    -ask to module to update is network

                return:
                    true if succes
                    else false
        """

        succes = selectedModule = False

        if isinstance(self.network, ZWaveNetwork) and self.isReady:
            if isinstance(moduleId, int):
                selectedModule = self.get_module(moduleId)

                if selectedModule != False:
                    if selectedModule.update_network():
                        succes = True
                    else:
                        succes = False
                else:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        if succes:
            if self.module_network_updated(selectedModule):
                succes = True
            else:
                succes = False
        else:
            pass        

        return succes



    """REFRESH METHOD"""
    def refresh_module_informations(self, moduleId):
        """
            method called for update the information of an module

                parametters:
                    moduleId: int

                functionning:
                    -ask to module to update is information

                return:
                    true if succes
                    else false
        """

        succes = selectedModule = False

        if isinstance(self.network, ZWaveNetwork) and self.isReady:
            if isinstance(moduleId, int):
                selectedModule = self.get_module(moduleId)

                if selectedModule != False:
                    if selectedModule.refresh_info():
                        succes = True
                    else:
                        succes = False
                else:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        if succes:
            if self.module_informations_refreshed(selectedModule):
                succes = True
            else:
                succes = False
        else:
            pass

        return succes


    def refresh_module_value(self, moduleId, valueId):
        """
            method called for update an value of an module

                parametters:
                    moduleId: int

                functionning:
                    -ask to module to update the value

                return:
                    true if succes
                    else false
        """

        succes = selectedModule = False

        if isinstance(self.network, ZWaveNetwork) and self.isReady:
            if isinstance(moduleId, int) and isinstance(valueId, int):
                selectedModule = self.get_module(moduleId)

                if selectedModule != False:
                    if selectedModule.refresh_value(valueId):
                        succes = True
                    else:
                        succes = False
                else:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        if succes:
            if self.module_value_refreshed(selectedModule):
                succes = True
            else:
                succes = False
        else:
            pass

        return succes


    def refresh_module_values(self, moduleId):
        """
            method called for update all value of an module

                parametters:
                    moduleId: int

                functionning:
                    -ask to module to update his values

                return:
                    true if succes
                    else false
        """

        succes = selectedModule = False

        if isinstance(self.network, ZWaveNetwork) and self.isReady:
            if isinstance(moduleId, int):
                selectedModule = self.get_module(moduleId)

                if selectedModule != False:
                    if selectedModule.refresh_values():
                        succes = True
                    else:
                        succes = False
                else:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        if succes:
            if self.module_values_refreshed(selectedModule):
                succes = True
            else:
                succes = False
        else:
            pass

        return succes



    """RESET METHOD"""
    def soft_reset_network(self):
        """
            method called for soft reset network

                return:
                    true if succes
                    else false
        """
        succes = False

        if isinstance(self.network, ZWaveNetwork) and self.isReady:
            if self.controller.soft_reset_network():
                succes = True
            else:
                succes = False
        else:
            succes = False

        if self.server != False and succes:
            if self.network_soft_resetted():
                succes = True
            else:
                succes = False
        else:
            pass

        return succes


    def hard_reset_network(self):
        """
            method called for hard reset network

                return:
                    true if succes
                    else false
        """

        succes = False

        if isinstance(self.network, ZWaveNetwork) and self.isReady:
            if self.controller.hard_reset_network():
                succes = True
            else:
                succes = False
        else:
            succes = False

        if succes:
            if self.network_hard_resetted():
                succes = True
            else:
                succes = False
        else:
            pass

        return succes



    ###NETWORK INTERACTIONS###
    """NETWORK EVENT"""
    def network_activated(self):
        succes = eventDatetime = event = False

        print("reseau zwave activer")
        
        try:
            eventDatetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            event = ZWaveNetworkActivated(eventDatetime)
            self.eventList.append(event)

            if event in self.eventList:
                succes = True
            else:
                succes = False

            if self.server != False and succes:
                if self.send_zWave_network_activated_event(event):
                    succes = True
                else:
                    succes = False
            else:
                pass
        except:
            succes = False

        return succes


    def network_deactivated(self):
        succes = eventDatetime = event = False

        print("reseau zwave activer")
        
        try:
            eventDatetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            event = ZWaveNetworkDeactivated(eventDatetime)
            self.eventList.append(event)

            if event in self.eventList:
                succes = True
            else:
                succes = False

            if self.server != False and succes:
                if self.send_zWave_network_deactivated_event(event):
                    succes = True
                else:
                    succes = False
            else:
                pass
        except:
            succes = False

        return succes


    def network_started(self):
        """
            method called when network is started

                functionning:
                    -add zwave network started event in event list

                return:
                    true if succes
                    else false
        """

        succes = eventDatetime = event = False

        print("reseau zwave demarrer:\n\
        homeid: {:08x}\n\n".format(self.homeId))
        
        try:
            eventDatetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            event = ZWaveNetworkStarted(eventDatetime)
            self.eventList.append(event)

            if event in self.eventList:
                succes = True
            else:
                succes = False

            if self.server != False and succes:
                if self.send_zWave_network_started_event(event):
                    succes = True
                else:
                    succes = False
            else:
                pass
        except:
            succes = False

        return succes


    def network_ready(self):
        """
            method called when network is ready
        """

        succes = event = eventDatetime = False

        print("reseau zwave pret\n")

        try:
            eventDatetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            event = ZWaveNetworkReady(eventDatetime)

            self.eventList.append(event)
        except:
            event = False

        if event != False:
            if event in self.eventList:
                succes = True
            else:
                succes = False
        else:
            succes = False

        if self.server != False and succes:
            if self.send_zWave_network_ready_event(event):
                succes = True
            else:
                succes = False
        else:
            pass

        return succes


    def network_awake(self):
        """
            method called when network is awaked
        """

        succes = event = eventDatetime = False

        print("reseau zwave reveille")

        for module in self.modulesList:
            if module.isSleeping:
                print("penser a reveiller le module n°{} ({})".format(module.id, module.name))
                print('\n\n')

        try:
            eventDatetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            event = ZWaveNetworkAwaked(eventDatetime)

            self.eventList.append(event)
        except:
            event = False

        if event != False:
            if event in self.eventList:
                succes = True
            else:
                succes = False
        else:
            succes = False

        if self.server != False and succes:
            if self.send_zWave_network_awaked_event(event):
                succes = True
            else:
                succes = False
        else:
            pass

        return succes


    def network_failed(self):
        """
            method called when network is failed

                functionning:
                    -add zwave network failed event in event list

                return:
                    true if succes
                    else false
        """
        
        succes = False

        print("Erreur lors du demarrage du reseau zwave")

        try:
            eventDatetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            event = ZWaveNetworkFailed(eventDatetime)

            self.eventList.append(event)

            if event in self.eventList:
                if self.stop():
                    succes = True
                else:
                    succes = False
            else:
                succes = False

            if self.server != False and succes:
                if self.send_zWave_network_failed_event(event):
                    succes = True
                else:
                    succes = False
            else:
                pass
        except:
            succes = False

        return succes


    def network_stopped(self):
        """
            method called when network is stopped

                functionning:
                    -add zwave network stopped event in event list

                return:
                    true if succes
                    else false
        """

        succes = False

        print("reseau zwave arreter\n\n")

        try:
            eventDatetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            event = ZWaveNetworkStopped(eventDatetime)

            self.eventList.append(event)

            if event in self.eventList:
                if self.stop():
                    succes = True
                else:
                    succes = False
            else:
                succes = False

            if self.server != False and succes:
                if self.send_zWave_network_stopped_event(event):
                    succes = True
                else:
                    succes = False
            else:
                pass
        except:
            succes = False

        return succes


    def network_resetted(self):
        """
            method called when network is resetted

                functionning:
                    -add zwave network resetted event in event list

                return:
                    true if succes
                    else false
        """

        succes = False

        print("reseau zwave redemarrer\n\n")

        try:
            eventDatetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            event = ZWaveNetworkResetted(eventDatetime)

            self.eventList.append(event)

            if event in self.eventList:
                succes = True
            else:
                succes = False

            if self.server != False and succes:
                if self.send_zWave_network_resetted_event(event):
                    succes = True
                else:
                    succes = False
            else:
                pass

        except:
            succes = False

        return succes


    def network_healed(self):
        print("reseau zwave soigner\n\n")

        try:
            eventDatetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            event = ZWaveNetworkHealed(eventDatetime)

            self.eventList.append(event)

            if event in self.eventList:
                succes = True
            else:
                succes = False

            if self.server != False and succes:
                if self.send_zWave_network_healed_event(event):
                    succes = True
                else:
                    succes = False
            else:
                pass

        except:
            succes = False

        return succes


    def network_destroyed(self):
        print("reseau zwave detruit\n\n")

        try:
            eventDatetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            event = ZWaveNetworkDestroyed(eventDatetime)

            self.eventList.append(event)

            if event in self.eventList:
                succes = True
            else:
                succes = False

            if self.server != False and succes:
                if self.send_zWave_network_destroyed_event(event):
                    succes = True
                else:
                    succes = False
            else:
                pass

        except:
            succes = False

        return succes


    def network_soft_resetted(self):
        print("reseau zwave soft resetted\n\n")

        try:
            eventDatetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            event = ZWaveNetworkSoftResetted(eventDatetime)

            self.eventList.append(event)

            if event in self.eventList:
                succes = True
            else:
                succes = False

            if self.server != False and succes:
                if self.send_zWave_network_soft_resetted_event(event):
                    succes = True
                else:
                    succes = False
            else:
                pass

        except:
            succes = False

        return succes


    def network_hard_resetted(self):
        print("reseau zwave hard resetted\n\n")

        try:
            eventDatetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            event = ZWaveNetworkHardResetted(eventDatetime)

            self.eventList.append(event)

            if event in self.eventList:
                succes = True
            else:
                succes = False

            if self.server != False and succes:
                if self.send_zWave_network_hard_resetted_event(event):
                    succes = True
                else:
                    succes = False
            else:
                pass

        except:
            succes = False

        return succes



    """DRIVER EVENT"""
    def driver_ready(self):
        """
            method called when controller is ready
        """

        succes = event = eventDatetime = False

        print("initialisation du controller reussi\n\n")

        try:
            eventDatetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            event = ZWaveControllerReady(eventDatetime)

            self.eventList.append(event)
        except:
            event = False

        if event != False:
            if event in self.eventList:
                succes = True
            else:
                succes = False
        else:
            succes = False

        if self.server != False and succes:
            if self.send_zWave_controller_ready_event(event):
                succes = True
            else:
                succes = False
        else:
            pass

        return succes


    def driver_failed(self):
        """
            method called when controller is failed
        """

        succes = event = eventDatetime = False

        print("erreur d'initialisation du controller\n\n")

        try:
            eventDatetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            event = ZWaveControllerFailed(eventDatetime)

            self.eventList.append(event)

            if event in self.eventList:
                if self.stop():
                    succes = True
                else:
                    succes = False
            else:
                succes = False

        except:
            succes = False

        if self.server != False and succes:
            if self.send_zWave_controller_failed_event(event):
                succes = True
            else:
                succes = False
        else:
            pass

        return succes


    def driver_removed(self):
        """
            method called when controller is removed
        """

        succes = event = eventDatetime = False

        print("controlleur debrancher\n\n")

        try:
            eventDatetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            event = ZWaveControllerRemoved(eventDatetime)

            self.eventList.append(event)

            if event in self.eventList:
                if self.stop():
                    succes = True
                else:
                    succes = False
            else:
                succes = False

        except:
            succes = False

        if self.server != False and succes:
            if self.send_zWave_controller_removed_event(event):
                succes = True
            else:
                succes = False
        else:
            pass

        return succes


    def driver_resetted(self):
        """
            method called when controller is resetted
        """

        succes = event = eventDatetime = False

        print("controlleur reinitialiser\n\n")

        try:
            eventDatetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            event = ZWaveControllerResetted(eventDatetime)

            self.eventList.append(event)

            if event in self.eventList:
                if self.restart():
                    succes = True
                else:
                    succes = False
            else:
                succes = False

        except:
            succes = False

        if self.server != False and succes:
            if self.send_zWave_controller_resetted_event(event):
                succes = True
            else:
                succes = False
        else:
            pass

        return succes



    """NODE EVENT"""
    def node_added(self, node):
        """
            method called when an module is added to the network

                parametters:
                    node: ZwaveNode

                functionning:
                    -ask to module to update is return route
                    -ask to module to update his neighbor
                    -ask to module to update his network

                return:
                    true if succes
                    else false
        """

        succes = event = eventDatetime = False

        print("module n°{} nomme: {}  as ete ajouter au reseau".format(node.node_id, node.name))

        module = self.get_module(node.node_id)

        if module != False:
            try:
                eventDatetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
                event = ZWaveNetworkModuleAdded(eventDatetime, module.id)

                self.eventList.append(event)

                module = False

                if event in self.eventList:
                    for module in self.modulesList:
                        if module.update_return_route():
                            if module.update_neighbors():
                                if module.update_network():
                                    succes = True
                                else:
                                    succes = False
                                    break
                            else:
                                succes = False
                                break
                        else:
                            succes = False
                            break
                else:
                    succes = False

            except:
                succes = False
        else:
            succes = False
        
        if self.server != False and succes:
            if self.send_module_added_event(event):
                succes = True
            else:
                succes = False
        else:
            pass

        return succes


    def node_removed(self, node):
        """
            method called when an module was removed

                parametters:
                    node: ZwaveNode

                functionning:
                    -ask to all module to update his return route
                    -ask to all module to update his neighbor
                    -ask to all module to update his network

                return:
                    true if succes
                    else false
        """

        succes = event = eventDatetime = False

        print("module n°{} nomme {}  as ete retirer du reseau".format(node.node_id, node.name))

        try:
            eventDatetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            event = ZWaveNetworkModuleRemoved(eventDatetime, node.node_id)

            self.eventList.append(event)

            if event in self.eventList:
                for module in self.modulesList:
                    if module.update_return_route():
                        if module.update_neighbors():
                            if module.update_network():
                                succes = True
                            else:
                                succes = False
                                break
                        else:
                            succes = False
                            break
                    else:
                        succes = False
                        break
            else:
                succes = False
        except:
            succes = False

        if self.server != False and succes:
            if self.send_module_removed_event(event):
                succes = True
            else:
                succes = False
        else:
            pass

        return succes


    def node_ready(self, node):
        """
            method called when an module is ready

                parametters:
                    node: ZwaveNode

                functionning:
                    -ask to module to update is return route
                    -ask to module to update his neighbor
                    -ask to module to update his network

                return:
                    true if succes
                    else false
        """
        succes = event = module = eventDatetime = False

        print("module n°{} est pret".format(node.node_id))

        module = self.get_module(node.node_id)
        
        if isinstance(module, ZWaveModule):
            eventDatetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            event = ZWaveModuleReady(eventDatetime, module.id)

            self.eventList.append(event)

            if event in self.eventList:
                if module.update_return_route():
                    if module.update_neighbors():
                        if module.update_network():
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

        if self.server != False and succes:
            if self.send_module_ready_event(event):
                succes = True
            else:
                succes = False
        else:
            pass

        return succes


    def value_changed(self, node, value):
        """
            method called when an value was modified

                parametters:
                    node: ZwaveNode
                    value: zwaveValue

                functionning:
                    determines the module whose value has changed
                    determine which value has been changed
                    trigger the asociate event (depending on module and value)

                return:
                    true if succes
                    else false
        """

        succes = eventProcessed = False

        if self.isReady:
            module = self.get_module(node.node_id)
            
            if value.label.lower() == 'name':
                if self.module_renamed(module):
                    succes = True
                else:
                    succes = False
            elif value.label.lower() == 'location':
                if self.module_moved(module):
                    succes = True
                else:
                    succes = False
            else:
                if isinstance(module, ZWaveModule):
                    if module.update_network():
                        #event of sensor
                        if isinstance(module, ZWaveSensor):
                            if value.label.lower() == 'access control' and 'acces control sensor' in module.strSensorsList:
                                if module.sensors['acces control sensor'].acces_state == 'open':
                                    if self.acces_open(module):
                                        eventProcessed = True
                                    else:
                                        eventProcessed = False

                                elif module.sensors['acces control sensor'].acces_state == 'closed':
                                    if self.acces_close(module):
                                        eventProcessed = True
                                    else:
                                        eventProcessed = False

                            elif value.label.lower() == 'sensor' and 'motion sensor' in module.strSensorsList:
                                if value.data == True:
                                    if self.motion_detection(module):
                                        eventProcessed = True
                                    else:
                                        eventProcessed = False
                            else:
                                eventProcessed = False

                        #light event
                        elif isinstance(module, ZWaveLightController):
                            if value.label.lower() == "level":
                                if value.data > 0:
                                    if value.data == module.startLevel or value.data == 99:
                                        if self.light_turning_on(module):
                                            eventProcessed = True
                                        else:
                                            eventProcessed = False
                                    else:
                                        if self.light_intensity_modified(module):
                                            eventProcessed = True
                                        else:
                                            eventProcessed = False
                                elif value.data == 0:
                                    if self.light_turning_off(module):
                                        eventProcessed = True
                                    else:
                                        eventProcessed = False

                            elif value.label.lower() == "color" and isinstance(module, ZWaveColorLightController):
                                if self.light_color_modified(module):
                                    eventProcessed = True
                                else:
                                    eventProcessed = False

                            else:
                                eventProcessed = False

                        #relay event
                        elif isinstance(module, ZWaveRelay):
                            if value.label.lower() == "switch":
                                if value.data == True:
                                    if self.relay_setting_on(module):
                                        eventProcessed = True
                                    else:
                                        eventProcessed = False
                                elif value.data == False:
                                    if self.relay_setting_off(module):
                                        eventProcessed = True
                                    else:
                                        eventProcessed = False
                                else:
                                    eventProcessed = False
                            else:
                                eventProcessed = False

                        #other
                        else:
                            if self.server != False and succes:
                                if self.module_value_modified(module, value.id):
                                    succes = True
                                else:
                                    succes = False
                            else:
                                pass

                        if eventProcessed:
                            if self.save_modification():
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
            succes = True


    def module_moved(self, module):
        """
            method called when an module location was changed

                parametters:
                    module: module class
                    eventDatetime: event of the datetime(str)

                functionning:
                    add event in event list

                return:
                    true if succes
                    else false
        """
        succes = event = eventDatetime = False

        if isinstance(module, ZWaveModule):
            eventDatetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            event = ZWaveModuleMoved(module.id, eventDatetime, module.location)
            self.eventList.append(event)

            print(event)

            if event in self.eventList:
                succes = True
            else:
                succes = False
        else:
            succes = False

        if self.server != False and succes:
            if self.send_module_relocated_event(event):
                succes = True
            else:
                succes = False
        else:
            pass

        return succes


    def module_renamed(self, module):
        """
            method called when an module name was changed

                parametters:
                    module: module class
                    eventDatetime: event of the datetime(str)

                functionning:
                    add event in event list

                return:
                    true if succes
                    else false
        """
        succes = event = eventDatetime = False

        if isinstance(module, ZWaveModule):
            eventDatetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            event = ZWaveModuleRenamed(module.id, eventDatetime, module.location)
            self.eventList.append(event)

            print(event)

            if event in self.eventList:
                    succes = True
            else:
                succes = False
        else:
            succes = False

        if self.server != False and succes:
            if self.send_module_renamed_event(event):
                succes = True
            else:
                succes = False
        else:
            pass

        return succes


    def module_healed(self, module):
        succes = event = eventDatetime = False

        if isinstance(module, ZWaveModule):
            eventDatetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            event = ZWaveModuleHealed(module.id, eventDatetime, module.location)
            self.eventList.append(event)

            print(event)

            if event in self.eventList:
                    succes = True
            else:
                succes = False
        else:
            succes = False

        if self.server != False and succes:
            if self.send_zWave_module_healed_event(event):
                succes = True
            else:
                succes = False
        else:
            pass

        return succes


    def module_return_route_updated(self, module):
        succes = event = eventDatetime = False

        if isinstance(module, ZWaveModule):
            eventDatetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            event = ZWaveModuleReturnRouteUpdated(module.id, eventDatetime, module.location)
            self.eventList.append(event)

            print(event)

            if event in self.eventList:
                    succes = True
            else:
                succes = False
        else:
            succes = False

        if self.server != False and succes:
            if self.send_zWave_module_return_route_updated_event(event):
                succes = True
            else:
                succes = False
        else:
            pass

        return succes


    def module_neighbors_updated(self, module):
        succes = event = eventDatetime = False

        if isinstance(module, ZWaveModule):
            eventDatetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            event = ZWaveModuleNeighborsUpdated(module.id, eventDatetime, module.location)
            self.eventList.append(event)

            print(event)

            if event in self.eventList:
                    succes = True
            else:
                succes = False
        else:
            succes = False

        if self.server != False and succes:
            if self.send_zWave_module_neighbors_updated_event(event):
                succes = True
            else:
                succes = False
        else:
            pass

        return succes


    def module_network_updated(self, module):
        succes = event = eventDatetime = False

        if isinstance(module, ZWaveModule):
            eventDatetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            event = ZWaveModuleNetworkUpdated(module.id, eventDatetime, module.location)
            self.eventList.append(event)

            print(event)

            if event in self.eventList:
                    succes = True
            else:
                succes = False
        else:
            succes = False

        if self.server != False and succes:
            if self.send_zWave_module_network_updated_event(event):
                succes = True
            else:
                succes = False
        else:
            pass

        return succes


    def module_informations_refreshed(self, module):
        succes = event = eventDatetime = False

        if isinstance(module, ZWaveModule):
            eventDatetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            event = ZWaveModuleInformationsRefreshed(module.id, eventDatetime, module.location)
            self.eventList.append(event)

            print(event)

            if event in self.eventList:
                    succes = True
            else:
                succes = False
        else:
            succes = False

        if self.server != False and succes:
            if self.send_zWave_module_informations_refreshed_event(event):
                succes = True
            else:
                succes = False
        else:
            pass

        return succes


    def module_value_refreshed(self, module):
        succes = event = eventDatetime = False

        if isinstance(module, ZWaveModule):
            eventDatetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            event = ZWaveModuleValueRefreshed(module.id, eventDatetime, module.location)
            self.eventList.append(event)

            print(event)

            if event in self.eventList:
                    succes = True
            else:
                succes = False
        else:
            succes = False

        if self.server != False and succes:
            if self.send_zWave_module_value_refreshed_event(event):
                succes = True
            else:
                succes = False
        else:
            pass

        return succes


    def module_values_refreshed(self, module):
        succes = event = eventDatetime = False

        if isinstance(module, ZWaveModule):
            eventDatetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            event = ZWaveModuleValueRefreshed(module.id, eventDatetime, module.location)
            self.eventList.append(event)

            print(event)

            if event in self.eventList:
                    succes = True
            else:
                succes = False
        else:
            succes = False

        if self.server != False and succes:
            if self.send_zWave_module_value_refreshed_event(event):
                succes = True
            else:
                succes = False
        else:
            pass

        return succes



    """SENSOR EVENT"""
    def motion_detection(self, module):
        """
            method called when an motion was detected by motion detector
        
                parametters:
                    module: sensor class (module)
                    eventDatetime: event of the datetime(str)

                functionning:
                    add event in event list

                return:
                    true if succes
                    else false
        """

        succes = event = eventDatetime = False

        if isinstance(module, ZWaveSensor):
            if 'motion sensor' in module.strSensorsList:
                eventDatetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
                event = ZWaveMotionDetection(module.id, eventDatetime, module.location)
                self.eventList.append(event)

                print(event)

                if event in self.eventList:
                    succes = True
                else:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        if self.server != False and succes:
            if self.send_motion_detected_event(event):
                succes = True
            else:
                succes = False
        else:
            pass

        return succes


    def acces_open(self, module):
        """
            method called when an acces was oppened

                parametters:
                    module: sensor class (module)
                    eventDatetime: event of the datetime(str)

                functionning:
                    add event in event list

                return:
                    true if succes
                    else false
        """

        succes = event = eventDatetime = False

        if isinstance(module, ZWaveSensor):
            if 'acces control sensor' in module.strSensorsList:
                eventDatetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
                event = ZWaveAccesOpened(module.id, eventDatetime, module.location)
        
                self.eventList.append(event)
                print(event)

                if event in self.eventList:
                    succes = True
                else:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        if self.server != False and succes:
            if self.send_acces_openned_event(event):
                succes = True
            else:
                succes = False
        else:
            pass

        return succes


    def acces_close(self, module):
        """
            method called when an acces was closed

                parametters:
                    module: sensor class (module)
                    eventDatetime: event of the datetime(str)

                functionning:
                    add event in event list

                return:
                    true if succes
                    else false
        """
        succes = event = eventDatetime = False

        if isinstance(module, ZWaveSensor):
            if 'acces control sensor' in module.strSensorsList:
                eventDatetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
                event = ZWaveAccesClosed(module.id, eventDatetime, module.location)
                self.eventList.append(event)
                print(event)

                if event in self.eventList:
                    succes = True
                else:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        if self.server != False and succes:
            if self.send_acces_closed_event(event):
                succes = True
            else:
                succes = False
        else:
            pass

        return succes



    """LIGHT CONTROLLER EVENT"""
    def light_turning_on(self, module):
        """
            method called when an light was turning on

                parametters:
                    module: light controller class (module)
                    eventDatetime: event of the datetime(str)

                functionning:
                    add event in event list

                return:
                    true if succes
                    else false
        """
        succes = event = eventDatetime = False

        if isinstance(module, ZWaveLightController):
            eventDatetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            event = ZWaveLightSettingOn(module.id, eventDatetime, module.location)
            self.eventList.append(event)
            print(event)

            if event in self.eventList:
                succes = True
            else:
                succes = False

        else:
            succes = False

        """
        if self.server != False and succes:
            if self.send_light_controller_switching_on_event(event):
                succes = True
            else:
                succes = False
        else:
            pass
        """

        return succes


    def light_turning_off(self, module):
        """
            method called when an light was turning off

                parametters:
                    module: light controller class (module)
                    eventDatetime: event of the datetime(str)

                functionning:
                    add event in event list

                return:
                    true if succes
                    else false
        """
        succes = event = eventDatetime = False

        if isinstance(module, ZWaveLightController):
            eventDatetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            event = ZWaveLightSettingOff(module.id, eventDatetime, module.location)
            self.eventList.append(event)
            print(event)

            if event in self.eventList:
                succes = True
            else:
                succes = False
        else:
            succes = False

        if self.server != False and succes:
            if self.send_light_controller_switching_off_event(event):
                succes = True
            else:
                succes = False
        else:
            pass

        return succes


    def light_color_modified(self, module):
        """
            method called when an light color was modified

                parametters:
                    module: color light controller class (module)
                    eventDatetime: event of the datetime(str)

                functionning:
                    add event in event list

                return:
                    true if succes
                    else false
        """
        succes = event = eventDatetime = False

        if isinstance(module, ZWaveColorLightController):
            eventDatetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            event = ZWaveLightColorModified(module.id, eventDatetime, module.location)
            self.eventList.append(event)
            print(event)

            if event in self.eventList:
                succes = True
            else:
                succes = False
        else:
            succes = False

        if self.server != False and succes:
            if self.send_light_controller_color_updated_event(event):
                succes = True
            else:
                succes = False
        else:
            pass

        return succes


    def light_intensity_modified(self, module):
        """
            method called when an light intensity was modified

                parametters:
                    module: light controller class (module)
                    eventDatetime: event of the datetime(str)

                functionning:
                    add event in event list

                return:
                    true if succes
                    else false
        """
        succes = event = eventDatetime = False

        if isinstance(module, ZWaveLightController):
            eventDatetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            event = ZWaveLightIntensityModified(module.id, eventDatetime, module.location)
            self.eventList.append(event)
            print(event)

            if event in self.eventList:
                succes = True
            else:
                succes = False
        else:
            succes = False

        if self.server != False and succes:
            if self.send_light_controller_level_updated_event(event):
                succes = True
            else:
                succes = False
        else:
            pass

        return succes



    """RELAY EVENT"""
    def relay_setting_on(self, module):
        """
            method called when an relay was turning on

                parametters:
                    module: relay class (module)
                    eventDatetime: event of the datetime(str)

                functionning:
                    add event in event list

                return:
                    true if succes
                    else false
        """
        succes = event = eventDatetime = False

        if isinstance(module, ZWaveRelay):
            eventDatetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            event = ZWaveRelaySettingOn(module.id, eventDatetime, module.location)
            self.eventList.append(event)
            print(event)

            if event in self.eventList:
                succes = True
            else:
                succes = False
        else:
            succes = False

        if self.server != False and succes:
            if self.send_relay_switching_on_event(event):
                succes = True
            else:
                succes = False
        else:
            pass

        return succes


    def relay_setting_off(self, module):
        """
            method called when an relay was turning off

                parametters:
                    module: relay class (module)
                    eventDatetime: event of the datetime(str)

                functionning:
                    add event in event list

                return:
                    true if succes
                    else false
        """
        succes = event = eventDatetime = False

        if isinstance(module, ZWaveRelay) and isinstance(eventDatetime, str):
            eventDatetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            event = ZWaveRelaySettingOff(module.id, eventDatetime, module.location)
            self.eventList.append(event)
            print(event)

            if event in self.eventList:
                succes = True
            else:
                succes = False
        else:
            succes = False

        if self.server != False and succes:
            if self.send_relay_switching_off_event(event):
                succes = True
            else:
                succes = False
        else:
            pass

        return succes
        

    
    ###SERVER EVENT###
    def send_zWave_network_updated_event(self, event):
        succes = False
        newZwaveNetworkInformations = {}

        if self.server != False and isinstance(event, ZWaveNetworkUpdated):
            self.server.emit('zWave_network_updated', event.serialize(), namespace='/HomeAutomationServer')
            if self.send_zWave_network_informations():
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def send_zWave_modules_list_updated_event(self, event):
        succes = False

        if self.server != False and isinstance(event, ZWaveNetworkModulesListUpdated):
            self.server.emit('zWave_modules_list_updated', event.serialize(), namespace='/HomeAutomationServer')
            
            if self.send_modules_list():
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def send_module_updated_event(self, moduleId):
        succes = module = False

        module = self.get_module(moduleId)

        if self.server != False:
            if module != False:
                self.server.emit('module_updated', module.serialize(), namespace='/HomeAutomationServer')
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def send_zWave_network_activated_event(self, event):
        succes = False

        if self.server != False and isinstance(event, ZWaveNetworkActivated):
            self.server.emit('zWave_network_activated', event.serialize(), namespace='/HomeAutomationServer')
            
            if self.send_zWave_network_informations():
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def send_zWave_network_deactivated_event(self, event):
        succes = False

        if self.server != False and isinstance(event, ZWaveNetworkDeactivated):
            self.server.emit('zWave_network_deactivated', event.serialize(), namespace='/HomeAutomationServer')
            
            if self.send_zWave_network_informations():
                succes = True
            else:
                succes = False
        else:
            succes= False

        return succes


    def send_zWave_network_started_event(self, event):
        succes = False

        if self.server != False and isinstance(event, ZWaveNetworkStarted):
            self.server.emit('zWave_network_started', event.serialize(), namespace='/HomeAutomationServer')
            
            if self.send_zWave_network_informations():
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def send_zWave_network_ready_event(self, event):
        succes = False

        if self.server != False and isinstance(event, ZWaveNetworkReady):
            self.server.emit('zWave_network_ready', event.serialize(), namespace='/HomeAutomationServer')
            
            if self.send_zWave_network_informations():
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def send_zWave_network_awaked_event(self, event):
        succes = False

        if self.server != False and isinstance(event, ZWaveNetworkAwaked):
            self.server.emit('zWave_network_awaked', event.serialize(), namespace='/HomeAutomationServer')
            
            if self.send_zWave_network_informations():
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def send_zWave_network_failed_event(self, event):
        succes = False

        if self.server != False and isinstance(event, ZWaveNetworkFailed):
            self.server.emit('zWave_network_failed', event.serialize(), namespace='/HomeAutomationServer')
            
            if self.send_zWave_network_informations():
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def send_zWave_network_stopped_event(self, event):
        succes = False

        if self.server != False and isinstance(event, ZWaveNetworkStopped):
            self.server.emit('zWave_network_stopped', event.serialize(), namespace='/HomeAutomationServer')
            
            if self.send_zWave_network_informations():
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def send_zWave_network_resetted_event(self, event):
        succes = False

        if self.server != False and isinstance(event, ZWaveNetworkResetted):
            self.server.emit('zWave_network_resetted', event.serialize(), namespace='/HomeAutomationServer')
            
            if self.send_zWave_network_informations():
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes
        

    def send_zWave_network_healed_event(self, event):
        succes = False

        if self.server != False and isinstance(event, ZWaveNetworkHealed):
            self.server.emit('zWave_network_healed', event.serialize(), namespace='/HomeAutomationServer')
            
            if self.send_zWave_network_informations():
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def send_zWave_network_destroyed_event(self, event):
        succes = False

        if self.server != False and isinstance(event, ZWaveNetworkDestroyed):
            self.server.emit('zWave_network_destroyed', event.serialize(), namespace='/HomeAutomationServer')
            
            if self.send_zWave_network_informations():
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def send_zWave_network_soft_resetted_event(self, event):
        succes = False

        if self.server != False and isinstance(event, ZWaveNetworkSoftResetted):
            self.server.emit('zWave_network_soft_resetted', event.serialize(), namespace='/HomeAutomationServer')
            
            if self.send_zWave_network_informations():
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def send_zWave_network_hard_resetted_event(self, event):
        succes = False

        if self.server != False and isinstance(event, ZWaveNetworkHardResetted):
            self.server.emit('zWave_network_hard_resetted', event.serialize(), namespace='/HomeAutomationServer')
            
            if self.send_zWave_network_informations():
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def send_module_added_event(self, event):
        succes = False

        if self.server != False and isinstance(event, ZWaveNetworkModuleAdded):
            self.server.emit('module_added', event.serialize(), namespace='/HomeAutomationServer')
                
            if self.send_zWave_modules_list_updated_event():
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def send_module_removed_event(self, event):
        succes = False

        if self.server != False and isinstance(event, ZWaveNetworkModuleRemoved):
            self.server.emit('module_removed', event.serialize(), namespace='/HomeAutomationServer')

            if self.send_zWave_modules_list_updated_event():
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes



    """controller event"""
    def send_zWave_controller_ready_event(self, event):
        succes = False

        if self.server != False and isinstance(event, ZWaveControllerReady):
            self.server.emit('zWave_controller_ready', event.serialize(), namespace='/HomeAutomationServer')
            succes = True
        else:
            succes = False

        return succes


    def send_zWave_controller_failed_event(self, event):
        succes = False

        if self.server != False and isinstance(event, ZWaveControllerFailed):
            self.server.emit('zWave_controller_failed', event.serialize(), namespace='/HomeAutomationServer')
            succes = True
        else:
            succes = False

        return succes


    def send_zWave_controller_removed_event(self, event):
        succes = False

        if self.server != False and isinstance(event, ZWaveControllerRemoved):
            self.server.emit('zWave_controller_removed', event.serialize(), namespace='/HomeAutomationServer')
            succes = True
        else:
            succes = False

        return succes


    def send_zWave_controller_resetted_event(self, event):
        """
            method called when controller is resetted
        """

        succes = False

        if self.server != False and isinstance(event, ZWaveControllerResetted):
            self.server.emit('zWave_controller_removed', event.serialize(), namespace='/HomeAutomationServer')
            succes = True
        else:
            succes = False

        return succes



    """module event"""
    def send_module_ready_event(self, event):
        succes = False

        if self.server != False and isinstance(event, ZWaveModuleReady):
            self.server.emit('module_ready', event.serialize(), namespace='/HomeAutomationServer')
                
            if self.send_module(event.moduleId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def send_module_value_modified_event(self, event):
        succes = False

        if self.server != False and isinstance(event, ZWaveModuleValueModified):
            self.server.emit('module_value_modified', event.serialize(), namespace='/HomeAutomationServer')
                
            if self.send_module(event.moduleId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def send_module_updated_event(self, event):
        succes = False

        if self.server != False and isinstance(event, ZWaveModuleUpdated):
            self.server.emit('module_updated', event.serialize(), namespace='/HomeAutomationServer')
                
            if self.send_module(event.moduleId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def send_module_renamed_event(self, event):
        succes = False

        if self.server != False and isinstance(event, ZWaveModuleRenamed):
            self.server.emit('module_renamed', event.serialize(), namespace='/HomeAutomationServer')
                
            if self.send_module(event.moduleId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def send_module_moved_event(self, event):
        succes = False

        if self.server != False and isinstance(event, ZWaveModuleMoved):
            self.server.emit('module_moved', event.serialize(), namespace='/HomeAutomationServer')
                
            if self.send_module(event.moduleId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def send_module_value_updated_event(self, event):
        succes = False

        if self.server != False and isinstance(event, ZWaveModuleValueUpdated):
            self.server.emit('module_value_updated', event.serialize(), namespace='/HomeAutomationServer')
                
            if self.send_module(event.moduleId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def send_zWave_module_healed_event(self, event):
        succes = False

        if self.server != False and isinstance(event, ZWaveModuleHealed):
            self.server.emit('zWave_module_healed', event.serialize(), namespace='/HomeAutomationServer')
                
            if self.send_module(event.moduleId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def send_zWave_module_return_route_updated_event(self, event):
        succes = False

        if self.server != False and isinstance(event, ZWaveModuleReturnRouteUpdated):
            self.server.emit('zWave_module_return_route_updated', event.serialize(), namespace='/HomeAutomationServer')
                
            if self.send_module(event.moduleId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def send_zWave_module_neighbors_updated_event(self, event):
        succes = False

        if self.server != False and isinstance(event, ZWaveModuleNeighborsUpdated):
            self.server.emit('module_neighbors_updated', event.serialize(), namespace='/HomeAutomationServer')
                
            if self.send_module(event.moduleId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def send_zWave_module_network_updated_event(self, event):
        succes = False

        if self.server != False and isinstance(event, ZWaveModuleNetworkUpdated):
            self.server.emit('module_network_updated', event.serialize(), namespace='/HomeAutomationServer')
                
            if self.send_module(event.moduleId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def send_zWave_module_informations_refreshed_event(self, event):
        succes = False

        if self.server != False and isinstance(event, ZWaveModuleInformationsRefreshed):
            self.server.emit('module_informations_refreshed', event.serialize(), namespace='/HomeAutomationServer')
                
            if self.send_module(event.moduleId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def send_zWave_module_value_refreshed_event(self, event):
        succes = False

        if self.server != False and isinstance(event, ZWaveModuleValueRefreshed):
            self.server.emit('module_value_refreshed', event.serialize(), namespace='/HomeAutomationServer')
                
            if self.send_module(event.moduleId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes



    """LIGHT CONTROLLER EVENT"""
    def send_light_controller_level_updated_event(self, event):
        succes = False

        if self.server != False and isinstance(event, ZWaveLightIntensityModified):
            self.server.emit('light_controller_level_updated', event.serialize(), namespace='/HomeAutomationServer')
                
            if self.send_module(event.moduleId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def send_light_controller_color_updated_event(self, event):
        succes = False
        

        #event.serialize()
        #and isinstance(event, ZWaveLightColorModified)

        if self.server != False:
            try:
                self.server.emit('light_controller_color_updated', {}, namespace='/HomeAutomationServer')
                self.server.sleep(0.1)
                succes = True
            except:
                succes = False
            """ 
            if self.send_module(event.moduleId):
                succes = True
            else:
                succes = False
            """
        else:
            succes = False

        if succes:
            print('iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')

        return succes


    def send_light_controller_switching_on_event(self, event):
        succes = False

        if self.server != False and isinstance(event, ZWaveLightSettingOn):
            #self.server.emit('light_controller_switching_on', event.serialize(), namespace='/HomeAutomationServer')
                
            if self.send_module(event.moduleId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def send_light_controller_switching_off_event(self, event):
        succes = False

        if self.server != False and isinstance(event, ZWaveLightSettingOff):
            self.server.emit('light_controller_switching_off', event.serialize(), namespace='/HomeAutomationServer')
                
            if self.send_module(event.moduleId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes



    """RELAY EVENT"""
    def send_relay_switching_on_event(self, event):
        succes = False

        if self.server != False and isinstance(event, ZWaveRelaySettingOn):
            self.server.emit('relay_switching_on', event.serialize(), namespace='/HomeAutomationServer')
                
            if self.send_module(event.moduleId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def send_relay_switching_off_event(self, event):
        succes = False

        if self.server != False and isinstance(event, ZWaveRelaySettingOff):
            self.server.emit('relay_switching_off', event.serialize(), namespace='/HomeAutomationServer')
                
            if self.send_module(event.moduleId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes



    """SENSOR EVENT"""
    def send_motion_detected_event(self, event):
        succes = False

        if self.server != False and isinstance(event, ZWaveMotionDetection):
            self.server.emit('motion_detected', event.serialize(), namespace='/HomeAutomationServer')
                
            if self.send_module(event.moduleId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def send_acces_openned_event(self, event):
        succes = False

        if self.server != False and isinstance(event, ZWaveAccesOpened):
            self.server.emit('acces_openned', event.serialize(), namespace='/HomeAutomationServer')
                
            if self.send_module(event.moduleId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def send_acces_closed_event(self, event):
        succes = False

        if self.server != False and isinstance(event, ZWaveAccesClosed):
            self.server.emit('acces_closed', event.serialize(), namespace='/HomeAutomationServer')
                
            if self.send_module(event.moduleId):
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    #value event
    def module_value_modified(self, module, valueId):
        succes = event = eventDatetime = False

        if isinstance(module, ZWaveModule):
            eventDatetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            event = ZWaveModuleValueModified(module.id, eventDatetime, module.location, valueId)
            self.eventList.append(event)
            print(event)

            if event in self.eventList:
                succes = True
            else:
                succes = False
        else:
            succes = False

        if self.server != False and succes:
            if self.send_module_value_modified_event(event):
                succes = True
            else:
                succes = False
        else:
            pass

        return succes


    
    ###SEND INFORMATIONS###
    def send_zWave_network_informations(self):
        succes = False

        if self.server != False:
            self.server.emit('send_zWave_network_informations', self.serialize(), namespace='/HomeAutomationServer')
            succes = True
        else:
            succes = False

        return succes


    def send_modules_list(self):
        succes = False

        modulesList = data = False

        if self.server != False:
            data = {}
            modulesList = []

            for module in self.modulesList:
                modulesList.append(module.serialize())

            data['data'] = modulesList

            self.server.emit('send_zWave_module_list', data, namespace='/HomeAutomationServer')
        else:
            succes = False


    def send_module(self, moduleId):
        succes = module = False

        module = self.get_module(moduleId)

        if self.server != False and isinstance(module, ZWaveModule):
            self.server.emit('send_zWave_module', module.serialize(), namespace='/HomeAutomationServer')
            succes = True
        else:
            succes = False

        return succes