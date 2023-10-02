import sys
import mock

sys.path.append("..")

from unittest.mock import patch, mock_open, MagicMock

from homeAutomationServer.install import *

def test_home_automation_server_installation():
    """
        1.test if method return true if succes
        2.test if method return false if error 
        3.test if method detect error during supervisor installation 
        4.test if method detect error durring installing zwave network
        5.test if method detect error durring creation home automation server config file
        6.test if method detect error durring creation home automation server supervisor config file
        7.test if method detect error in setting home automation server booleean control
        8.test if method detect error durring setting zwave network activity state
    """


    #test if method return true if succes
    with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.dowload_supervisor') as mockedSupervisorDownload:
        mockedSupervisorDownload.return_value = True

        with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.install_zwaveNetwork') as mockedZwaveNetworkInstallation:
            mockedZwaveNetworkInstallation.return_value = True

            with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.create_home_automation_server_config_file') as mockedCreatingHomeAutomationServerConfigFile:
                        mockedCreatingHomeAutomationServerConfigFile.return_value = True

                        with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.create_automation_server_supervisor_config_file') as mockedCreatingHomeAutomationServerSupervisorConfigFile:
                            mockedCreatingHomeAutomationServerSupervisorConfigFile.return_value = True

                            with mock.patch('builtins.input', return_value="o"):
                                with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.set_home_automation_server_configuration_booleean_control') as mockedSettingHomeAutomationServerBooleeanControl:
                                    mockedSettingHomeAutomationServerBooleeanControl.return_value = True

                                    with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.set_zWaveNetwork_activity_state') as mockedSettingZwaveNetworkActivityState:
                                        mockedSettingZwaveNetworkActivityState.return_value = True

                                        assert install() == True

    #test if method detect error
    with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.dowload_supervisor') as mockedSupervisorDownload:
        mockedSupervisorDownload.return_value = False

        with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.install_zwaveNetwork') as mockedZwaveNetworkInstallation:
            mockedZwaveNetworkInstallation.return_value = False

            with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.create_home_automation_server_config_file') as mockedCreatingHomeAutomationServerConfigFile:
                        mockedCreatingHomeAutomationServerConfigFile.return_value = False

                        with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.create_automation_server_supervisor_config_file') as mockedCreatingHomeAutomationServerSupervisorConfigFile:
                            mockedCreatingHomeAutomationServerSupervisorConfigFile.return_value = False

                            with mock.patch('builtins.input', return_value="o"):
                                with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.set_home_automation_server_configuration_booleean_control') as mockedSettingHomeAutomationServerBooleeanControl:
                                    mockedSettingHomeAutomationServerBooleeanControl.return_value = False

                                    with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.set_zWaveNetwork_activity_state') as mockedSettingZwaveNetworkActivityState:
                                        mockedSettingZwaveNetworkActivityState.return_value = False

                                        assert install() == False

    #test if method detect error during supervisor installation
    with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.dowload_supervisor') as mockedSupervisorDownload:
        mockedSupervisorDownload.return_value = False

        with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.install_zwaveNetwork') as mockedZwaveNetworkInstallation:
            mockedZwaveNetworkInstallation.return_value = True

            with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.create_home_automation_server_config_file') as mockedCreatingHomeAutomationServerConfigFile:
                        mockedCreatingHomeAutomationServerConfigFile.return_value = True

                        with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.create_automation_server_supervisor_config_file') as mockedCreatingHomeAutomationServerSupervisorConfigFile:
                            mockedCreatingHomeAutomationServerSupervisorConfigFile.return_value = True

                            with mock.patch('builtins.input', return_value="o"):
                                with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.set_home_automation_server_configuration_booleean_control') as mockedSettingHomeAutomationServerBooleeanControl:
                                    mockedSettingHomeAutomationServerBooleeanControl.return_value = True

                                    with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.set_zWaveNetwork_activity_state') as mockedSettingZwaveNetworkActivityState:
                                        mockedSettingZwaveNetworkActivityState.return_value = True

                                        assert install() == False

    #test if method detect error durring installing zwave network
    with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.dowload_supervisor') as mockedSupervisorDownload:
        mockedSupervisorDownload.return_value = True

        with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.install_zwaveNetwork') as mockedZwaveNetworkInstallation:
            mockedZwaveNetworkInstallation.return_value = False

            with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.create_home_automation_server_config_file') as mockedCreatingHomeAutomationServerConfigFile:
                        mockedCreatingHomeAutomationServerConfigFile.return_value = True

                        with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.create_automation_server_supervisor_config_file') as mockedCreatingHomeAutomationServerSupervisorConfigFile:
                            mockedCreatingHomeAutomationServerSupervisorConfigFile.return_value = True

                            with mock.patch('builtins.input', return_value="o"):
                                with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.set_home_automation_server_configuration_booleean_control') as mockedSettingHomeAutomationServerBooleeanControl:
                                    mockedSettingHomeAutomationServerBooleeanControl.return_value = True

                                    with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.set_zWaveNetwork_activity_state') as mockedSettingZwaveNetworkActivityState:
                                        mockedSettingZwaveNetworkActivityState.return_value = True

                                        assert install() == False

    #test if method detect error durring creation home automation server config file
    with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.dowload_supervisor') as mockedSupervisorDownload:
        mockedSupervisorDownload.return_value = True

        with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.install_zwaveNetwork') as mockedZwaveNetworkInstallation:
            mockedZwaveNetworkInstallation.return_value = True

            with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.create_home_automation_server_config_file') as mockedCreatingHomeAutomationServerConfigFile:
                        mockedCreatingHomeAutomationServerConfigFile.return_value = False

                        with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.create_automation_server_supervisor_config_file') as mockedCreatingHomeAutomationServerSupervisorConfigFile:
                            mockedCreatingHomeAutomationServerSupervisorConfigFile.return_value = True

                            with mock.patch('builtins.input', return_value="o"):
                                with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.set_home_automation_server_configuration_booleean_control') as mockedSettingHomeAutomationServerBooleeanControl:
                                    mockedSettingHomeAutomationServerBooleeanControl.return_value = True

                                    with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.set_zWaveNetwork_activity_state') as mockedSettingZwaveNetworkActivityState:
                                        mockedSettingZwaveNetworkActivityState.return_value = True

                                        assert install() == False

    #test if method detect error durring creation home automation server supervisor config file
    with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.dowload_supervisor') as mockedSupervisorDownload:
        mockedSupervisorDownload.return_value = True

        with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.install_zwaveNetwork') as mockedZwaveNetworkInstallation:
            mockedZwaveNetworkInstallation.return_value = True

            with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.create_home_automation_server_config_file') as mockedCreatingHomeAutomationServerConfigFile:
                        mockedCreatingHomeAutomationServerConfigFile.return_value = True

                        with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.create_automation_server_supervisor_config_file') as mockedCreatingHomeAutomationServerSupervisorConfigFile:
                            mockedCreatingHomeAutomationServerSupervisorConfigFile.return_value = False

                            with mock.patch('builtins.input', return_value="o"):
                                with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.set_home_automation_server_configuration_booleean_control') as mockedSettingHomeAutomationServerBooleeanControl:
                                    mockedSettingHomeAutomationServerBooleeanControl.return_value = True

                                    with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.set_zWaveNetwork_activity_state') as mockedSettingZwaveNetworkActivityState:
                                        mockedSettingZwaveNetworkActivityState.return_value = True

                                        assert install() == False

    #test if method detect error in setting home automation server booleean control
    with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.dowload_supervisor') as mockedSupervisorDownload:
        mockedSupervisorDownload.return_value = True

        with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.install_zwaveNetwork') as mockedZwaveNetworkInstallation:
            mockedZwaveNetworkInstallation.return_value = True

            with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.create_home_automation_server_config_file') as mockedCreatingHomeAutomationServerConfigFile:
                        mockedCreatingHomeAutomationServerConfigFile.return_value = True

                        with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.create_automation_server_supervisor_config_file') as mockedCreatingHomeAutomationServerSupervisorConfigFile:
                            mockedCreatingHomeAutomationServerSupervisorConfigFile.return_value = True

                            with mock.patch('builtins.input', return_value="o"):
                                with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.set_home_automation_server_configuration_booleean_control') as mockedSettingHomeAutomationServerBooleeanControl:
                                    mockedSettingHomeAutomationServerBooleeanControl.return_value = False

                                    with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.set_zWaveNetwork_activity_state') as mockedSettingZwaveNetworkActivityState:
                                        mockedSettingZwaveNetworkActivityState.return_value = True

                                        assert install() == False

    #test if method detect error durring setting zwave network activity state
    with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.dowload_supervisor') as mockedSupervisorDownload:
        mockedSupervisorDownload.return_value = True

        with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.install_zwaveNetwork') as mockedZwaveNetworkInstallation:
            mockedZwaveNetworkInstallation.return_value = True

            with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.create_home_automation_server_config_file') as mockedCreatingHomeAutomationServerConfigFile:
                        mockedCreatingHomeAutomationServerConfigFile.return_value = True

                        with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.create_automation_server_supervisor_config_file') as mockedCreatingHomeAutomationServerSupervisorConfigFile:
                            mockedCreatingHomeAutomationServerSupervisorConfigFile.return_value = True

                            with mock.patch('builtins.input', return_value="o"):
                                with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.set_home_automation_server_configuration_booleean_control') as mockedSettingHomeAutomationServerBooleeanControl:
                                    mockedSettingHomeAutomationServerBooleeanControl.return_value = True

                                    with mock.patch('homeAutomationServer.classes.homeAutomationServerInstaller.HomeAutomationServerInstaller.set_zWaveNetwork_activity_state') as mockedSettingZwaveNetworkActivityState:
                                        mockedSettingZwaveNetworkActivityState.return_value = False

                                        assert install() == False