#!/usr/bin/python3

import os


if __name__ == '__main__':
    from classes.homeAutomationSystemInstaller import *
else:
    from .classes.homeAutomationSystemInstaller import *


def install():
    succes = supervisorInstalled = homeDatabaseInstalled = False
    configFileCreated = homeAutomationSystemSupervisorConfigFileCreated = False
    homeAutomationServerIp = False

    scriptPath = os.path.dirname(os.path.abspath(__file__))
    homeAutomationSystemInstaller = HomeAutomationSystemInstaller(scriptPath)

    if homeAutomationSystemInstaller.dowload_supervisor():
        supervisorInstalled = True
    else:
        supervisorInstalled = False

    if supervisorInstalled:
        if homeAutomationSystemInstaller.install_home_database():
            homeDatabaseInstalled = True
        else:
            homeDatabaseInstalled = False

    if supervisorInstalled and homeDatabaseInstalled:
        homeAutomationServerIp = homeAutomationSystemInstaller.get_homeAutomation_server_ip()

    if supervisorInstalled and homeDatabaseInstalled and homeAutomationServerIp:
        if homeAutomationSystemInstaller.create_home_automation_system_config_file(False, homeAutomationServerIp):
            configFileCreated = True
        else:
            configFileCreated = False

        if configFileCreated:
            if homeAutomationSystemInstaller.create_home_automation_system_supervisor_config_file():
                homeAutomationSystemSupervisorConfigFileCreated = True
            else:
                homeAutomationSystemSupervisorConfigFileCreated = False
        else:
            homeAutomationSystemSupervisorConfigFileCreated = False
    else:
        configFileCreated = False
        homeAutomationSystemSupervisorConfigFileCreated = False


    if supervisorInstalled and homeAutomationSystemSupervisorConfigFileCreated\
        and configFileCreated and homeDatabaseInstalled:

        if homeAutomationSystemInstaller.set_home_automation_system_configuration_booleean_control(True):
            succes = True
        else:
            succes = False
    else:
        succes = False


    if succes:
        print("systeme domotique installer avec succes")
    else:
        print("erreur lors de l'installation du systeme domotique")

    return succes



if __name__ == '__main__':
    install()