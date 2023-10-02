#!/usr/bin/python3

import os


if __name__ == '__main__':
    from classes.zWaveNetworkInstaller import *
else:
    from .classes.zWaveNetworkInstaller import *



def install():
    succes = zwaveControllerPath = zWaveConfigFolderPath = False
    usbPortNameAssigned = configFileCreated = False
    
    scriptPath = os.path.dirname(os.path.abspath(__file__))
    zWaveNetworkInstaller = ZWaveNetworkInstaller(scriptPath)

    zwaveControllerPath = zWaveNetworkInstaller.get_zwave_controller_path()
    zWaveConfigFolderPath = zWaveNetworkInstaller.get_zwave_config_folder_path()

    if zwaveControllerPath != False and zWaveConfigFolderPath != False:
        if zWaveNetworkInstaller.assign_fixed_usb_port_names_to_controller(zwaveControllerPath):
            usbPortNameAssigned = True
        else:
            usbPortNameAssigned = False
    else:
        usbPortNameAssigned = False

    if usbPortNameAssigned:
        if zWaveNetworkInstaller.create_zwave_network_config_file(zwaveControllerPath, zWaveConfigFolderPath, False):
            configFileCreated = True
        else:
            configFileCreated = False
    else:
        configFileCreated = False

    
    if configFileCreated and usbPortNameAssigned:
        if zWaveNetworkInstaller.set_zwave_network_configuration_booleean_control(True):
            succes = True
        else:
            succes = False
    else:
        succes = False

    if succes:
        print("réseau zwave installer avec succes")
    else:
        print("erreur lors de l'installation du réseau zwave")

    return succes



if __name__ == '__main__':
	install()