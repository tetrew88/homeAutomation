import sys
import mock

sys.path.append("..")

from unittest.mock import patch, mock_open, MagicMock

from zWaveNetwork.install import *

def test_zwave_network_installation():
    """
        1.test if method return true if succes
        2.test if method return false if error 
        4.test if method detect error durring getting zwave controller path
        5.test if method detect error durring getting zwave config path
        6.test if method detect error during attributing fix usb name ton controller
        7.test if method detect error durring creation home automation server config file
        9.test if method detect error in setting home automation server booleean control
    """


    #test if method return true if succes
    with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.get_zwave_controller_path') as mockedGettingZwaveControllerPath:
        mockedGettingZwaveControllerPath.return_value = ""

        with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.get_zwave_config_folder_path') as mockedGettingZwaveConfigFolder:
            mockedGettingZwaveConfigFolder.return_value = ""

            with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.assign_fixed_usb_port_names_to_controller') as mockedAssignationFixUsbNameToController:
                mockedAssignationFixUsbNameToController.return_value = True

                with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.create_zwave_network_config_file') as mockedCreatingZWaveConfigFile:
                    mockedCreatingZWaveConfigFile.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.set_zwave_network_configuration_booleean_control') as mockedSettingHomeAutomationServerBooleeanControl:
                            mockedSettingHomeAutomationServerBooleeanControl.return_value = True

                            assert install() == True

    #test if method detect error
    with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.get_zwave_controller_path') as mockedGettingZwaveControllerPath:
        mockedGettingZwaveControllerPath.return_value = False

        with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.get_zwave_config_folder_path') as mockedGettingZwaveConfigFolder:
            mockedGettingZwaveConfigFolder.return_value = False

            with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.assign_fixed_usb_port_names_to_controller') as mockedAssignationFixUsbNameToController:
                mockedAssignationFixUsbNameToController.return_value = False

                with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.create_zwave_network_config_file') as mockedCreatingZWaveConfigFile:
                    mockedCreatingZWaveConfigFile.return_value = False

                    with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.set_zwave_network_configuration_booleean_control') as mockedSettingHomeAutomationServerBooleeanControl:
                        mockedSettingHomeAutomationServerBooleeanControl.return_value = False

                        assert install() == False


    #test if method detect error durring getting zwave controller path
    with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.get_zwave_controller_path') as mockedGettingZwaveControllerPath:
        mockedGettingZwaveControllerPath.return_value = False

        with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.get_zwave_config_folder_path') as mockedGettingZwaveConfigFolder:
            mockedGettingZwaveConfigFolder.return_value = ""

            with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.assign_fixed_usb_port_names_to_controller') as mockedAssignationFixUsbNameToController:
                mockedAssignationFixUsbNameToController.return_value = True

                with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.create_zwave_network_config_file') as mockedCreatingZWaveConfigFile:
                    mockedCreatingZWaveConfigFile.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.set_zwave_network_configuration_booleean_control') as mockedSettingHomeAutomationServerBooleeanControl:
                        mockedSettingHomeAutomationServerBooleeanControl.return_value = True

                        assert install() == False

    #test if method detect error durring getting zwave config path
    with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.get_zwave_controller_path') as mockedGettingZwaveControllerPath:
        mockedGettingZwaveControllerPath.return_value = ""

        with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.get_zwave_config_folder_path') as mockedGettingZwaveConfigFolder:
            mockedGettingZwaveConfigFolder.return_value = False

            with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.assign_fixed_usb_port_names_to_controller') as mockedAssignationFixUsbNameToController:
                mockedAssignationFixUsbNameToController.return_value = True

                with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.create_zwave_network_config_file') as mockedCreatingZWaveConfigFile:
                    mockedCreatingZWaveConfigFile.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.set_zwave_network_configuration_booleean_control') as mockedSettingHomeAutomationServerBooleeanControl:
                        mockedSettingHomeAutomationServerBooleeanControl.return_value = True

                        assert install() == False

    #test if method detect error during attributing fix usb name ton controller
    with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.get_zwave_controller_path') as mockedGettingZwaveControllerPath:
        mockedGettingZwaveControllerPath.return_value = ""

        with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.get_zwave_config_folder_path') as mockedGettingZwaveConfigFolder:
            mockedGettingZwaveConfigFolder.return_value = ""

            with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.assign_fixed_usb_port_names_to_controller') as mockedAssignationFixUsbNameToController:
                mockedAssignationFixUsbNameToController.return_value = False

                with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.create_zwave_network_config_file') as mockedCreatingZWaveConfigFile:
                    mockedCreatingZWaveConfigFile.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.set_zwave_network_configuration_booleean_control') as mockedSettingHomeAutomationServerBooleeanControl:
                        mockedSettingHomeAutomationServerBooleeanControl.return_value = True

                        assert install() == False

    #test if method detect error durring creation home automation server config file
    with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.get_zwave_controller_path') as mockedGettingZwaveControllerPath:
        mockedGettingZwaveControllerPath.return_value = ""

        with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.get_zwave_config_folder_path') as mockedGettingZwaveConfigFolder:
            mockedGettingZwaveConfigFolder.return_value = ""

            with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.assign_fixed_usb_port_names_to_controller') as mockedAssignationFixUsbNameToController:
                mockedAssignationFixUsbNameToController.return_value = True

                with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.create_zwave_network_config_file') as mockedCreatingZWaveConfigFile:
                    mockedCreatingZWaveConfigFile.return_value = False

                    with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.set_zwave_network_configuration_booleean_control') as mockedSettingHomeAutomationServerBooleeanControl:
                        mockedSettingHomeAutomationServerBooleeanControl.return_value = True

                        assert install() == False

    #test if method detect error in setting home automation server booleean control
    with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.get_zwave_controller_path') as mockedGettingZwaveControllerPath:
        mockedGettingZwaveControllerPath.return_value = ""

        with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.get_zwave_config_folder_path') as mockedGettingZwaveConfigFolder:
            mockedGettingZwaveConfigFolder.return_value = ""

            with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.assign_fixed_usb_port_names_to_controller') as mockedAssignationFixUsbNameToController:
                mockedAssignationFixUsbNameToController.return_value = True

                with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.create_zwave_network_config_file') as mockedCreatingZWaveConfigFile:
                    mockedCreatingZWaveConfigFile.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetworkInstaller.ZWaveNetworkInstaller.set_zwave_network_configuration_booleean_control') as mockedSettingHomeAutomationServerBooleeanControl:
                            mockedSettingHomeAutomationServerBooleeanControl.return_value = False

                            assert install() == False