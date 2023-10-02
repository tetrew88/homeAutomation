#!/usr/bin/python3

import os

from classes.zWaveNetwork import *

scriptPath = os.path.dirname(os.path.abspath(__file__))
zwaveNetwork = Network(scriptPath)
userChoice = 0


if zwaveNetwork.start():
    while zwaveNetwork.running:
        userChoice = 0

        while userChoice < 1 or userChoice > 6:
            print("Menu:\n\n")
            print("1.ajouter un module")
            print("2.lister les modules")
            print("3.recuperer un module spécifique")
            print("4.supprimer un module")
            print("5.test")
            print("6.arreter")
            userChoice = input('entrer votre choix: ')

            print("\n\n\n\n")

            try:
                userChoice = int(userChoice)
            except:
                userChoice = 0

        if userChoice == 1:
            zwaveNetwork.add_module()

        elif userChoice == 2:
            for module in zwaveNetwork.modulesList:
                print(module)

        elif userChoice == 3:
            menuChoice = moduleId = maxChoiceNumber = 0

            while moduleId < 1:
                print("modules:")
                for module in zwaveNetwork.modulesList:
                    print("id: {}".format(module.id))
                    print("nom: {}".format(module.name))

                moduleId = input("\nentrer l'id du module: ")

                print("\n\n")

                try:
                    moduleId = int(moduleId)
                except:
                    moduleId = 0

            module = zwaveNetwork.get_module(moduleId)

            if module != False:
                if isinstance(module, ZWaveColorLightController):
                    maxChoiceNumber = 8
                elif isinstance(module, ZWaveLightController):
                    maxChoiceNumber = 7
                elif isinstance(module, ZWaveRelay):
                    maxChoiceNumber = 6
                else:
                    maxChoiceNumber = 4

                print("id: {}".format(module.id))
                print("nom: {}".format(module.name))
                print("emplacement: {}".format(module.location))
                print("niveau de batterie: {}".format(module.batteryLevel))
                if isinstance(module, ZWaveSensor):
                    print('capteur:')
                    print(module.strSensorsList)
                print("\n\n")

                while menuChoice < 1 or menuChoice > maxChoiceNumber:
                    print("menu:\n")
                    print("1.changer le nom du module")
                    print("2.changer l'emplacement du module")
                    print("3.afficher les paramettres")
                    print("4.soigner")

                    if isinstance(module, ZWaveLightController):
                        print("5.allumer")
                        print("6.eteindre")
                        print("7.modifier intensité")

                        if isinstance(module, ZWaveColorLightController):
                            print("8.modifier la couleur")

                    if isinstance(module, ZWaveRelay):
                        print("5.allumer")
                        print("6.eteindre")

                    menuChoice = input("\nentrer votre choix: ")

                    try:
                        menuChoice = int(menuChoice)
                    except:
                        menuChoice = 0

                    print("\n\n")

                if menuChoice == 1:
                    newModuleName = input("entrer le nouveau nom du module: ")
                    zwaveNetwork.set_module_name(module.id, newModuleName)

                elif menuChoice == 2:
                    newModuleEmplacement = input("entrer le nouvel emplacement du module(room id): ")
                    try:
                        newModuleEmplacement = int(newModuleEmplacement)
                        zwaveNetwork.set_module_location(module.id, newModuleEmplacement)
                    except:
                        pass

                elif menuChoice == 3:
                    print('values:')
                    for value in module.values:
                        print(value)
                    print('\nparametters:')
                    for parametters in module.parametters:
                        print(parametters)
                
                elif menuChoice == 4:
                    zwaveNetwork.heal_module(module.id)

                elif menuChoice == 5 and isinstance(module, ZWaveLightController):
                    zwaveNetwork.switch_light_controller_on(module.id)
                
                elif menuChoice == 6 and isinstance(module, ZWaveLightController):
                    zwaveNetwork.switch_light_controller_off(module.id)

                elif menuChoice == 7 and isinstance(module, ZWaveLightController):
                    print("intensité max: {}".format(module.maxLevel))
                    print("intensité min: ".format(module.minLevel))

                    newIntensity = input("\nentrer l'intensite souhaiter: ")

                    try:
                        newIntensity = int(newIntensity)

                        if newIntensity >= module.minLevel or newIntensity <= module.maxLevel:
                            zwaveNetwork.set_light_controller_level(module.id, newIntensity)
                    except:
                        pass

                elif menuChoice == 8 and isinstance(module, ZWaveColorLightController):
                    x = 1
                    print("palette de couleur:")
                    for color in module.colorPalette:
                        print("{}: {}".format(x, color))
                        x = x+1

                    newColorNumber = input("entrer votre choix: ")

                    try:
                        newColorNumber = int(newColorNumber)
                        newColorNumber = newColorNumber-1

                        zwaveNetwork.set_light_controller_color_by_label(module.id, str(module.colorPalette[newColorNumber]))
                    except:
                        pass


                elif menuChoice == 5 and isinstance(module, ZWaveRelay):
                    zwaveNetwork.switch_relay_on(module.id)
                
                elif menuChoice == 6 and isinstance(module, ZWaveRelay):
                    zwaveNetwork.switch_relay_off(module.id)


        elif userChoice == 4:
            moduleId = 0
            succesDeleting = False
            
            while moduleId < 1:
                moduleId = input("entrer l'id du module: ")

                print("\n\n")

                try:
                    moduleId = int(moduleId)
                except:
                    moduleId = 0

            succesDeleting = zwaveNetwork.del_module(moduleId)

            if succesDeleting:
                print("module supprimer avec succes")
            else:
                print("erreur dans la supression")

        elif userChoice == 5:
            module = zwaveNetwork.get_module(30)
            module.set_value(72057594551468049, 50)

        elif userChoice == 6:
            zwaveNetwork.save_modification()
            zwaveNetwork.stop()
        else:
            pass

        if zwaveNetwork.isReady:
            zwaveNetwork.save_modification()