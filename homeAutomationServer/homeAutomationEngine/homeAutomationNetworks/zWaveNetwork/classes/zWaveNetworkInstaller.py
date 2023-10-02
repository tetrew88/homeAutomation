import subprocess
import re
import json
import getpass
import os


class ZWaveNetworkInstaller:
    """
        class contained all information and functionnality of the zwave network installer

            attributes:
                script path
                zwave network config file path

                assigned zwave controller name
                assigned zwave controller path

            propertys:
                network configured

            methods:
                get_zwave_controller_path
                get_zwave_config_folder_path
                get_controller_vendor_id
                get_controller_product_id

                create_zwave_network_config_file
                create_assignation_rule_files

                assign_fixed_usb_port_names_to_controller

                set_zwave_network_configuration_booleean_control

                reload_udev_rules

                move_config_file
    """

    def __init__(self, scriptPath):
        self.scriptPath = scriptPath
        self.zWaveNetworkConfigFilePath = scriptPath + "/configs/zWaveNetworkConfig.json"
        
        self.assignedZwaveControllerName = "ttyUSB_CONTROLLER"
        self.assignedZwaveControllerPath = "/dev/" + self.assignedZwaveControllerName


    """PROPERTY"""
    @property
    def networkConfigured(self):
        """
            bolléan use for know if server was configured 
            functioning:
                1.open config file
                2.collecte data dictionnary
                3.check if boolean was on true or false
                4.return result
                
            return:
                if server was configured return true
                else return false 
        """
        
        networkConfigured = data = False

        #open config file
        try:
            with open(self.zWaveNetworkConfigFilePath, 'r') as f:
                #collecte data dictionnary
                data = json.load(f)
        except:
            networkConfigured = False
            data = False
            

        if data != False:
            #check if boolean was on true or false
            try:
                networkConfigured = data['networkConfigured']
            except:
                networkConfigured = False
        else:
            networkConfigured = False

        #return
        return networkConfigured



    """METHODS"""
    """GET METHOD"""
    def get_zwave_controller_path(self):
        """
            method used for collect the path of the zwave controller

            functioning:
                1.collect the path
                2.check if path exist
                3.return

            return:
                if succes return path of the controller
                else return False
        """

        zwaveControllerPath = ""
        pathExist = False

        #collect the path
        zwaveControllerPath = input("\nentrer le chemin vers le controller zwave(ex: /dev/ttyACM0): ")

        #check if path exist
        try:
            with open(zwaveControllerPath, 'r') as f:
                pathExist = True
        except:
            print("controller introuvable")
            pathExist = False

        #return
        if pathExist:
            return zwaveControllerPath
        else:
            return False


    def get_zwave_config_folder_path(self):
        """
            method used for collect the path of the zwave config folder

            functioning:
                1.create server request
                2.execute server request with subprocess
                3.check subprocess return code
                4.return

            return:
                if succes return path of the zwave config file
                else return False
        """

        #create server request
        searchRequest = "find /home -name ozw_config | head -1"
        zwaveConfigFolderPath = ""
        succes = False

        try:
            #execute server request with subprocess
            proc = subprocess.Popen(searchRequest, shell=True, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE, executable="/bin/bash")
            output, error = proc.communicate()
            proc.wait()


            #check subprocess return code
            if proc.returncode == 0:
                zwaveConfigFolderPath = str(output.decode()).replace('\n', '')
            else:
                error = str(error.decode()).replace('\n', '')
                zwaveConfigFolderPath = ""

            if zwaveConfigFolderPath != "":
                succes = True
            else:
                succes = False
        except:
            succes = False

        #return
        if succes:
            return zwaveConfigFolderPath
        else:
            return False


    def get_controller_vendor_id(self, controllerPath):
        """
            Method called for getting the controller vendor id

                functionning:
                    1.test controllerPath conformity
                    2.used subprocces for getting vendor id
                    3.check output
                    4.return

                return:
                    if succes return vendor id
                    else return false
        """

        succes = vendorId = False

        #test controllerPath conformity
        if isinstance(controllerPath, str):
            getVendorIdRequest = "udevadm info --name={} --attribute-walk | grep -m 1 ATTRS{}".format(controllerPath, '{idVendor}')

            try:
                #used subprocces for getting vendor id
                proc = subprocess.Popen(getVendorIdRequest, shell=True, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE, executable="/bin/bash")
                output, error = proc.communicate()
                proc.wait()

                #check output
                if proc.returncode == 0:
                    vendorId = re.findall('"(.*?)"', output.decode().replace(" ", ""))[0]
                    if vendorId != "":
                        pass
                    else:
                        vendorId = False
                else:
                    error = str(error).replace('\n', '')
                    vendorId = False
            except:
                vendorId = False
        else:
            vendorId = False

        if vendorId != False:
            succes = True
        else:
            succes = False

        #return
        if succes:
            return vendorId
        else:
            return False


    def get_controller_product_id(self, controllerPath):
        """
            Method called for getting the controller product id

                functionning:
                    1.test controllerPath conformity
                    2.used subprocces for getting product id
                    3.check output
                    4.return

                return:
                    if succes return vendor id
                    else return false
        """
        
        succes = productId = False

        #test controllerPath conformity
        if isinstance(controllerPath, str):
            getProductIdRequest = "udevadm info --name={} --attribute-walk | grep -m 1 ATTRS{}".format(controllerPath, '{idProduct}')

            try:
                #used subprocces for getting product id
                proc = subprocess.Popen(getProductIdRequest, shell=True, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE, executable="/bin/bash")
                output, error = proc.communicate()
                proc.wait()

                #check output
                if proc.returncode == 0:
                    productId = re.findall('"(.*?)"', output.decode().replace(" ", ""))[0]
                else:
                    error = str(error).replace('\n', '')
                    productId = False
            except:
                productId = False
        else:
            productId = False

        if productId != False:
            succes = True
        else:
            succes = False

        #return
        if succes:
            return productId
        else:
            return False



    """CREATE METHOD"""
    def create_zwave_network_config_file(self, zwaveControllerPath, zWaveConfigFolderPath, networkConfigured):
        """
            method used for create the zwave network config file

            functioning:
                1.set the data dictionnary
                2.open/create zwave network config file
                3.write data dictionnary in file
                4.return

            return:
                if succes return True
                else return False
        """

        succes = False
        data = {}

        if isinstance(zwaveControllerPath, str) and \
            isinstance(zWaveConfigFolderPath, str) and \
                isinstance(networkConfigured, bool):

            #set the data dictionnary
            data["zwaveControllerPath"] = zwaveControllerPath
            data["assignedZwaveControllerPath"] = self.assignedZwaveControllerPath
            data["zWaveConfigFolderPath"] = zWaveConfigFolderPath
            data["networkConfigured"] = networkConfigured
            data["status"] = "activated"

            try:
                #open/create database config file
                with open(self.zWaveNetworkConfigFilePath, 'w') as f:
                    #write data dictionnary in file
                    json.dump(data, f, indent=4)
                succes = True
            except:
                succes = False
        else:
            succes = False

        #return
        return succes


    def create_assignation_rule_files(self, productId, vendorId):
        """
            method called for create the assignation rule file

                functionning:
                    1.create assignation file with controller information
                    2.moved file in udev rules folder
                    3.check existance of the new file in udev rules
                    4.return

                return:
                    if succes return true
                    else return false
        """

        ruleFilePath = self.scriptPath + "/configs/10-usb-serial.rules"
        succes = assignationRequest = fileCreated = fileMoved = False

        if vendorId and productId:
            #create assignation file with controller information
            assignationRequest = 'SUBSYSTEM=="tty", ATTRS{}=="{}", ATTRS{}=="{}", SYMLINK+="{}"'.format("{idProduct}", productId, "{idVendor}", vendorId, self.assignedZwaveControllerName)
        
            try:
                with open(ruleFilePath, "w") as f:
                    f.write(assignationRequest)

                fileCreated = True
            except Exception as error:
                fileCreated = False

            if fileCreated:
                #moved file in udev rules folder
                if self.move_config_file(ruleFilePath, "/etc/udev/rules.d/10-usb-serial.rules"):
                    fileMoved = True
                else:
                    fileMoved = False
            else:
                fileMoved = False
        else:
            fileCreated = False

        #check existance of the new file in udev rules
        if os.path.exists("/etc/udev/rules.d/10-usb-serial.rules"):
            succes = True
        else:
            succes = False

        #return
        return succes



    """ASSIGNATION METHODS"""
    def assign_fixed_usb_port_names_to_controller(self, controllerPath): 
        """
            method used for assigned an fix name to the controller

            functioning:
                1.get controller vendor id
                2.get controller product id
                3.create assignation file with controller information
                4.reload udev rules
                5.return

            return:
                if succes return True
                else return False
        """

        vendorId = productId = False

        #get controller vendor id
        vendorId = self.get_controller_vendor_id(controllerPath)
        #get controller product id
        productId = self.get_controller_product_id(controllerPath)

        if vendorId and productId:
            #create assignation file with controller information
            if self.create_assignation_rule_files(productId, vendorId):
                #reload udev rules
                if self.reload_udev_rules():
                    succes = True
                else:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        return succes



    """SET METHODS"""
    def set_zwave_network_configuration_booleean_control(self, value):
        """
            method used for set booléen of configuration control in zwave network config file

            functioning:
                1.check if value is an booleean
                2.open config file
                3.collecte data dictionnary
                4.set booléen on value
                5.return

            return:
                if succes return true
                else return false 
        """
        
        succes = data = False

        #check if value is an booleean
        if isinstance(value, bool):
            #open config file
            try:
                with open(self.zWaveNetworkConfigFilePath, 'r') as f:
                    #collecte data dictionnary
                    data = json.load(f)
            except:
                succes = False

            if data != False:
                try:
                    #set booléen on value
                    data['networkConfigured'] = value
                    #open config file
                    try:
                        with open(self.zWaveNetworkConfigFilePath, 'w') as f:
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


    
    """RELOAD METHOD"""
    def reload_udev_rules(self):
        """
            method used for reload the udev rules

                functionning:
                    1.use subprocces for reload udev rules
                    2.check subprocess return code
                    3.return

                return:
                    if succes return true
                    else return false
        """

        succes = False

        refreshRequest = "sudo udevadm trigger"

        try:
            #use subprocces for reload udev rules
            proc = subprocess.Popen(refreshRequest, shell=True, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE, executable="/bin/bash")
            output, error = proc.communicate()
            proc.wait()

            #check subrocess return code
            if proc.returncode == 0:
                succes=True
            else:
                succes = False
        except:
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