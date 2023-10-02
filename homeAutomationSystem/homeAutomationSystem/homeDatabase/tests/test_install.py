import sys
import mock

sys.path.append("..")

from unittest.mock import patch, mock_open, MagicMock

from homeDatabase.install import *

def test_database_installation():
        """
            1.test if method return true if succes
            2.test if method return false if error
            3.test if method detect error during database dowloading
			4.test if method detect error when getting user information and databasename
			5.test if method detect creation config file error
			6.test if method detect error during database creation
			7.test if method detect error during database table creation
		    8.test if method detect error during user creation
			9.test if method detect error during the attribution of the privilege
			10.test if method detect error during setting database booleean    
        """

        #test if method return true if succes
        with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.download_database_system') as mockedDatabaseDownload:
            mockedDatabaseDownload.return_value = True

            with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.get_system_username') as mockedGettingUsername:
                mockedGettingUsername.return_value = "homeAutomationSystem"

                with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.get_system_user_password') as mockedGettingPassword:
                    mockedGettingPassword.return_value = "password"

                    with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.get_database_name') as mockedGettingDatabaseName:
                        mockedGettingDatabaseName.return_value = "Home"

                        with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.create_database_config_file') as mockedCreatingDatabaseConfigFile:
                            mockedCreatingDatabaseConfigFile.return_value = True

                            with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.create_database') as mockedCreatingDatabase:
                                mockedCreatingDatabase.return_value = True

                                with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.create_database_table') as mockedCreatingDatabaseTable:
                                    mockedCreatingDatabaseTable.return_value = True

                                    with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.create_database_system_user') as mockedCreatingDatabaseUser:
                                        mockedCreatingDatabaseUser.return_value = True

                                        with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.attribute_user_system_privilege') as mockedAttributingPrivilege:
                                            mockedAttributingPrivilege.return_value = True

                                            with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.set_database_configuration_booleean_control') as mockedSettingDatabaseConfigurationBooleean:
                                                mockedSettingDatabaseConfigurationBooleean.return_value = True

                                                assert install() == True
            
        #test if method return false if error
        with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.download_database_system') as mockedDatabaseDownload:
            mockedDatabaseDownload.return_value = False

            with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.get_system_username') as mockedGettingUsername:
                mockedGettingUsername.return_value = "homeAutomationSystem"

                with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.get_system_user_password') as mockedGettingPassword:
                    mockedGettingPassword.return_value = "password"

                    with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.get_database_name') as mockedGettingDatabaseName:
                        mockedGettingDatabaseName.return_value = "Home"

                        with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.create_database_config_file') as mockedCreatingDatabaseConfigFile:
                            mockedCreatingDatabaseConfigFile.return_value = True

                            with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.create_database') as mockedCreatingDatabase:
                                mockedCreatingDatabase.return_value = True

                                with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.create_database_table') as mockedCreatingDatabaseTable:
                                    mockedCreatingDatabaseTable.return_value = True

                                    with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.create_database_system_user') as mockedCreatingDatabaseUser:
                                        mockedCreatingDatabaseUser.return_value = True

                                        with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.attribute_user_system_privilege') as mockedAttributingPrivilege:
                                            mockedAttributingPrivilege.return_value = True

                                            with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.set_database_configuration_booleean_control') as mockedSettingDatabaseConfigurationBooleean:
                                                mockedSettingDatabaseConfigurationBooleean.return_value = True

                                                assert install() == False
            
        #test if method detect error during database dowloading
        with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.download_database_system') as mockedDatabaseDownload:
            mockedDatabaseDownload.return_value = False

            with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.get_system_username') as mockedGettingUsername:
                mockedGettingUsername.return_value = "homeAutomationSystem"

                with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.get_system_user_password') as mockedGettingPassword:
                    mockedGettingPassword.return_value = "password"

                    with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.get_database_name') as mockedGettingDatabaseName:
                        mockedGettingDatabaseName.return_value = "Home"

                        with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.create_database_config_file') as mockedCreatingDatabaseConfigFile:
                            mockedCreatingDatabaseConfigFile.return_value = True

                            with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.create_database') as mockedCreatingDatabase:
                                mockedCreatingDatabase.return_value = True

                                with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.create_database_table') as mockedCreatingDatabaseTable:
                                    mockedCreatingDatabaseTable.return_value = True

                                    with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.create_database_system_user') as mockedCreatingDatabaseUser:
                                        mockedCreatingDatabaseUser.return_value = True

                                        with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.attribute_user_system_privilege') as mockedAttributingPrivilege:
                                            mockedAttributingPrivilege.return_value = True

                                            with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.set_database_configuration_booleean_control') as mockedSettingDatabaseConfigurationBooleean:
                                                mockedSettingDatabaseConfigurationBooleean.return_value = True

                                                assert install() == False

        #test if method detect error when getting user information and databasename
        with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.download_database_system') as mockedDatabaseDownload:
            mockedDatabaseDownload.return_value = True

            with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.get_system_username') as mockedGettingUsername:
                mockedGettingUsername.return_value = False

                with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.get_system_user_password') as mockedGettingPassword:
                    mockedGettingPassword.return_value = False

                    with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.get_database_name') as mockedGettingDatabaseName:
                        mockedGettingDatabaseName.return_value = False

                        with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.create_database_config_file') as mockedCreatingDatabaseConfigFile:
                            mockedCreatingDatabaseConfigFile.return_value = True

                            with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.create_database') as mockedCreatingDatabase:
                                mockedCreatingDatabase.return_value = True

                                with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.create_database_table') as mockedCreatingDatabaseTable:
                                    mockedCreatingDatabaseTable.return_value = True

                                    with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.create_database_system_user') as mockedCreatingDatabaseUser:
                                        mockedCreatingDatabaseUser.return_value = True

                                        with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.attribute_user_system_privilege') as mockedAttributingPrivilege:
                                            mockedAttributingPrivilege.return_value = True

                                            with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.set_database_configuration_booleean_control') as mockedSettingDatabaseConfigurationBooleean:
                                                mockedSettingDatabaseConfigurationBooleean.return_value = True

                                                assert install() == False

        #test if method detect creation config file error
        with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.download_database_system') as mockedDatabaseDownload:
            mockedDatabaseDownload.return_value = True

            with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.get_system_username') as mockedGettingUsername:
                mockedGettingUsername.return_value = "systemDomotique"

                with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.get_system_user_password') as mockedGettingPassword:
                    mockedGettingPassword.return_value = "password"

                    with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.get_database_name') as mockedGettingDatabaseName:
                        mockedGettingDatabaseName.return_value = "Home"

                        with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.create_database_config_file') as mockedCreatingDatabaseConfigFile:
                            mockedCreatingDatabaseConfigFile.return_value = False

                            with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.create_database') as mockedCreatingDatabase:
                                mockedCreatingDatabase.return_value = True

                                with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.create_database_table') as mockedCreatingDatabaseTable:
                                    mockedCreatingDatabaseTable.return_value = True

                                    with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.create_database_system_user') as mockedCreatingDatabaseUser:
                                        mockedCreatingDatabaseUser.return_value = True

                                        with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.attribute_user_system_privilege') as mockedAttributingPrivilege:
                                            mockedAttributingPrivilege.return_value = True

                                            with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.set_database_configuration_booleean_control') as mockedSettingDatabaseConfigurationBooleean:
                                                mockedSettingDatabaseConfigurationBooleean.return_value = True

                                                assert install() == False

        #test if method detect error during database creation
        with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.download_database_system') as mockedDatabaseDownload:
            mockedDatabaseDownload.return_value = True

            with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.get_system_username') as mockedGettingUsername:
                mockedGettingUsername.return_value = "systemDomotique"

                with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.get_system_user_password') as mockedGettingPassword:
                    mockedGettingPassword.return_value = "password"

                    with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.get_database_name') as mockedGettingDatabaseName:
                        mockedGettingDatabaseName.return_value = "Home"

                        with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.create_database_config_file') as mockedCreatingDatabaseConfigFile:
                            mockedCreatingDatabaseConfigFile.return_value = True

                            with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.create_database') as mockedCreatingDatabase:
                                mockedCreatingDatabase.return_value = False

                                with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.create_database_table') as mockedCreatingDatabaseTable:
                                    mockedCreatingDatabaseTable.return_value = True

                                    with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.create_database_system_user') as mockedCreatingDatabaseUser:
                                        mockedCreatingDatabaseUser.return_value = True

                                        with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.attribute_user_system_privilege') as mockedAttributingPrivilege:
                                            mockedAttributingPrivilege.return_value = True

                                            with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.set_database_configuration_booleean_control') as mockedSettingDatabaseConfigurationBooleean:
                                                mockedSettingDatabaseConfigurationBooleean.return_value = True

                                                assert install() == False

        #test if method detect error during database table creation
        with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.download_database_system') as mockedDatabaseDownload:
            mockedDatabaseDownload.return_value = True

            with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.get_system_username') as mockedGettingUsername:
                mockedGettingUsername.return_value = "systemDomotique"

                with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.get_system_user_password') as mockedGettingPassword:
                    mockedGettingPassword.return_value = "password"

                    with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.get_database_name') as mockedGettingDatabaseName:
                        mockedGettingDatabaseName.return_value = "Home"

                        with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.create_database_config_file') as mockedCreatingDatabaseConfigFile:
                            mockedCreatingDatabaseConfigFile.return_value = True

                            with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.create_database') as mockedCreatingDatabase:
                                mockedCreatingDatabase.return_value = True

                                with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.create_database_table') as mockedCreatingDatabaseTable:
                                    mockedCreatingDatabaseTable.return_value = False

                                    with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.create_database_system_user') as mockedCreatingDatabaseUser:
                                        mockedCreatingDatabaseUser.return_value = True

                                        with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.attribute_user_system_privilege') as mockedAttributingPrivilege:
                                            mockedAttributingPrivilege.return_value = True

                                            with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.set_database_configuration_booleean_control') as mockedSettingDatabaseConfigurationBooleean:
                                                mockedSettingDatabaseConfigurationBooleean.return_value = True

                                                assert install() == False

        #test if method detect error during user creation
        with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.download_database_system') as mockedDatabaseDownload:
            mockedDatabaseDownload.return_value = True

            with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.get_system_username') as mockedGettingUsername:
                mockedGettingUsername.return_value = "systemDomotique"

                with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.get_system_user_password') as mockedGettingPassword:
                    mockedGettingPassword.return_value = "password"

                    with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.get_database_name') as mockedGettingDatabaseName:
                        mockedGettingDatabaseName.return_value = "Home"

                        with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.create_database_config_file') as mockedCreatingDatabaseConfigFile:
                            mockedCreatingDatabaseConfigFile.return_value = True

                            with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.create_database') as mockedCreatingDatabase:
                                mockedCreatingDatabase.return_value = True

                                with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.create_database_table') as mockedCreatingDatabaseTable:
                                    mockedCreatingDatabaseTable.return_value = True

                                    with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.create_database_system_user') as mockedCreatingDatabaseUser:
                                        mockedCreatingDatabaseUser.return_value = False

                                        with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.attribute_user_system_privilege') as mockedAttributingPrivilege:
                                            mockedAttributingPrivilege.return_value = True

                                            with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.set_database_configuration_booleean_control') as mockedSettingDatabaseConfigurationBooleean:
                                                mockedSettingDatabaseConfigurationBooleean.return_value = True

                                                assert install() == False

        #test if method detect error during the attribution of the privilege
        with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.download_database_system') as mockedDatabaseDownload:
            mockedDatabaseDownload.return_value = True

            with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.get_system_username') as mockedGettingUsername:
                mockedGettingUsername.return_value = "systemDomotique"

                with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.get_system_user_password') as mockedGettingPassword:
                    mockedGettingPassword.return_value = "password"

                    with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.get_database_name') as mockedGettingDatabaseName:
                        mockedGettingDatabaseName.return_value = "Home"

                        with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.create_database_config_file') as mockedCreatingDatabaseConfigFile:
                            mockedCreatingDatabaseConfigFile.return_value = True

                            with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.create_database') as mockedCreatingDatabase:
                                mockedCreatingDatabase.return_value = True

                                with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.create_database_table') as mockedCreatingDatabaseTable:
                                    mockedCreatingDatabaseTable.return_value = True

                                    with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.create_database_system_user') as mockedCreatingDatabaseUser:
                                        mockedCreatingDatabaseUser.return_value = True

                                        with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.attribute_user_system_privilege') as mockedAttributingPrivilege:
                                            mockedAttributingPrivilege.return_value = False

                                            with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.set_database_configuration_booleean_control') as mockedSettingDatabaseConfigurationBooleean:
                                                mockedSettingDatabaseConfigurationBooleean.return_value = True

                                                assert install() == False

        #test if method detect error during setting database booleean  
        with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.download_database_system') as mockedDatabaseDownload:
            mockedDatabaseDownload.return_value = True

            with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.get_system_username') as mockedGettingUsername:
                mockedGettingUsername.return_value = "systemDomotique"

                with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.get_system_user_password') as mockedGettingPassword:
                    mockedGettingPassword.return_value = "password"

                    with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.get_database_name') as mockedGettingDatabaseName:
                        mockedGettingDatabaseName.return_value = "Home"

                        with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.create_database_config_file') as mockedCreatingDatabaseConfigFile:
                            mockedCreatingDatabaseConfigFile.return_value = True

                            with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.create_database') as mockedCreatingDatabase:
                                mockedCreatingDatabase.return_value = True

                                with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.create_database_table') as mockedCreatingDatabaseTable:
                                    mockedCreatingDatabaseTable.return_value = True

                                    with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.create_database_system_user') as mockedCreatingDatabaseUser:
                                        mockedCreatingDatabaseUser.return_value = True

                                        with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.attribute_user_system_privilege') as mockedAttributingPrivilege:
                                            mockedAttributingPrivilege.return_value = True

                                            with mock.patch('homeDatabase.classes.databaseInstaller.DatabaseInstaller.set_database_configuration_booleean_control') as mockedSettingDatabaseConfigurationBooleean:
                                                mockedSettingDatabaseConfigurationBooleean.return_value = False

                                                assert install() == False

