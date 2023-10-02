#!/usr/bin/python3

import os
import mock
import sys
import json
import subprocess

sys.path.append("..")

from zWaveNetwork.classes.zWaveNetworkInstaller import *
from unittest.mock import patch, mock_open, MagicMock

class Test_ZWaveNetworkInstaller:
    """
        class used for test the zwaveNetworkInstaller
        
            Attributes:
                script path (path of the main script (for files manipulation))
				zwave network installer
                zwave network config file path

            tests:

    """

    """constructor"""
    scriptPath = os.path.dirname(os.path.abspath(__file__))
    zwaveNetworkInstaller = ZWaveNetworkInstaller(os.path.dirname(os.path.abspath(__file__)))
    zWaveNetworkConfigFile = os.path.dirname(os.path.abspath(__file__)) + "/configs/zWaveNetworkConfig.json"


    """TESTS"""
    def test_networkConfigured_property(self):
        """
            test if method return true or false
            test if method return false if error
            test if method return good values
        """

        assert isinstance(self.zwaveNetworkInstaller.networkConfigured, bool)

        open_mock = mock_open()
        jsonMock = MagicMock( side_effect = [ { "networkConfigured": True } ] )

        with patch("builtins.open", open_mock, create=False):
            with patch("json.load", jsonMock):
                #test if method return the good values
                assert self.zwaveNetworkInstaller.networkConfigured == True
                jsonMock = MagicMock( side_effect = [ { "networkConfigured": False } ] )
                assert self.zwaveNetworkInstaller.networkConfigured == False

            #test if method return false if error
            open_mock.side_effect = IOError()
            assert self.zwaveNetworkInstaller.networkConfigured == False


    def test_getting_zwave_controller_path(self):
        """
            1.test if method return the controller Path
            2.test if method detect wrong input
        """

        open_mock = mock_open()

        #test if method return the controller Path
        with mock.patch('builtins.input', return_value="/dev/ttyACM0"):
            with patch("builtins.open", open_mock, create=False):
                assert self.zwaveNetworkInstaller.get_zwave_controller_path() == "/dev/ttyACM0"

        #test if method detect wrong input type
        with mock.patch('builtins.input', return_value=0):
            assert self.zwaveNetworkInstaller.get_zwave_controller_path() == False


    @patch("subprocess.Popen")
    def test_getting_zwave_config_folder_path(self, mock_subproc_popen):
        """
            1.test if method return the zwave config folder
            2.test if method detect error
            3.test if method detect inexistance of folder
        """

        process_mock = mock.Mock()

        #test if method return the zwave config folder
        attrs = {"communicate.return_value": (b'/test', b"error"),
        "returncode": 0}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        assert self.zwaveNetworkInstaller.get_zwave_config_folder_path() == "/test"

        #test if method detect error
        attrs = {"communicate.return_value": ("b'/test'", b"error"),
        "returncode": 1}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock

        assert self.zwaveNetworkInstaller.get_zwave_config_folder_path() == False

        #test if method detect inexistance of folder
        attrs = {"communicate.return_value": (b"", b"error"),
        "returncode": 0}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock

        assert self.zwaveNetworkInstaller.get_zwave_config_folder_path() == False


    @patch("subprocess.Popen")
    def test_getting_controller_vendor_id(self, mock_subproc_popen):
        """
            1.test if method return good value if succes
            2.test if method detect error in subprocces call
            3.test if method detect wrong answer of the request
        """

        process_mock = mock.Mock()

        #test if method return good value if succes
        attrs = {"communicate.return_value": (b'ATTRS{idVendor}=="0658"', b"error"),
        "returncode": 0}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        assert self.zwaveNetworkInstaller.get_controller_vendor_id("") == "0658"

        #test if method detect error in subprocces call
        attrs = {"communicate.return_value": (b'ATTRS{idVendor}=="0658"', b"error"),
        "returncode": 1}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        assert self.zwaveNetworkInstaller.get_controller_vendor_id("") == False

        #test if method detect wrong answer of the request
        attrs = {"communicate.return_value": (b"", b"error"),
        "returncode": 0}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        assert self.zwaveNetworkInstaller.get_controller_vendor_id("") == False


    @patch("subprocess.Popen")
    def test_getting_controller_product_id(self, mock_subproc_popen):
        """
            1.test if method return good value if succes
            2.test if method detect error in subprocces call
            3.test if method detect wrong answer of the request
        """

        process_mock = mock.Mock()

        #test if method return good value if succes
        attrs = {"communicate.return_value": (b'ATTRS{idProduct}=="0658"', b"error"),
        "returncode": 0}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        assert self.zwaveNetworkInstaller.get_controller_product_id("") == "0658"

        #test if method detect error in subprocces call
        attrs = {"communicate.return_value": (b'ATTRS{idProduct}=="0658"', b"error"),
        "returncode": 1}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        assert self.zwaveNetworkInstaller.get_controller_product_id("") == False

        #test if method detect wrong answer of the request
        attrs = {"communicate.return_value": (b"", b"error"),
        "returncode": 0}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        assert self.zwaveNetworkInstaller.get_controller_product_id("") == False


    def test_create_assignation_rule_files(self):
        """
            1.test if method return true if succes
            2.test if method detect error during creating file
            3.test if methiod detect error during moving file
            4.test if method detect file inexistence

        """

        open_mock = mock_open()

        #test if method return true if succes
        with patch("builtins.open", open_mock, create=False):
            with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.move_config_file') as mockedMovingConfigFile:
                mockedMovingConfigFile.return_value = True

                with mock.patch('os.path.exists') as mockedFileExist:
                        mockedFileExist.return_value = True

                        assert self.zwaveNetworkInstaller.create_assignation_rule_files("1", "1") == True

        #test if method detect error during creating file
        with patch("builtins.open", open_mock, create=False):
            open_mock.side_effect = IOError()

            with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.move_config_file') as mockedMovingConfigFile:
                mockedMovingConfigFile.return_value = True

                with mock.patch('os.path.exists') as mockedFileExist:
                        mockedFileExist.return_value = False

                        assert self.zwaveNetworkInstaller.create_assignation_rule_files("1", "1") == False

        #test if methiod detect error during moving file
        with patch("builtins.open", open_mock, create=False):
            with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.move_config_file') as mockedMovingConfigFile:
                mockedMovingConfigFile.return_value = False

                with mock.patch('os.path.exists') as mockedFileExist:
                        mockedFileExist.return_value = False

                        assert self.zwaveNetworkInstaller.create_assignation_rule_files("1", "1") == False

        #test if method detect file inexistence
        with patch("builtins.open", open_mock, create=False):
            with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.move_config_file') as mockedMovingConfigFile:
                mockedMovingConfigFile.return_value = True

                with mock.patch('os.path.exists') as mockedFileExist:
                        mockedFileExist.return_value = False

                        assert self.zwaveNetworkInstaller.create_assignation_rule_files("1", "1") == False

    
    @patch("subprocess.Popen")
    def test_moving_config_file(self, mock_subproc_popen):
        """
            1.test if method return true if succes
            2.test if method detect file inexistance
            3.check if method detect error durring subprocces call
        """
        open_mock = mock_open()
        
        #test if method return true if succes
        with patch("builtins.open", open_mock, create=False):
            process_mock = mock.Mock()
            attrs = {"communicate.return_value": (b"output", b"error"),
            "returncode": 0}
            process_mock.configure_mock(**attrs)
            mock_subproc_popen.return_value = process_mock

            assert self.zwaveNetworkInstaller.move_config_file("test", "newTest") == True

        #test if method detect file inexistance
        with patch("builtins.open", open_mock, create=False):
            open_mock.side_effect = IOError()
            
            assert self.zwaveNetworkInstaller.move_config_file("test", "newTest") == False

        #check if method detect error durring subprocces call
        with patch("builtins.open", open_mock, create=False):

            process_mock = mock.Mock()
            attrs = {"communicate.return_value": (b"output", b"error"),
            "returncode": 1}
            process_mock.configure_mock(**attrs)
            mock_subproc_popen.return_value = process_mock

            assert self.zwaveNetworkInstaller.move_config_file("test", "newTest") == False


    def test_assignating_fixed_usb_port_names_to_controller(self):
        """
            1.test if method return true if succes
            2.test if method detect error during getting vendor id
            3.test if method detect error during getting product id
            4.test if method detect error during udev file creation
            5.test if method detect error during udev rules reloading
        """

        #test if method return true if succes
        with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.get_controller_vendor_id') as mockedgettingVendorId:
            mockedgettingVendorId.return_value = "1"

            with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.get_controller_product_id') as mockedgettingProductId:
                mockedgettingProductId.return_value = "1"

                with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.create_assignation_rule_files') as mockedCreatingAssignationRulesFiles:
                    mockedCreatingAssignationRulesFiles.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.reload_udev_rules') as mockedReloadingUdevRules:
                        mockedReloadingUdevRules.return_value = True

                        assert self.zwaveNetworkInstaller.assign_fixed_usb_port_names_to_controller("") == True

        #test if method detect error during getting vendor id
        with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.get_controller_vendor_id') as mockedgettingVendorId:
            mockedgettingVendorId.return_value = False

            with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.get_controller_product_id') as mockedgettingProductId:
                mockedgettingProductId.return_value = "1"

                with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.create_assignation_rule_files') as mockedCreatingAssignationRulesFiles:
                    mockedCreatingAssignationRulesFiles.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.reload_udev_rules') as mockedReloadingUdevRules:
                        mockedReloadingUdevRules.return_value = True

                        assert self.zwaveNetworkInstaller.assign_fixed_usb_port_names_to_controller("") == False

        #test if method detect error during getting product id
        with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.get_controller_vendor_id') as mockedgettingVendorId:
            mockedgettingVendorId.return_value = "1"

            with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.get_controller_product_id') as mockedgettingProductId:
                mockedgettingProductId.return_value = False

                with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.create_assignation_rule_files') as mockedCreatingAssignationRulesFiles:
                    mockedCreatingAssignationRulesFiles.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.reload_udev_rules') as mockedReloadingUdevRules:
                        mockedReloadingUdevRules.return_value = True

                        assert self.zwaveNetworkInstaller.assign_fixed_usb_port_names_to_controller("") == False

        #test if method detect error during udev file creation
        with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.get_controller_vendor_id') as mockedgettingVendorId:
            mockedgettingVendorId.return_value = "1"

            with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.get_controller_product_id') as mockedgettingProductId:
                mockedgettingProductId.return_value = "1"

                with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.create_assignation_rule_files') as mockedCreatingAssignationRulesFiles:
                    mockedCreatingAssignationRulesFiles.return_value = False

                    with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.reload_udev_rules') as mockedReloadingUdevRules:
                        mockedReloadingUdevRules.return_value = True

                        assert self.zwaveNetworkInstaller.assign_fixed_usb_port_names_to_controller("") == False

        #test if method detect error during udev rules reloading
        with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.get_controller_vendor_id') as mockedgettingVendorId:
            mockedgettingVendorId.return_value = "1"

            with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.get_controller_product_id') as mockedgettingProductId:
                mockedgettingProductId.return_value = "1"

                with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.create_assignation_rule_files') as mockedCreatingAssignationRulesFiles:
                    mockedCreatingAssignationRulesFiles.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.reload_udev_rules') as mockedReloadingUdevRules:
                        mockedReloadingUdevRules.return_value = False

                        assert self.zwaveNetworkInstaller.assign_fixed_usb_port_names_to_controller("") == False


    def test_setting_home_automation_system_configuration_booleean_control(self):
        """
            1.test if method return an bool 
            2.test if method detect wrong value type
            3.test if method return true if succes
            4.test if method return false if error
            5.test if method read file for collect the data
            6.test if method write in file
        """
        
        #test if method return an bool
        assert isinstance(self.zwaveNetworkInstaller.set_zwave_network_configuration_booleean_control("false"), bool) == True
        
        #test if method detect wrong value type
        assert self.zwaveNetworkInstaller.set_zwave_network_configuration_booleean_control("test") == False

        open_mock = mock_open()
        jsonMock = MagicMock( side_effect = [ { "test": "test" } ] )

        with patch("builtins.open", open_mock, create=False):
            with patch("json.load", jsonMock):
                #test if method return true if succes
                assert self.zwaveNetworkInstaller.set_zwave_network_configuration_booleean_control(True) == True

            #test if method write in file
            open_mock.assert_called_with(self.zWaveNetworkConfigFile, "w")

        #test if method return false if error
        open_mock.side_effect = IOError()
        with patch("builtins.open", open_mock, create=False):
            assert self.zwaveNetworkInstaller.set_zwave_network_configuration_booleean_control(True) == False


    @patch("subprocess.Popen")
    def test_reloading_udev_rules(self, mock_subproc_popen):
        """
            1.test if method return True if succes
            2.test if methode detect error
        """

        #test if method return True if succes
        process_mock = mock.Mock()
        attrs = {"communicate.return_value": (b"output", b"error"),
            "returncode": 0}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock

        assert self.zwaveNetworkInstaller.reload_udev_rules() == True

        #test if methode detect error
        process_mock = mock.Mock()
        attrs = {"communicate.return_value": (b"output", b"error"),
            "returncode": 1}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock

        assert self.zwaveNetworkInstaller.reload_udev_rules() == False