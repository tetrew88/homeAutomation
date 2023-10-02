#!/usr/bin/python3

import os


if __name__ == '__main__':
    from classes.homeAutomationServerInstaller import *
else:
    from .classes.homeAutomationServerInstaller import *


def install():
    succes = supervisorInstalled = zWaveNetworkInstalled = zWaveNetworkActivityChoice =zWaveNetworkActivityState = False
    configFileCreated = homeAutomationServerSupervisorConfigFileCreated = False
    
    scriptPath = os.path.dirname(os.path.abspath(__file__))
    homeAutomationServerInstaller = HomeAutomationServerInstaller(scriptPath)

    if homeAutomationServerInstaller.dowload_supervisor():
        supervisorInstalled = True
    else:
        supervisorInstalled = False

    if supervisorInstalled:
        if homeAutomationServerInstaller.install_zwaveNetwork():
            zWaveNetworkInstalled = True
        else:
            zWaveNetworkInstalled = False


    if supervisorInstalled and zWaveNetworkInstalled:
        if homeAutomationServerInstaller.create_home_automation_server_config_file(False, "disabled"):
            configFileCreated = True
        else:
            configFileCreated = False

        if configFileCreated:
            if homeAutomationServerInstaller.create_automation_server_supervisor_config_file():
                homeAutomationServerSupervisorConfigFileCreated = True
            else:
                homeAutomationServerSupervisorConfigFileCreated = False
        else:
            homeAutomationServerSupervisorConfigFileCreated = False
    else:
        configFileCreated = False
        homeAutomationServerSupervisorConfigFileCreated = False


    if supervisorInstalled and homeAutomationServerSupervisorConfigFileCreated\
        and configFileCreated and supervisorInstalled and zWaveNetworkInstalled:

        while zWaveNetworkActivityState != "n" and zWaveNetworkActivityState != "o":
            zWaveNetworkActivityChoice = input("\nVoulez-vous activer le reseau zwave ?(o/n): ").lower()

            zWaveNetworkActivityState = zWaveNetworkActivityChoice

        if homeAutomationServerInstaller.set_home_automation_server_configuration_booleean_control(True):
            if zWaveNetworkActivityState == 'o':
                if homeAutomationServerInstaller.set_zWaveNetwork_activity_state("activated"):
                    succes = True
                else:
                    succes = False
            else:
                if homeAutomationServerInstaller.set_zWaveNetwork_activity_state("disabled"):
                    succes = True
                else:
                    succes = False
        else:
            succes = False
    else:
        succes = False


    if succes:
        print("serveur installer avec succes")
    else:
        print("erreur lors de l'installation du serveur")

    return succes


if __name__ == '__main__':
	install()