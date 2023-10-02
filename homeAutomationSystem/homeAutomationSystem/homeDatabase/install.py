#!/usr/bin/python3

import os


if __name__ == '__main__':
    from classes.databaseInstaller import *
    from classes.homeDatabase import *
else:
    from .classes.databaseInstaller import *
    from .classes.homeDatabase import *


def install():
    succes = databaseInstalled = False
    configFileCreated = databaseCreated = databaseTablesCreated = False
    systemUserCreated = privilegeAttribued = False
    systemUserName = systemUserPassword = databaseName = ""

    scriptPath = os.path.dirname(os.path.abspath(__file__))
    databaseInstaller = DatabaseInstaller(scriptPath)

                
    #download database system (maria db)
    if databaseInstaller.download_database_system():
        databaseInstalled = True
    else:
        databaseInstalled = False


    if databaseInstalled:
        #get system user information and database name
        systemUserName = databaseInstaller.get_system_username()
        systemUserPassword = databaseInstaller.get_system_user_password()
        databaseName = databaseInstaller.get_database_name()

        if systemUserName and systemUserPassword and databaseName:
            #create the config file of the database
            if databaseInstaller.create_database_config_file(systemUserName, systemUserPassword, databaseName, False):
                configFileCreated = True
            else:
                configFileCreated = False
        else:
            configFileCreated = False

        if configFileCreated:
            #create the database
            if databaseInstaller.create_database(databaseName):
                databaseCreated = True
            else:
                databaseCreated = False
        else:
            databaseCreated = False

        if databaseCreated:
            #create table of the database
            if databaseInstaller.create_database_table(databaseName):
                databaseTablesCreated = True
            else:
                databaseTablesCreated = False
        else:
            databaseTablesCreated = False

        if databaseCreated and databaseTablesCreated:
            #create system user in database system
            if databaseInstaller.create_database_system_user(systemUserName, systemUserPassword):
                systemUserCreated = True
            else:
                systemUserCreated = False
        else:
            systemUserCreated = False

        if systemUserCreated:
            #attribute privilege on database at the system user
            if databaseInstaller.attribute_user_system_privilege(systemUserName, databaseName):
                privilegeAttribued = True
            else:
                privilegeAttribued = False
        else:
            privilegeAttribued = False
    else:
        databaseInstalled = False

    if databaseInstalled and configFileCreated and \
        databaseCreated and databaseTablesCreated and \
        systemUserCreated and privilegeAttribued:
        #set database configuration control booleen on true
        if HomeDatabase(scriptPath + "/configs/databaseConfig.json").check_database_connection():
            if databaseInstaller.set_database_configuration_booleean_control(True):
                succes = True
            else:
                succes = False
        else:
            succes = False
    else:
        succes = False


    if succes:
        print("\nsucces de l'installation de la base de donnée")
    else:
        print("\nechec de l'installation de la base de donnée")

    return succes


if __name__ == '__main__':
	install()