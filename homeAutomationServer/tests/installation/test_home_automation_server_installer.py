#!/usr/bin/python3

import os
import mock
import sys
import json
import subprocess

sys.path.append("..")

from homeAutomationServer.classes.homeAutomationServerInstaller import *
from unittest.mock import patch, mock_open, MagicMock


class TestHomeAutomationServerInstaller:
    """
        class used for test the home automation server installer
        
            Attributes:
                script path (path of the main script (for files manipulation))
				home automation system installer (class contained all function used for home automation system installation)
                home automation system config file path

            tests:
                test_homeAutomationServerConfigured_property
                test_getting_zwave_controller_path
                test_getting_zwave_config_folder_path
                test_downloading_nginx
                test_dowloading_supervisor
                test_creating_home_automation_system_config_file
                test_setting_home_automation_system_configuration_booleean_control
    """

    """constructor"""
    scriptPath = os.path.dirname(os.path.abspath(__file__))
    homeAutomationServerInstaller = HomeAutomationServerInstaller(os.path.dirname(os.path.abspath(__file__)))
    homeAutomationServerConfigFile = os.path.dirname(os.path.abspath(__file__)) + "/configs/homeAutomationServerConfig.json"


    """TESTS"""
    def test_homeAutomationServerConfigured_property(self):
        """
            test if method return true or false
            test if method return false if error
            test if method return good values
        """

        assert isinstance(self.homeAutomationServerInstaller.homeAutomationServerConfigured, bool)

        open_mock = mock_open()
        jsonMock = MagicMock( side_effect = [ { "serverConfigured": True } ] )

        with patch("builtins.open", open_mock, create=False):
            with patch("json.load", jsonMock):
                #test if method return the good values
                assert self.homeAutomationServerInstaller.homeAutomationServerConfigured == True
                jsonMock = MagicMock( side_effect = [ { "serverConfigured": False } ] )
                assert self.homeAutomationServerInstaller.homeAutomationServerConfigured == False

            #test if method return false if error
            open_mock.side_effect = IOError()
            assert self.homeAutomationServerInstaller.homeAutomationServerConfigured == False



    def test_getting_base_supervisor_config(self):
        """
            1.test if method return good data
            2.test if method detect error
        """

        open_mock = mock_open()
        
        #test if method return good data
        with patch('builtins.open', mock_open(read_data='test')):
                assert self.homeAutomationServerInstaller.get_base_supervisor_config(True) == 'test'

        #test if method detect error
        with patch("builtins.open", open_mock, create=False):
            open_mock.side_effect = IOError()
            assert self.homeAutomationServerInstaller.get_base_supervisor_config(True) == False



    @patch("subprocess.Popen")
    def test_dowloading_supervisor(self, mock_subproc_popen):
        """
            1.test if method return an bool 
            2.test if method return true if succes
            3.test if method return false if error
        """

        process_mock = mock.Mock()
        attrs = {"communicate.return_value": (b"output", b"error"),
        "returncode": 0}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock

        #test if method return an bool
        assert isinstance(self.homeAutomationServerInstaller.dowload_supervisor(), bool)

        #test if method return True if succes
        assert self.homeAutomationServerInstaller.dowload_supervisor() == True


        process_mock = mock.Mock()
        attrs = {"communicate.return_value": (b"output", b"error"),
        "returncode": 1}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock

        #test if method return False if error
        assert self.homeAutomationServerInstaller.dowload_supervisor() == False


    def test_creating_home_automation_server_config_file(self):
        """
            1.test if method write in file
                a.test if method used the good file
                b.test if good data was write
            2.test if method return true if succes
            3.test if method return false if error
            4.test if method detect bad parametters
        """

        data = {}

        data["zWaveNetwork"] = "activated"
        data["serverConfigured"] = False

        #test if method write in file
        open_mock = mock_open()
        with patch("builtins.open", open_mock, create=False):
            self.homeAutomationServerInstaller.create_home_automation_server_config_file(data["serverConfigured"], data["zWaveNetwork"])

            #test if method used the good file
            open_mock.assert_called_with(self.homeAutomationServerConfigFile, "w")

            #test if method return true if succes
            assert self.homeAutomationServerInstaller.create_home_automation_server_config_file(data["serverConfigured"], data["zWaveNetwork"]) == True

        #test if method return false if error
        open_mock.side_effect = IOError()
        
        with patch("builtins.open", open_mock, create=False):
            assert self.homeAutomationServerInstaller.create_home_automation_server_config_file(data["serverConfigured"], data["zWaveNetwork"]) == False

        #test if method detect bad parametters
        open_mock = mock_open()
        with patch("builtins.open", open_mock, create=False):
            assert self.homeAutomationServerInstaller.create_home_automation_server_config_file("False", data["zWaveNetwork"]) == False
            assert self.homeAutomationServerInstaller.create_home_automation_server_config_file(data["serverConfigured"], False) == False


    def test_creating_automation_server_supervisor_config_file(self):
        """
            1.test if method return true if succes
            2.test if method detect copy error
            3.test if method detect error during setting supervisor config file
            4.test if method detect error durring moving supervisor config file
            5.test if method detect file inexistance
        """

        #test if method return true if succes
        with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.copy_config_file') as mockedCopiedFile:
            mockedCopiedFile.return_value = True

            with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.set_supervisor_config_file') as mockedSettingSupervisorConfigFile:
                mockedSettingSupervisorConfigFile.return_value = True

                with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.move_config_file') as mockedMovingConfigFile:
                    mockedMovingConfigFile.return_value = True

                    with mock.patch('os.path.exists') as mockedFileExist:
                        mockedFileExist.return_value = True

                        assert self.homeAutomationServerInstaller.create_automation_server_supervisor_config_file() == True

        #test if method detect copy error
        with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.copy_config_file') as mockedCopiedFile:
            mockedCopiedFile.return_value = False

            with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.set_supervisor_config_file') as mockedSettingSupervisorConfigFile:
                mockedSettingSupervisorConfigFile.return_value = True

                with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.move_config_file') as mockedMovingConfigFile:
                    mockedMovingConfigFile.return_value = True

                    with mock.patch('os.path.exists') as mockedFileExist:
                        mockedFileExist.return_value = False

                        assert self.homeAutomationServerInstaller.create_automation_server_supervisor_config_file() == False

        #test if method detect error during setting supervisor config file
        with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.copy_config_file') as mockedCopiedFile:
            mockedCopiedFile.return_value = True

            with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.set_supervisor_config_file') as mockedSettingSupervisorConfigFile:
                mockedSettingSupervisorConfigFile.return_value = False

                with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.move_config_file') as mockedMovingConfigFile:
                    mockedMovingConfigFile.return_value = True

                    with mock.patch('os.path.exists') as mockedFileExist:
                        mockedFileExist.return_value = False

                        assert self.homeAutomationServerInstaller.create_automation_server_supervisor_config_file() == False

        #test if method detect error durring moving supervisor config file
        with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.copy_config_file') as mockedCopiedFile:
            mockedCopiedFile.return_value = True

            with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.set_supervisor_config_file') as mockedSettingSupervisorConfigFile:
                mockedSettingSupervisorConfigFile.return_value = True

                with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.move_config_file') as mockedMovingConfigFile:
                    mockedMovingConfigFile.return_value = False

                    with mock.patch('os.path.exists') as mockedFileExist:
                        mockedFileExist.return_value = False

                        assert self.homeAutomationServerInstaller.create_automation_server_supervisor_config_file() == False

        #test if method detect file inexistance
        with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.copy_config_file') as mockedCopiedFile:
            mockedCopiedFile.return_value = True

            with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.set_supervisor_config_file') as mockedSettingSupervisorConfigFile:
                mockedSettingSupervisorConfigFile.return_value = True

                with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.move_config_file') as mockedMovingConfigFile:
                    mockedMovingConfigFile.return_value = True

                    with mock.patch('os.path.exists') as mockedFileExist:
                        mockedFileExist.return_value = False

                        assert self.homeAutomationServerInstaller.create_automation_server_supervisor_config_file() == False


    @patch("subprocess.Popen")
    def test_copying_config_file(self, mock_subproc_popen):
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

            assert self.homeAutomationServerInstaller.copy_config_file("test", "newTest") == True

        #test if method detect file inexistance
        with patch("builtins.open", open_mock, create=False):
            open_mock.side_effect = IOError()
            
            assert self.homeAutomationServerInstaller.copy_config_file("test", "newTest") == False

        #check if method detect error durring subprocces call
        with patch("builtins.open", open_mock, create=False):

            process_mock = mock.Mock()
            attrs = {"communicate.return_value": (b"output", b"error"),
            "returncode": 1}
            process_mock.configure_mock(**attrs)
            mock_subproc_popen.return_value = process_mock

            assert self.homeAutomationServerInstaller.copy_config_file("test", "newTest") == False


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

            assert self.homeAutomationServerInstaller.move_config_file("test", "newTest") == True

        #test if method detect file inexistance
        with patch("builtins.open", open_mock, create=False):
            open_mock.side_effect = IOError()
            
            assert self.homeAutomationServerInstaller.move_config_file("test", "newTest") == False

        #check if method detect error durring subprocces call
        with patch("builtins.open", open_mock, create=False):

            process_mock = mock.Mock()
            attrs = {"communicate.return_value": (b"output", b"error"),
            "returncode": 1}
            process_mock.configure_mock(**attrs)
            mock_subproc_popen.return_value = process_mock

            assert self.homeAutomationServerInstaller.move_config_file("test", "newTest") == False



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
        assert isinstance(self.homeAutomationServerInstaller.set_home_automation_server_configuration_booleean_control("false"), bool) == True
        
        #test if method detect wrong value type
        assert self.homeAutomationServerInstaller.set_home_automation_server_configuration_booleean_control("test") == False

        open_mock = mock_open()
        jsonMock = MagicMock( side_effect = [ { "test": "test" } ] )

        with patch("builtins.open", open_mock, create=False):
            with patch("json.load", jsonMock):
                #test if method return true if succes
                assert self.homeAutomationServerInstaller.set_home_automation_server_configuration_booleean_control(True) == True

            #test if method write in file
            open_mock.assert_called_with(self.homeAutomationServerConfigFile, "w")

        #test if method return false if error
        open_mock.side_effect = IOError()
        with patch("builtins.open", open_mock, create=False):
            assert self.homeAutomationServerInstaller.set_home_automation_server_configuration_booleean_control(True) == False


    def test_setting_supervisor_config_file(self):
        """
            1.test if method return true if succes
            2.test if method detect error during getting base supervisor config file
            3.test if method detect error during writing config
        """

        open_mock = mock_open()
        
        #test if method return true if succes
        with patch("builtins.open", open_mock, create=False):
            with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.get_base_supervisor_config') as mockedgettingBaseSupervisorConfig:
                mockedgettingBaseSupervisorConfig.return_value = ""

                assert self.homeAutomationServerInstaller.set_supervisor_config_file("") == True
        
        #test if method detect error during getting base supervisor config file
        with patch("builtins.open", open_mock, create=False):
            with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.get_base_supervisor_config') as mockedgettingBaseSupervisorConfig:
                mockedgettingBaseSupervisorConfig.return_value = False

                assert self.homeAutomationServerInstaller.set_supervisor_config_file("") == False

        #test if method detect error during writing config
        with patch("builtins.open", open_mock, create=False):
            with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.get_base_supervisor_config') as mockedgettingBaseSupervisorConfig:
                mockedgettingBaseSupervisorConfig.return_value = ""
                open_mock.side_effect = IOError()
                
                assert self.homeAutomationServerInstaller.set_supervisor_config_file("") == False


    def test_setting_zWaveNetwork_activity_state(self):
        """
            1.test if method return an bool 
            2.test if method detect wrong value type
            3.test if method return true if succes
            4.test if method return false if error
            5.test if method read file for collect the data
            6.test if method write in file
        """
        
        #test if method return an bool
        assert isinstance(self.homeAutomationServerInstaller.set_zWaveNetwork_activity_state("activated"), bool) == True
        
        open_mock = mock_open()
        jsonMock = MagicMock( side_effect = [ { "test": "test" } ] )

        with patch("builtins.open", open_mock, create=False):
            with patch("json.load", jsonMock):
                #test if method return true if succes
                assert self.homeAutomationServerInstaller.set_zWaveNetwork_activity_state("activated") == True

                #test if method write in file
                open_mock.assert_called_with(self.homeAutomationServerConfigFile, "w")

                #test if method detect wrong value type
                assert self.homeAutomationServerInstaller.set_zWaveNetwork_activity_state("False") == False


        #test if method return false if error
        open_mock.side_effect = IOError()
        with patch("builtins.open", open_mock, create=False):
            assert self.homeAutomationServerInstaller.set_zWaveNetwork_activity_state("activated") == False



    def test_installing_zwaveNetwork(self):
        """
            1.test if method succes
            2.test if method return good type of data
            3.test if method detect error durring installation
        """
        
        """
            with mock.patch('homeAutomationServer.homeAutomationNetworks.zWaveNetwork.install.install') as mockedZwaveNetworkInstallation:
                mockedZwaveNetworkInstallation.return_value = True

                #test if method succes
                assert self.homeAutomationServerInstaller.install_zwaveNetwork() == True

                #test if method return good type of data
                assert isinstance(self.homeAutomationServerInstaller.install_zwaveNetwork(), bool) == True


            with mock.patch('homeAutomationServer.homeAutomationNetworks.zWaveNetwork.install.install') as mockedZwaveNetworkInstallation:
                mockedZwaveNetworkInstallation.return_value = False

                #test if method detect error durring installation
                assert self.homeAutomationServerInstaller.install_zwaveNetwork() == False
        """

        pass