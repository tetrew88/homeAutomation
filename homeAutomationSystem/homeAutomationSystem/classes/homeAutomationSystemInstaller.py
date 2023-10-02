import subprocess
import re
import json
import getpass
import os
import sys

sys.path.append("..")
from homeAutomationSystem.homeDatabase.install import install as homeDatabase_installation


class HomeAutomationSystemInstaller:
    def __init__(self, scriptPath):
        self.scriptPath = scriptPath
        self.homeAutomationSystemConfigFilePath = scriptPath + "/configs/homeAutomationSystemConfig.json"


    """METHODS"""
    """GET METHODS"""
    def get_base_supervisor_config(self, supervisorConfigFilePath):
        """
            method used for gettinf base supervisor config

                functionnality:

                return:
                    if succes return base supervisor config
                    else return False
        """

        succes = fileContent = False

        try:
            with open(supervisorConfigFilePath, "r") as f:
                fileContent = f.read()
        except:
                fileContent = False

        if fileContent != False:
            succes = True
        else:
            succes = False

        if succes:
            return fileContent
        else:
            return False

    
    def get_homeAutomation_server_ip(self):
        homeAutomationServerIp = False

        homeAutomationServerIp  = input("\nEntrer l'ip du serveur domotique")

        return homeAutomationServerIp



    """DOWNLOAD METHODS"""
    def dowload_supervisor(self):
        """
            method used for dowload supervisor

            functioning:
                1.create server request
                2.execute server request with subprocess
                3.check subprocess return code
                4.return

            return:
                if succes return True
                else return False
        """

        succes = False

        #create server request
        serverRequest = 'sudo apt-get install -y supervisor'

        try:
            #execute server request with subprocess
            proc = subprocess.Popen(serverRequest, shell=True, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE, executable="/bin/bash")
            output, error = proc.communicate()
            proc.wait()

            #check subprocess return code
            if proc.returncode == 0:
                succes = True
            else:
                print("Erreur: {}".format(error.decode()))
                succes = False
        except:
            succes = False

        #return
        return succes



    """CREATE METHODS"""
    def create_home_automation_system_config_file(self, systemConfigured, homeAutomationServerIp):
        succes = False
        data = {}

        if isinstance(systemConfigured, bool) :
            #set the data dictionnary
            data["systemConfigured"] = systemConfigured
            data["homeAutomationServerIp"] = homeAutomationServerIp

            try:
                #open/create database config file
                with open(self.homeAutomationSystemConfigFilePath, 'w') as f:
                    #write data dictionnary in file
                    json.dump(data, f, indent=4)

                succes = True
            except:
                succes = False
        else:
            succes = False

        #return
        return succes


    def create_home_automation_system_supervisor_config_file(self):
        succes = fileCopied = baseConfigFileExist = fileMoved = supervisorConfigFileCreated = False

        supervisorBaseConfigFilePath = self.scriptPath + "/configs/supervisorBaseConfig.txt"
        newSupervisorConfigFilePath = self.scriptPath + "/configs/newSupervisorConfig"

        #copy the base config file used for example
        if self.copy_config_file(supervisorBaseConfigFilePath, newSupervisorConfigFilePath):
            #modify data of the new file
            if self.set_supervisor_config_file(newSupervisorConfigFilePath):
                #moved the file to the supervisor conf.d folder
                if self.move_config_file(newSupervisorConfigFilePath, "/etc/supervisor/conf.d/automationSystem.conf"):
                    succes = True
                else:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        #check existance of the new file in conf.d
        if os.path.exists("/etc/supervisor/conf.d/automationSystem.conf"):
            succes = True
        else:
            succes = False

        #return
        return succes



    """COPY METHODS"""
    def copy_config_file(self, filePath, newFilePath):
        """
            method use for copy config file

                functionning:
                    1.check if the file exist
                    2.use subproccess for copy the file
                    3.check the return code
                    4.return
                return:
                    if succes return True
                    else return False
        """

        succes = fileExist = False

        copyRequest = "cp {} {}".format(filePath, newFilePath)

        #check if the file exist
        try:
            with open(filePath, 'r') as f:
                pass
            fileExist = True
        except:
            fileExist = False

        if fileExist != False:
            #use subproccess for copy the file
            try:
                proc = subprocess.Popen(copyRequest, shell=True, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE, executable="/bin/bash")
                output, error = proc.communicate()
                proc.wait()

                #check the return code
                if proc.returncode == 0:
                    fileCopied = True
                else:
                    error = error.decode().replace('\n', '')
                    fileCopied = False
            except:
                fileCopied = False
        else:
            fileCopied = False

        if fileCopied:
            succes = True
        else:
            succes = False

        #return
        return succes



    """MOVE METHODS"""
    def move_config_file(self, filePath, newEmplacementPath):
        """
            method use for move config file

                functionning:
                    1.check if the file exist
                    2.use subproccess for move the file
                    3.check the return code
                    4.return
                return:
                    if succes return True
                    else return False
        """
        
        succes = fileExist = False

        moveRequest = "sudo mv -f {} {}".format(filePath, newEmplacementPath)

        #check if the file exist
        try:
            with open(filePath, "r") as f:
                pass
            fileExist = True
        except:
            fileExist = False

        if fileExist:
            try:
                #use subproccess for move the file
                proc = subprocess.Popen(moveRequest, shell=True, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE, executable="/bin/bash")
                output, error = proc.communicate()
                proc.wait()

                #check the return code
                if proc.returncode == 0:
                    fileMoved = True
                else:
                    error = error.decode()
                    fileMoved = False
            except:
                fileMoved = False
        else:
            fileMoved = False

        if fileMoved:
            succes = True
        else:
            succes = False

        #return
        return succes



    """SET METHODS"""
    def set_home_automation_system_configuration_booleean_control(self, value):
        succes = data = False

        #check if value is an booleean
        if isinstance(value, bool):
            #open config file
            try:
                with open(self.homeAutomationSystemConfigFilePath, 'r') as f:
                    #collecte data dictionnary
                    data = json.load(f)
            except:
                succes = False

            if data != False:
                try:
                    #set booléen on value
                    data['systemConfigured'] = value
                    #open config file
                    try:
                        with open(self.homeAutomationSystemConfigFilePath, 'w') as f:
                            #write data dictionnary in file
                            json.dump(data, f, indent=4)
                            succes = True
                    except:
                        succes = False
                except:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        #return
        return succes


    def set_supervisor_config_file(self, supervisorConfigFilePath):
        """
            method called for set the supervisor config file

                1.get the base content
        """

        succes = fileContent = supervisorConfigFileModified = False

        command = "python3 main.py"
        username = getpass.getuser()
        directory = self.scriptPath
        
        if username != False:
            #get the base content
            fileContent = self.get_base_supervisor_config(supervisorConfigFilePath)

            if fileContent != False:
                #modify data of the new file
                fileContent = fileContent.replace("COMMAND", command)
                fileContent = fileContent.replace("USERNAME", username)
                fileContent = fileContent.replace("PATH_TO_APPLICATION", directory)

                try:
                    with open(supervisorConfigFilePath, "w") as f:
                        f.write(fileContent)

                    supervisorConfigFileModified = True
                except:
                    supervisorConfigFileModified = False
            else:
                supervisorConfigFileModified = False
        else:
            supervisorConfigFileModified = False


        if supervisorConfigFileModified:
            succes = True
        else:
            succes = False

        return succes



    """INSTALLATION METHODS"""
    def install_home_database(self):
        succes = False

        if homeDatabase_installation():
            succes = True
        else:
            succes = False

        return succes