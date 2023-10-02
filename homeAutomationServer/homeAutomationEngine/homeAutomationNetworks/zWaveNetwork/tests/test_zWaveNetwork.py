import os
import unittest
import sys
import mock

from unittest.mock import patch, mock_open, MagicMock

sys.path.append("..")

from fakeClasses.fakeZwaveNetwork import *
from fakeClasses.fakeNode import *

from zWaveNetwork.classes.zWaveNetwork import *

from zWaveNetwork.classes.zWaveModules.zWaveModule import *

from zWaveNetwork.classes.zWaveModules.zWaveNetworkController import *

from zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveLightController import *
from zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveColorLightController import *

from zWaveNetwork.classes.zWaveModules.zWaveRelays.zWaveRelay import *

from zWaveNetwork.classes.zWaveModules.zWaveSensors.zWaveSensor import *


class Test_ZWaveNetwork:
    """
        testing class of the zwaveNetwork
    """       


    zWaveNetwork = Network(os.path.abspath(__file__))
    goodZWaveNetwork = FakeZwaveNetwork(20, 10, True)
    badZWaveNetwork = FakeZwaveNetwork(20, 1, False)



    """PROPERTYS"""
    def test_homeId_property(self):
        """
            1.check if method return good data
            2.check if method detecte failure zwave network
        """

        #check if method return good data
        self.zWaveNetwork.network = self.goodZWaveNetwork
        assert self.zWaveNetwork.homeId == 20
        assert isinstance(self.zWaveNetwork.homeId, int)

        #test with failure zwaveNetwork
        self.zWaveNetwork.network = False
        assert isinstance(self.zWaveNetwork.homeId, bool)
        assert self.zWaveNetwork.homeId is False


    def test_state_property(self):
        """
            1.check if method return good type of data
            2.check if method detect bad zwave network
        """

        #check if method return good type of data
        self.zWaveNetwork.network = self.goodZWaveNetwork
        assert isinstance(self.zWaveNetwork.state, int)
        assert self.zWaveNetwork.state == 10
        
        self.zWaveNetwork.network = self.badZWaveNetwork
        assert isinstance(self.zWaveNetwork.state, int)
        assert self.zWaveNetwork.state == 1

        #check if method detect bad zwave network
        self.zWaveNetwork.network = False
        assert isinstance(self.zWaveNetwork.state, bool)
        assert self.zWaveNetwork.state is False


    def test_isReady_property(self):
        """
            1.check if method return good type of data
            2.check if method detect bad zwave network
        """

        #check if method return good type of data
        self.zWaveNetwork.network = self.goodZWaveNetwork
        assert isinstance(self.zWaveNetwork.isReady, bool)
        assert self.zWaveNetwork.isReady is True

        self.zWaveNetwork.network = self.badZWaveNetwork
        assert isinstance(self.zWaveNetwork.isReady, bool)
        assert self.zWaveNetwork.isReady is False

        #check if method detect bad zwave network
        self.zWaveNetwork.network = False
        assert isinstance(self.zWaveNetwork.isReady, bool)
        assert self.zWaveNetwork.isReady is False


    def test_controller_property(self):
        """
            1.check if method return good type of data
            2.check if method detect bad zwave network
        """

        #check if method return good type of data
        self.zWaveNetwork.network = self.goodZWaveNetwork
        assert isinstance(self.zWaveNetwork.controller, ZWaveNetworkController)

        self.zWaveNetwork.network = self.badZWaveNetwork
        assert isinstance(self.zWaveNetwork.controller, ZWaveNetworkController)

        #check if method detect bad zwave network
        self.zWaveNetwork.network = False
        assert self.zWaveNetwork.controller is False


    def test_controllerPath(self):
        """
            1.check if method return good type of data
            2.test if method detect inexistance of data
            3.check if method file error
        """

        open_mock = mock_open()
        jsonMock = MagicMock( side_effect = [ { "assignedZwaveControllerPath": "test" } ] )

        with patch("builtins.open", open_mock, create=False):
            with patch("json.load", jsonMock):
                #check if method return good type of data
                data = self.zWaveNetwork.controllerPath
                assert isinstance(data, str)
                assert data == "test"

        jsonMock = MagicMock( side_effect = [ { "NULL": "NULL" } ] )
        with patch("builtins.open", open_mock, create=False):
            #test if method detect inexistance of data
            assert self.zWaveNetwork.controllerPath == False

        with patch("builtins.open", open_mock, create=False):
            #check if method file error
            open_mock.side_effect = IOError()
            assert self.zWaveNetwork.controllerPath == False


    def test_zwaveConfigFolderPath(self):
        """
            1.check if method return good type of data
            2.test if method detect inexistance of data
            3.check if method detect file error
        """

        open_mock = mock_open()
        jsonMock = MagicMock( side_effect = [ { "zWaveConfigFolderPath": "test" } ] )

        with patch("builtins.open", open_mock, create=False):
            with patch("json.load", jsonMock):
                #check if method return good type of data
                data = self.zWaveNetwork.zwaveConfigFolderPath
                assert isinstance(data, str)
                assert data == "test"

        jsonMock = MagicMock( side_effect = [ { "NULL": "NULL" } ] )
        with patch("builtins.open", open_mock, create=False):
            #test if method detect inexistance of data
            assert self.zWaveNetwork.zwaveConfigFolderPath == False

        with patch("builtins.open", open_mock, create=False):
            #check if method detect file error
            open_mock.side_effect = IOError()
            assert self.zWaveNetwork.zwaveConfigFolderPath == False


    def test_networkConfigured(self):
        """
            1.check if method return good type of data
            2.test if method detect inexistance of data
            3.check if method file error
        """

        open_mock = mock_open()
        jsonMock = MagicMock( side_effect = [ { "networkConfigured": True } ] )

        with patch("builtins.open", open_mock, create=False):
            with patch("json.load", jsonMock):
                #check if method return good type of data
                data = self.zWaveNetwork.networkConfigured
                assert isinstance(data, bool)
                assert data == True

        jsonMock = MagicMock( side_effect = [ { "NULL": "NULL" } ] )
        with patch("builtins.open", open_mock, create=False):
            #test if method detect inexistance of data
            assert self.zWaveNetwork.networkConfigured == False

        with patch("builtins.open", open_mock, create=False):
            #check if method file error
            open_mock.side_effect = IOError()
            assert self.zWaveNetwork.networkConfigured == False


    def test_moduleList(self):
        """
            1.check if method return good type of data
            2.check if method detect bad zwave network
        """

        #check if method return good type of data
        self.zWaveNetwork.network = self.goodZWaveNetwork
        moduleList = self.zWaveNetwork.modulesList
        assert len(moduleList) == 2
        for module in moduleList:
            assert isinstance(module, ZWaveModule)

        #check if method detect bad zwave network
        self.zWaveNetwork.network = self.badZWaveNetwork
        moduleList = self.zWaveNetwork.modulesList
        assert moduleList == False

        self.zWaveNetwork.network = False
        moduleList = self.zWaveNetwork.modulesList
        assert moduleList == False



    """METHODS"""
    def test_load(self):
        """
            1.check if method succes
            2.check if method detect error
        """
        
        #check if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork
        assert self.zWaveNetwork.load() == True

        #check if method detect error
        self.zWaveNetwork.network = False
        assert self.zWaveNetwork.load() == False


    def test_start(self):
        pass


    def test_stop(self):
        """
            1.check if method succes
            2.check if method detect failed stop network
            3.check if method detect failing saving modification
            4.check if method detect already stopped
        """
        
        #check if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
            mockedSavingModification.return_value = True

            with mock.patch('fakeClasses.fakeZwaveNetwork.FakeZwaveNetwork.stop') as mockedStop:
                mockedStop.return_value = True

                assert self.zWaveNetwork.stop() == True


        #check if method detect failed stop network
        self.zWaveNetwork.network = self.badZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
            mockedSavingModification.return_value = True

            with mock.patch('fakeClasses.fakeZwaveNetwork.FakeZwaveNetwork.stop') as mockedStop:
                mockedStop.return_value = False

                assert self.zWaveNetwork.stop() == False


        #check if method detect failing saving modification
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
            mockedSavingModification.return_value = False

            with mock.patch('fakeClasses.fakeZwaveNetwork.FakeZwaveNetwork.stop') as mockedStop:
                mockedStop.return_value = True

                assert self.zWaveNetwork.stop() == False

        
        #check if method detect already stopped
        self.zWaveNetwork.network = False
        assert self.zWaveNetwork.stop() == True


    def test_save_modification(self):
        """
            1.check if method succes
            2.check if method detect error during saving modification
            3.check if method detecte network isn't ready
            4.check if method detect bad zwave network
        """
        
        #check if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('fakeClasses.fakeZwaveNetwork.FakeZwaveNetwork.write_config') as mockedWrittingConfig:
                mockedWrittingConfig.return_value = True
                
                assert self.zWaveNetwork.save_modification() == True


        #check if method detect error during saving modification
        self.zWaveNetwork.network = self.badZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('fakeClasses.fakeZwaveNetwork.FakeZwaveNetwork.write_config') as mockedWrittingConfig:
                mockedWrittingConfig.side_effect = Exception()
                
                assert self.zWaveNetwork.save_modification() == False


        #check if method detecte network isn't ready
        self.zWaveNetwork.network = self.badZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = False

            with mock.patch('fakeClasses.fakeZwaveNetwork.FakeZwaveNetwork.write_config') as mockedWrittingConfig:
                mockedWrittingConfig.side_effect = Exception()
                
                assert self.zWaveNetwork.save_modification() == False


        #check if method detect bad zwave network
        self.zWaveNetwork.network = False
        assert self.zWaveNetwork.save_modification() == False


    def test_restart(self):
        """
            1.check if method succes
            2.check if method detect start error
            3.check if method detect load error
            4.check if method detect stop error
            5.check if method detect bad zwave network
        """
        
        #check if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.stop') as mockedStop:
            mockedStop.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.load') as mockedLoad:
                mockedLoad.return_value = True

                with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.start') as mockedStart:
                    mockedStart.return_value = True

                    assert self.zWaveNetwork.restart() == True

        
        #check if method detect start error
        self.zWaveNetwork.network = self.badZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.stop') as mockedStop:
            mockedStop.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.load') as mockedLoad:
                mockedLoad.return_value = True

                with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.start') as mockedStart:
                    mockedStart.return_value = False

                    assert self.zWaveNetwork.restart() == False


        #check if method detect load error
        self.zWaveNetwork.network = self.badZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.stop') as mockedStop:
            mockedStop.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.load') as mockedLoad:
                mockedLoad.return_value = False

                with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.start') as mockedStart:
                    mockedStart.return_value = True

                    assert self.zWaveNetwork.restart() == False


        #check if method detect stop error
        self.zWaveNetwork.network = self.badZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.stop') as mockedStop:
            mockedStop.return_value = False

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.load') as mockedLoad:
                mockedLoad.return_value = True

                with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.start') as mockedStart:
                    mockedStart.return_value = True

                    assert self.zWaveNetwork.restart() == False

        
        #check if method detect bad zwave network
        self.zWaveNetwork.network = False
        assert self.zWaveNetwork.restart() == False


    def test_get_module(self):
        """
            1.check if method succes
            2.check if method detect not found module
            3.check if method detect bad moduleId parametters
            4.check if method detect bad zwave network
        """
        
        #check if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork

        module = self.zWaveNetwork.get_module(1)
        assert isinstance(module, ZWaveModule)
        assert module.id == 1

        #check if method detect not found module
        self.zWaveNetwork.network = self.goodZWaveNetwork

        assert self.zWaveNetwork.get_module(100) == False

        #check if method detect bad moduleId parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork

        assert self.zWaveNetwork.get_module("1") == False

        #check if method detect bad zwave network
        self.zWaveNetwork.network = False
        assert self.zWaveNetwork.get_module(1) == False


    def test_add_module(self):
        """
            1.check if method succes
            2.check if method detect if the network isn't ready
            3.check if method detect bad zwave network
        """
        
        #check if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork
        moduleId = False

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            moduleId = self.zWaveNetwork.add_module()

            assert isinstance(moduleId, int)


        #check if method detect if the network isn't ready
        self.zWaveNetwork.network = self.goodZWaveNetwork
        moduleId = False

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            self.zWaveNetwork.add_module() == False


        #check if method detect bad zwave network
        self.zWaveNetwork.network = False
        self.zWaveNetwork.add_module() == False


    def test_del_module(self):
        """
            1.check if method succes
            2.check if method detect if the network isn't ready
            3.check if method detect bad parammetters
            4.check if method detect bad zwave network
        """
        
        #check if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork
        moduleId = False

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            self.zWaveNetwork.del_module(1) == True

        
        #check if method detect if the network isn't ready
        self.zWaveNetwork.network = self.goodZWaveNetwork
        moduleId = False

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = False

            self.zWaveNetwork.del_module(1) == False

        
        #check if method detect bad parammetters
        self.zWaveNetwork.network = self.goodZWaveNetwork
        moduleId = False

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            self.zWaveNetwork.del_module("1") == False

        
        #check if method detect inexistance of the node
        self.zWaveNetwork.network = self.goodZWaveNetwork
        moduleId = False

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            self.zWaveNetwork.del_module(1000) == False


        #check if method detect bad zwave network
        self.zWaveNetwork.network = False
        self.zWaveNetwork.del_module(1) == False


    def test_set_module_name(self):
        """
            1.check if method succes
            2.test if method detect bad moduleId parametters
            3.test if method detect bad newName parametters
            4.test if method detect error during name modification
            5.test if method detect error during saving modification
            6.test if method detect error during getting module
            7.test if method detect bad zwave network
        """
        
        #check if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.set_name') as mockedSettingName:
                mockedSettingName.return_value = True

                with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                    mockedSavingModification.return_value = True

                    assert self.zWaveNetwork.set_module_name(1, "test") == True


        #test if method detect bad moduleId parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.set_name') as mockedSettingName:
                mockedSettingName.return_value = True

                with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                    mockedSavingModification.return_value = True

                    assert self.zWaveNetwork.set_module_name("1", "test") == False


        #test if method detect bad newName parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.set_name') as mockedSettingName:
                mockedSettingName.return_value = True

                with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                    mockedSavingModification.return_value = True

                    assert self.zWaveNetwork.set_module_name(1, 1) == False


        """"   
            #test if method detect if the network isn't ready
            self.zWaveNetwork.network = self.goodZWaveNetwork

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
                mockedIsReady.return_value = False

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.set_name') as mockedSettingName:
                    mockedSettingName.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.set_module_name(1, "test") == False
        """


        #test if method detect error during name modification
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.set_name') as mockedSettingName:
                mockedSettingName.return_value = False

                with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                    mockedSavingModification.return_value = True

                    assert self.zWaveNetwork.set_module_name(1, "test") == False

                
        #test if method detect error during saving modification
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.set_name') as mockedSettingName:
                mockedSettingName.return_value = True

                with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                    mockedSavingModification.return_value = False

                    assert self.zWaveNetwork.set_module_name(1, "test") == False


        #test if method detect error during getting module
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = False

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.set_name') as mockedSettingName:
                    mockedSettingName.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.set_module_name(1, "test") == False


        #test if method detect bad zwave network
        self.zWaveNetwork.network = False
        assert self.zWaveNetwork.set_module_name(1, "test") == False


    def test_set_module_location(self):
        """
            1.check if method succes
            2.test if method detect bad moduleId parametters
            3.test if method detect bad newlocation parametters
            4.test if method detect error during location modification
            5.test if method detect error during saving modification
            6.test if method detect error during getting module
            7.test if method detect bad zwave network
        """

        #check if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.set_location') as mockedSettingLocation:
                mockedSettingLocation.return_value = True

                with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                    mockedSavingModification.return_value = True

                    assert self.zWaveNetwork.set_module_location(1, 1) == True


        #test if method detect bad moduleId parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.set_location') as mockedSettingLocation:
                mockedSettingLocation.return_value = True

                with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                    mockedSavingModification.return_value = True

                    assert self.zWaveNetwork.set_module_location("1", 1) == False


        #test if method detect bad newLocation parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.set_location') as mockedSettingLocation:
                mockedSettingLocation.return_value = True

                with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                    mockedSavingModification.return_value = True

                    assert self.zWaveNetwork.set_module_location(1, "1") == False


        """
            #test if method detect if the network isn't ready
            self.zWaveNetwork.network = self.goodZWaveNetwork

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
                mockedIsReady.return_value = False

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.set_location') as mockedSettingName:
                    mockedSettingName.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.set_module_location(1, 1) == False
        """

        #test if method detect error during location modification
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.set_location') as mockedSettingLocation:
                mockedSettingLocation.return_value = False

                with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                    mockedSavingModification.return_value = True

                    assert self.zWaveNetwork.set_module_location(1, 1) == False


        #test if method detect error during saving modification
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.set_location') as mockedSettingLocation:
                mockedSettingLocation.return_value = True

                with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                    mockedSavingModification.return_value = False

                    assert self.zWaveNetwork.set_module_location(1, 1) == False


        #test if method detect error during getting module
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True


            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = False

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.set_location') as mockedSettingLocation:
                    mockedSettingLocation.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.set_module_location(1, 1) == False


        #test if method detect bad zwave network
        self.zWaveNetwork.network = False
        assert self.zWaveNetwork.set_module_location(1, 1) == False


    def test_set_module_value(self):
        """
            1.check if method succes
            2.test if method detect bad moduleId parametters
            3.test if method detect bad valueId parametters
            4.test if method detect error during value modification
            5.test if method detect error during saving modification
            6.test if method detect error during getting module
            7.test if method detect bad zwave network
        """

        #check if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.set_value_data') as mockedSettingValue:
                mockedSettingValue.return_value = True

                with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                    mockedSavingModification.return_value = True

                    assert self.zWaveNetwork.set_module_value(1, 1, 1) == True


        #test if method detect bad moduleId parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.set_value_data') as mockedSettingValue:
                mockedSettingValue.return_value = True

                with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                    mockedSavingModification.return_value = True

                    assert self.zWaveNetwork.set_module_value("1", 1, 1) == False

        
        #test if method detect bad valueId parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.set_value_data') as mockedSettingValue:
                mockedSettingValue.return_value = True

                with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                    mockedSavingModification.return_value = True

                    assert self.zWaveNetwork.set_module_value(1, "1", 1) == False

        """
            #check if method detect if network isn't ready
            self.zWaveNetwork.network = self.goodZWaveNetwork

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
                mockedIsReady.return_value = False

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.set_value_data') as mockedSettingValue:
                    mockedSettingValue.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.set_module_value(1, 1, 1) == True
        """


        #test if method detect error during value modification
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.set_value_data') as mockedSettingValue:
                mockedSettingValue.return_value = False

                with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                    mockedSavingModification.return_value = True

                    assert self.zWaveNetwork.set_module_value(1, 1, 1) == False


        #test if method detect error during saving modification
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.set_value_data') as mockedSettingValue:
                mockedSettingValue.return_value = True

                with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                    mockedSavingModification.return_value = False

                    assert self.zWaveNetwork.set_module_value(1, 1, 1) == False


        #test if method detect error during getting module
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = False

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.set_value_data') as mockedSettingValue:
                    mockedSettingValue.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.set_module_value(1, 1, 1) == False

        #test if method detect bad zwave network
        self.zWaveNetwork.network = False
        assert self.zWaveNetwork.set_module_value(1, 1, 1) == False


    def test_set_light_controller_level(self):
        """
            1.test if method succes
            2.test if method detect bad moduleId parametters
            3.test if method detect bad newLevel parametters
            4.test if method detect error during level modification
            5.test if method detect error during saving modification
            6.test if method detect error during getting module
            7.test if method detect bad module type selected
            8.test if method detect bad zwave network
        """
        
        #test if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = ZWaveLightController(self.goodZWaveNetwork.nodes["0001"])

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveLightController.ZWaveLightController.set_level') as mockedSettingLevel:
                    mockedSettingLevel.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.set_light_controller_level(1, 1) == True

        
        #test if method detect bad moduleId parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = ZWaveLightController(self.goodZWaveNetwork.nodes["0001"])

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveLightController.ZWaveLightController.set_level') as mockedSettingLevel:
                    mockedSettingLevel.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.set_light_controller_level("1", 1) == False


        #test if method detect bad newLevel parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = ZWaveLightController(self.goodZWaveNetwork.nodes["0001"])

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveLightController.ZWaveLightController.set_level') as mockedSettingLevel:
                    mockedSettingLevel.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.set_light_controller_level(1, "1") == False


        """
            #check if method detect if the network isn't ready
            self.zWaveNetwork.network = self.goodZWaveNetwork

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
                mockedIsReady.return_value = False

                with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                    mockedGettingModule.return_value = ZWaveLightController(self.goodZWaveNetwork.nodes["0001"])

                    with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveLightController.ZWaveLightController.set_level') as mockedSettingLevel:
                        mockedSettingLevel.return_value = True

                        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                            mockedSavingModification.return_value = True

                            assert self.zWaveNetwork.set_light_controller_level(1, 1) == False
        """


        #test if method detect error during level modification
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = ZWaveLightController(self.goodZWaveNetwork.nodes["0001"])

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveLightController.ZWaveLightController.set_level') as mockedSettingLevel:
                    mockedSettingLevel.return_value = False

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.set_light_controller_level(1, 1) == False


        #test if method detect error during saving modification
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = ZWaveLightController(self.goodZWaveNetwork.nodes["0001"])

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveLightController.ZWaveLightController.set_level') as mockedSettingLevel:
                    mockedSettingLevel.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = False

                        assert self.zWaveNetwork.set_light_controller_level(1, 1) == False


        #test if method detect error during getting module
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = False

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveLightController.ZWaveLightController.set_level') as mockedSettingLevel:
                    mockedSettingLevel.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.set_light_controller_level(1, 1) == False


        #test if method detect bad module type selected
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = ZWaveRelay(self.goodZWaveNetwork.nodes["0001"])

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveLightController.ZWaveLightController.set_level') as mockedSettingLevel:
                    mockedSettingLevel.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.set_light_controller_level(1, 1) == False


        #test if method detect bad zwave network
        self.zWaveNetwork.network = False
        assert self.zWaveNetwork.set_light_controller_level(1, 1) == False


    def test_set_light_controller_color_by_label(self):
        """
            1.test if method succes
            2.test if method detect bad moduleId parametters
            3.test if method detect bad newColorLabel parametters
            4.test if method detect error during color modification
            5.test if method detect error during saving modification
            6.test if method detect error during getting module
            7.test if method detect bad module type selected
            8.test if method detect bad zwave network
        """
        
        #test if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = ZWaveColorLightController(self.goodZWaveNetwork.nodes["0001"])

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveColorLightController.ZWaveColorLightController.set_color_by_label') as mockedSettingLabel:
                    mockedSettingLabel.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.set_light_controller_color_by_label(1, "red") == True


        #test if method detect bad moduleId parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = ZWaveColorLightController(self.goodZWaveNetwork.nodes["0001"])

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveColorLightController.ZWaveColorLightController.set_color_by_label') as mockedSettingLabel:
                    mockedSettingLabel.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.set_light_controller_color_by_label("1", "red") == False


        #test if method detect bad newColorLabel parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = ZWaveColorLightController(self.goodZWaveNetwork.nodes["0001"])

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveColorLightController.ZWaveColorLightController.set_color_by_label') as mockedSettingLabel:
                    mockedSettingLabel.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.set_light_controller_color_by_label(1, 1) == False


        """
            #test if method detect bad newColorLabel parametters
            self.zWaveNetwork.network = self.goodZWaveNetwork

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
                mockedIsReady.return_value = False

                with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                    mockedGettingModule.return_value = ZWaveColorLightController(self.goodZWaveNetwork.nodes["0001"])

                    with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveColorLightController.ZWaveColorLightController.set_color_by_label') as mockedSettingLabel:
                        mockedSettingLabel.return_value = True

                        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                            mockedSavingModification.return_value = True

                            assert self.zWaveNetwork.set_light_controller_color_by_label(1, "red") == False
        """


        #test if method detect error during color modification
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = ZWaveColorLightController(self.goodZWaveNetwork.nodes["0001"])

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveColorLightController.ZWaveColorLightController.set_color_by_label') as mockedSettingLabel:
                    mockedSettingLabel.return_value = False

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.set_light_controller_color_by_label(1, "red") == False


        #test if method detect error during saving modification
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = ZWaveColorLightController(self.goodZWaveNetwork.nodes["0001"])

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveColorLightController.ZWaveColorLightController.set_color_by_label') as mockedSettingLabel:
                    mockedSettingLabel.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = False

                        assert self.zWaveNetwork.set_light_controller_color_by_label(1, "red") == False


        #test if method detect error during getting module
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = False

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveColorLightController.ZWaveColorLightController.set_color_by_label') as mockedSettingLabel:
                    mockedSettingLabel.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.set_light_controller_color_by_label(1, "red") == False

        
        #test if method detect bad module type selected
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = ZWaveRelay(self.goodZWaveNetwork.nodes["0001"])

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveColorLightController.ZWaveColorLightController.set_color_by_label') as mockedSettingLabel:
                    mockedSettingLabel.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.set_light_controller_color_by_label(1, "red") == False


        #test if method detect bad zwave network
        self.zWaveNetwork.network = False
        assert self.zWaveNetwork.set_light_controller_color_by_label(1, "red") == False


    def test_set_light_controller_color_by_rgbw(self):
        """
            1.test if method succes
            2.test if method detect bad moduleId parametters
            3.test if method detect bad newColorData parametters
            4.test if method detect error during color modification
            5.test if method detect error during saving modification
            6.test if method detect error during getting module
            7.test if method detect bad module type selected
            8.test if method detect bad zwave network
        """
        
        #test if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = ZWaveColorLightController(self.goodZWaveNetwork.nodes["0001"])

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveColorLightController.ZWaveColorLightController.set_color_by_rgbw') as mockedSettingLabel:
                    mockedSettingLabel.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.set_light_controller_color_by_rgbw(1, "#0000") == True


        #test if method detect bad moduleId parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = ZWaveColorLightController(self.goodZWaveNetwork.nodes["0001"])

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveColorLightController.ZWaveColorLightController.set_color_by_rgbw') as mockedSettingLabel:
                    mockedSettingLabel.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.set_light_controller_color_by_rgbw("1", "#0000") == False


        #test if method detect bad newColorData parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = ZWaveColorLightController(self.goodZWaveNetwork.nodes["0001"])

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveColorLightController.ZWaveColorLightController.set_color_by_rgbw') as mockedSettingLabel:
                    mockedSettingLabel.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.set_light_controller_color_by_rgbw(1, 1) == False


        """
            #test if method detect bad newColorLabel parametters
            self.zWaveNetwork.network = self.goodZWaveNetwork

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
                mockedIsReady.return_value = False

                with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                    mockedGettingModule.return_value = ZWaveColorLightController(self.goodZWaveNetwork.nodes["0001"])

                    with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveColorLightController.ZWaveColorLightController.set_color_by_rgbw') as mockedSettingLabel:
                        mockedSettingLabel.return_value = True

                        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                            mockedSavingModification.return_value = True

                            assert self.zWaveNetwork.set_light_controller_color_by_rgbw(1, "#0000") == False
        """


        #test if method detect error during color modification
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = ZWaveColorLightController(self.goodZWaveNetwork.nodes["0001"])

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveColorLightController.ZWaveColorLightController.set_color_by_rgbw') as mockedSettingLabel:
                    mockedSettingLabel.return_value = False

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.set_light_controller_color_by_rgbw(1, "#0000") == False


        #test if method detect error during saving modification
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = ZWaveColorLightController(self.goodZWaveNetwork.nodes["0001"])

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveColorLightController.ZWaveColorLightController.set_color_by_rgbw') as mockedSettingLabel:
                    mockedSettingLabel.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = False

                        assert self.zWaveNetwork.set_light_controller_color_by_rgbw(1, "#0000") == False


        #test if method detect error during getting module
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = False

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveColorLightController.ZWaveColorLightController.set_color_by_rgbw') as mockedSettingLabel:
                    mockedSettingLabel.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.set_light_controller_color_by_rgbw(1, "#0000") == False

        
        #test if method detect bad module type selected
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = ZWaveRelay(self.goodZWaveNetwork.nodes["0001"])

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveColorLightController.ZWaveColorLightController.set_color_by_rgbw') as mockedSettingLabel:
                    mockedSettingLabel.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.set_light_controller_color_by_rgbw(1, "#0000") == False


        #test if method detect bad zwave network
        self.zWaveNetwork.network = False
        assert self.zWaveNetwork.set_light_controller_color_by_rgbw(1, "#0000") == False


    def test_switch_light_controller(self):
        """
            1.test if method succes
            2.test if method detect bad moduleId parametters
            3.test if method detect bad value parametters
            4.test if method detect error during switching
            5.test if method detect error during saving modification
            6.test if method detect error during getting module
            7.test if method detect bad module type selected
            8.test if method detect bad zwave network
        """

        #test for true value
        #test if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = ZWaveLightController(self.goodZWaveNetwork.nodes["0001"])

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveLightController.ZWaveLightController.switch_on') as mockedSwitchOn:
                    mockedSwitchOn.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.switch_light_controller(1, True) == True


        #test if method detect bad moduleId parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = ZWaveLightController(self.goodZWaveNetwork.nodes["0001"])

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveLightController.ZWaveLightController.switch_on') as mockedSwitchOn:
                    mockedSwitchOn.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.switch_light_controller("1", True) == False


        #test if method detect bad value parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = ZWaveLightController(self.goodZWaveNetwork.nodes["0001"])

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveLightController.ZWaveLightController.switch_on') as mockedSwitchOn:
                    mockedSwitchOn.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.switch_light_controller(1, "test") == False


        #test if method detect error during switching
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = ZWaveLightController(self.goodZWaveNetwork.nodes["0001"])

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveLightController.ZWaveLightController.switch_on') as mockedSwitchOn:
                    mockedSwitchOn.return_value = False

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.switch_light_controller(1, True) == False


        #test if method detect error during saving modification
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = ZWaveLightController(self.goodZWaveNetwork.nodes["0001"])

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveLightController.ZWaveLightController.switch_on') as mockedSwitchOn:
                    mockedSwitchOn.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = False

                        assert self.zWaveNetwork.switch_light_controller(1, True) == False


        #test if method detect error during getting module
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = False

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveLightController.ZWaveLightController.switch_on') as mockedSwitchOn:
                    mockedSwitchOn.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.switch_light_controller(1, True) == False


        #test if method detect bad module type selected
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = ZWaveRelay(self.goodZWaveNetwork.nodes["0001"])

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveLightController.ZWaveLightController.switch_on') as mockedSwitchOn:
                    mockedSwitchOn.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.switch_light_controller(1, True) == False


        #test if method detect bad zwave network
        self.zWaveNetwork.network = False
        assert self.zWaveNetwork.switch_light_controller(1, True) == False


        #test for false value
        #test if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = ZWaveLightController(self.goodZWaveNetwork.nodes["0001"])

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveLightController.ZWaveLightController.switch_off') as mockedSwitchOff:
                    mockedSwitchOff.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.switch_light_controller(1, False) == True

        
        #test if method detect bad moduleId parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = ZWaveLightController(self.goodZWaveNetwork.nodes["0001"])

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveLightController.ZWaveLightController.switch_off') as mockedSwitchOff:
                    mockedSwitchOff.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.switch_light_controller("1", False) == False


        #test if method detect bad value parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = ZWaveLightController(self.goodZWaveNetwork.nodes["0001"])

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveLightController.ZWaveLightController.switch_off') as mockedSwitchOff:
                    mockedSwitchOff.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.switch_light_controller(1, "test") == False


        #test if method detect error during switching
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = ZWaveLightController(self.goodZWaveNetwork.nodes["0001"])

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveLightController.ZWaveLightController.switch_off') as mockedSwitchOff:
                    mockedSwitchOff.return_value = False

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.switch_light_controller(1, False) == False


        #test if method detect error during saving modification
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = ZWaveLightController(self.goodZWaveNetwork.nodes["0001"])

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveLightController.ZWaveLightController.switch_off') as mockedSwitchOff:
                    mockedSwitchOff.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = False

                        assert self.zWaveNetwork.switch_light_controller(1, False) == False


        #test if method detect error during getting module
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = False

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveLightController.ZWaveLightController.switch_off') as mockedSwitchOff:
                    mockedSwitchOff.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.switch_light_controller(1, False) == False


        #test if method detect bad module type selected
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = ZWaveRelay(self.goodZWaveNetwork.nodes["0001"])

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveLightController.ZWaveLightController.switch_off') as mockedSwitchOff:
                    mockedSwitchOff.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.switch_light_controller(1, False) == False


        #test if method detect bad zwave network
        self.zWaveNetwork.network = False
        assert self.zWaveNetwork.switch_light_controller(1, False) == False


    def test_switch_light_controller_on(self):
        """
            1.test if method succes
            2.test if method detect bad moduleId parametters
            3.test if method detect error during switching
            4.test if method detect bad zwave network
        """
        
        #test if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.switch_light_controller') as mockedSwitching:
                mockedSwitching.return_value = True

                assert self.zWaveNetwork.switch_light_controller_on(1) == True


        #test if method detect bad moduleId parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.switch_light_controller') as mockedSwitching:
                mockedSwitching.return_value = True

                assert self.zWaveNetwork.switch_light_controller_on("1") == False


        #test if method detect error during switching
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.switch_light_controller') as mockedSwitching:
                mockedSwitching.return_value = False

                assert self.zWaveNetwork.switch_light_controller_on(1) == False


        #test if method detect bad zwave network
        self.zWaveNetwork.network = False
        assert self.zWaveNetwork.switch_light_controller_on(1) == False


    def test_switch_light_controller_off(self):
        """
            1.test if method succes
            2.test if method detect bad moduleId parametters
            3.test if method detect error during switching
            4.test if method detect bad zwave network
        """
        
        #test if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.switch_light_controller') as mockedSwitching:
                mockedSwitching.return_value = True

                assert self.zWaveNetwork.switch_light_controller_off(1) == True


        #test if method detect bad moduleId parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.switch_light_controller') as mockedSwitching:
                mockedSwitching.return_value = True

                assert self.zWaveNetwork.switch_light_controller_off("1") == False


        #test if method detect error during switching
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.switch_light_controller') as mockedSwitching:
                mockedSwitching.return_value = False

                assert self.zWaveNetwork.switch_light_controller_off(1) == False


        #test if method detect bad zwave network
        self.zWaveNetwork.network = False
        assert self.zWaveNetwork.switch_light_controller_off(1) == False


    def test_switch_relay(self):
        """
            1.test if method succes
            2.test if method detect bad moduleId parametters
            3.test if method detect bad value parametters
            4.test if method detect error during switching
            5.test if method detect error during saving modification
            6.test if method detect error during getting module
            7.test if method detect bad module type selected
            8.test if method detect bad zwave network
        """

        #test for true value
        #test if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = ZWaveRelay(self.goodZWaveNetwork.nodes["0001"])

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveRelays.zWaveRelay.ZWaveRelay.switch_on') as mockedSwitchOn:
                    mockedSwitchOn.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.switch_relay(1, True) == True


        #test if method detect bad moduleId parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = ZWaveRelay(self.goodZWaveNetwork.nodes["0001"])

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveRelays.zWaveRelay.ZWaveRelay.switch_on') as mockedSwitchOn:
                    mockedSwitchOn.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.switch_relay("1", True) == False


        #test if method detect bad value parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = ZWaveRelay(self.goodZWaveNetwork.nodes["0001"])

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveRelays.zWaveRelay.ZWaveRelay.switch_on') as mockedSwitchOn:
                    mockedSwitchOn.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.switch_relay(1, "test") == False


        #test if method detect error during switching
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = ZWaveRelay(self.goodZWaveNetwork.nodes["0001"])

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveRelays.zWaveRelay.ZWaveRelay.switch_on') as mockedSwitchOn:
                    mockedSwitchOn.return_value = False

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.switch_relay(1, True) == False


        #test if method detect error during saving modification
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = ZWaveRelay(self.goodZWaveNetwork.nodes["0001"])

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveRelays.zWaveRelay.ZWaveRelay.switch_on') as mockedSwitchOn:
                    mockedSwitchOn.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = False

                        assert self.zWaveNetwork.switch_relay(1, True) == False


        #test if method detect error during getting module
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = False

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveRelays.zWaveRelay.ZWaveRelay.switch_on') as mockedSwitchOn:
                    mockedSwitchOn.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.switch_relay(1, True) == False


        #test if method detect bad module type selected
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = ZWaveLightController(self.goodZWaveNetwork.nodes["0001"])

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveRelays.zWaveRelay.ZWaveRelay.switch_on') as mockedSwitchOn:
                    mockedSwitchOn.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.switch_relay(1, True) == False


        #test if method detect bad zwave network
        self.zWaveNetwork.network = False
        assert self.zWaveNetwork.switch_relay(1, True) == False



        #test for false value
        ##test if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = ZWaveRelay(self.goodZWaveNetwork.nodes["0001"])

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveRelays.zWaveRelay.ZWaveRelay.switch_off') as mockedSwitchOff:
                    mockedSwitchOff.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.switch_relay(1, False) == True


        #test if method detect bad moduleId parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = ZWaveRelay(self.goodZWaveNetwork.nodes["0001"])

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveRelays.zWaveRelay.ZWaveRelay.switch_off') as mockedSwitchOff:
                    mockedSwitchOff.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.switch_relay("1", False) == False


        #test if method detect bad value parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = ZWaveRelay(self.goodZWaveNetwork.nodes["0001"])

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveRelays.zWaveRelay.ZWaveRelay.switch_off') as mockedSwitchOff:
                    mockedSwitchOff.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.switch_relay(1, "test") == False


        #test if method detect error during switching
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = ZWaveRelay(self.goodZWaveNetwork.nodes["0001"])

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveRelays.zWaveRelay.ZWaveRelay.switch_off') as mockedSwitchOff:
                    mockedSwitchOff.return_value = False

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.switch_relay(1, False) == False


        #test if method detect error during saving modification
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = ZWaveRelay(self.goodZWaveNetwork.nodes["0001"])

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveRelays.zWaveRelay.ZWaveRelay.switch_off') as mockedSwitchOff:
                    mockedSwitchOff.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = False

                        assert self.zWaveNetwork.switch_relay(1, False) == False


        #test if method detect error during getting module
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = False

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveRelays.zWaveRelay.ZWaveRelay.switch_off') as mockedSwitchOff:
                    mockedSwitchOff.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.switch_relay(1, False) == False


        #test if method detect bad module type selected
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = ZWaveLightController(self.goodZWaveNetwork.nodes["0001"])

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveRelays.zWaveRelay.ZWaveRelay.switch_off') as mockedSwitchOff:
                    mockedSwitchOff.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.save_modification') as mockedSavingModification:
                        mockedSavingModification.return_value = True

                        assert self.zWaveNetwork.switch_relay(1, False) == False


        #test if method detect bad zwave network
        self.zWaveNetwork.network = False
        assert self.zWaveNetwork.switch_relay(1, True) == False


    def test_switch_relay_on(self):
        """
            1.test if method succes
            2.test if method detect bad moduleId parametters
            3.test if method detect error during switching
            4.test if method detect bad zwave network
        """
        
        #test if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.switch_relay') as mockedSwitching:
                mockedSwitching.return_value = True

                assert self.zWaveNetwork.switch_relay_on(1) == True


        #test if method detect bad moduleId parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.switch_relay') as mockedSwitching:
                mockedSwitching.return_value = True

                assert self.zWaveNetwork.switch_relay_on("1") == False


        #test if method detect error during switching
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.switch_relay') as mockedSwitching:
                mockedSwitching.return_value = False

                assert self.zWaveNetwork.switch_relay_on(1) == False


        #test if method detect bad zwave network
        self.zWaveNetwork.network = False
        assert self.zWaveNetwork.switch_relay_on(1) == False


    def test_switch_relay_off(self):
        """
            1.test if method succes
            2.test if method detect bad moduleId parametters
            3.test if method detect error during switching
            4.test if method detect bad zwave network
        """
        
        #test if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.switch_relay') as mockedSwitching:
                mockedSwitching.return_value = True

                assert self.zWaveNetwork.switch_relay_off(1) == True


        #test if method detect bad moduleId parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.switch_relay') as mockedSwitching:
                mockedSwitching.return_value = True

                assert self.zWaveNetwork.switch_relay_off("1") == False


        #test if method detect error during switching
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.switch_relay') as mockedSwitching:
                mockedSwitching.return_value = False

                assert self.zWaveNetwork.switch_relay_off(1) == False


        #test if method detect bad zwave network
        self.zWaveNetwork.network = False
        assert self.zWaveNetwork.switch_relay_off(1) == False


    def test_heal_network(self):
        """
            1.test if method succes
            2.test if method detect error during healing
            3.test if method detect bad zwave network
        """
        
        #test if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('fakeClasses.fakeZwaveNetwork.FakeZwaveNetwork.heal') as mockedHealing:
            mockedHealing.return_value = True

            assert self.zWaveNetwork.heal_network() == True


        #test if method detect error during healing
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('fakeClasses.fakeZwaveNetwork.FakeZwaveNetwork.heal') as mockedHealing:
            mockedHealing.side_effect = Exception()

            assert self.zWaveNetwork.heal_network() == False


        #test if method detect bad zwave network
        self.zWaveNetwork.network = False
        assert self.zWaveNetwork.heal_network() == False


    def test_heal_module(self):
        """
            1.test if method succes
            2.test if method detect bad moduleId parametters
            3.test if method detect error during healing
            4.test if method detect error during getting module
            5.test if method detect bad zwave network
        """
        
        #test if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.heal') as mockedHealing:
                mockedHealing.return_value = True

                assert self.zWaveNetwork.heal_module(1) == True


        #test if method detect bad moduleId parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.heal') as mockedHealing:
                mockedHealing.return_value = True

                assert self.zWaveNetwork.heal_module("1") == False


        #test if method detect error during healing
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.heal') as mockedHealing:
                mockedHealing.return_value = False

                assert self.zWaveNetwork.heal_module(1) == False
            

        #test if method detect error during getting module
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = False

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.heal') as mockedHealing:
                    mockedHealing.return_value = True

                    assert self.zWaveNetwork.heal_module(1) == False


        #test if method detect bad zwave network
        self.zWaveNetwork.network = False
        assert self.zWaveNetwork.heal_module(1) == False


    def test_destroy_network(self):
        """
            1.test if method succes
            2.test if method detect error during destroying
            3.test if method detect bad zwave network
        """
        
        #test if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('fakeClasses.fakeZwaveNetwork.FakeZwaveNetwork.destroy') as mockedDestroying:
            mockedDestroying.return_value = True

            assert self.zWaveNetwork.destroy_network() == True


        #test if method detect error during destroying
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('fakeClasses.fakeZwaveNetwork.FakeZwaveNetwork.destroy') as mockedDestroying:
            mockedDestroying.side_effect = Exception()

            assert self.zWaveNetwork.destroy_network() == False


        #test if method detect bad zwave network
        self.zWaveNetwork.network = False
        assert self.zWaveNetwork.destroy_network() == False


    def test_update_module_return_route(self):
        """
            1.test if method succes
            2.test if method detect bad moduleId parametters
            3.test if method detect error during updating
            4.test if method detect error during getting module
            5.test if method detect bad zwave network
        """
        
        #test if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_return_route') as mockedUpdatingReturnRoute:
                mockedUpdatingReturnRoute.return_value = True

                assert self.zWaveNetwork.update_module_return_route(1) == True

        
        #test if method detect bad moduleId parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_return_route') as mockedUpdatingReturnRoute:
                mockedUpdatingReturnRoute.return_value = True

                assert self.zWaveNetwork.update_module_return_route("1") == False


        #test if method detect error during updating
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_return_route') as mockedUpdatingReturnRoute:
                mockedUpdatingReturnRoute.return_value = False

                assert self.zWaveNetwork.update_module_return_route(1) == False


        #test if method detect error during getting module
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = False

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_return_route') as mockedUpdatingReturnRoute:
                    mockedUpdatingReturnRoute.return_value = True

                    assert self.zWaveNetwork.update_module_return_route(1) == False


        #test if method detect bad zwave network
        self.zWaveNetwork.network = False
        assert self.zWaveNetwork.update_module_return_route(1) == False


    def test_update_module_neighbors(self):
        """
            1.test if method succes
            2.test if method detect bad moduleId parametters
            3.test if method detect error during updating
            4.test if method detect error during getting module
            5.test if method detect bad zwave network
        """
        
        #test if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_neighbors') as mockedUpdatingNeighbors:
                mockedUpdatingNeighbors.return_value = True

                assert self.zWaveNetwork.update_module_neighbors(1) == True

        
        #test if method detect bad moduleId parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_neighbors') as mockedUpdatingNeighbors:
                mockedUpdatingNeighbors.return_value = True

                assert self.zWaveNetwork.update_module_neighbors("1") == False


        #test if method detect error during updating
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_neighbors') as mockedUpdatingNeighbors:
                mockedUpdatingNeighbors.return_value = False

                assert self.zWaveNetwork.update_module_neighbors(1) == False


        #test if method detect error during getting module
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = False

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_neighbors') as mockedUpdatingNeighbors:
                    mockedUpdatingNeighbors.return_value = True

                    assert self.zWaveNetwork.update_module_neighbors(1) == False


        #test if method detect bad zwave network
        self.zWaveNetwork.network = False
        assert self.zWaveNetwork.update_module_neighbors(1) == False


    def test_update_module_network(self):
        """
            1.test if method succes
            2.test if method detect bad moduleId parametters
            3.test if method detect error during updating
            4.test if method detect error during getting module
            5.test if method detect bad zwave network
        """
        
        #test if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_network') as mockedUpdatingNetwork:
                mockedUpdatingNetwork.return_value = True

                assert self.zWaveNetwork.update_module_network(1) == True

        
        #test if method detect bad moduleId parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_network') as mockedUpdatingNetwork:
                mockedUpdatingNetwork.return_value = True

                assert self.zWaveNetwork.update_module_network("1") == False


        #test if method detect error during updating
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_network') as mockedUpdatingNetwork:
                mockedUpdatingNetwork.return_value = False

                assert self.zWaveNetwork.update_module_network(1) == False


        #test if method detect error during getting module
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = False

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_network') as mockedUpdatingNetwork:
                    mockedUpdatingNetwork.return_value = True

                    assert self.zWaveNetwork.update_module_network(1) == False


        #test if method detect bad zwave network
        self.zWaveNetwork.network = False
        assert self.zWaveNetwork.update_module_network(1) == False


    def test_refresh_module_info(self):
        """
            1.test if method succes
            2.test if method detect bad moduleId parametters
            3.test if method detect error during refreshing
            4.test if method detect error during getting module
            5.test if method detect bad zwave network
        """
        
        #test if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.refresh_info') as mockedRefreshingInfo:
                mockedRefreshingInfo.return_value = True

                assert self.zWaveNetwork.refresh_module_info(1) == True

        
        #test if method detect bad moduleId parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.refresh_info') as mockedRefreshingInfo:
                mockedRefreshingInfo.return_value = True

                assert self.zWaveNetwork.refresh_module_info("1") == False


        #test if method detect error during refreshing
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.refresh_info') as mockedRefreshingInfo:
                mockedRefreshingInfo.return_value = False

                assert self.zWaveNetwork.refresh_module_info(1) == False


        #test if method detect error during getting module
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = False

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.refresh_info') as mockedRefreshingInfo:
                    mockedRefreshingInfo.return_value = True

                    assert self.zWaveNetwork.refresh_module_info(1) == False


        #test if method detect bad zwave network
        self.zWaveNetwork.network = False
        assert self.zWaveNetwork.refresh_module_info(1) == False


    def test_refresh_module_value(self):
        """
            1.test if method succes
            2.test if method detect bad moduleId parametters
            3.test if method detect bad valueId parametters
            4.test if method detect error during refreshing
            5.test if method detect error during getting module
            6.test if method detect bad zwave network
        """

        #test if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.refresh_value') as mockedRefreshingValue:
                mockedRefreshingValue.return_value = True

                assert self.zWaveNetwork.refresh_module_value(1, 1) == True

        
        #test if method detect bad moduleId parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.refresh_value') as mockedRefreshingValue:
                mockedRefreshingValue.return_value = True

                assert self.zWaveNetwork.refresh_module_value("1", 1) == False

        
        #test if method detect bad valueeId parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.refresh_value') as mockedRefreshingValue:
                mockedRefreshingValue.return_value = True

                assert self.zWaveNetwork.refresh_module_value(1, "1") == False


        #test if method detect error during refreshing
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.refresh_value') as mockedRefreshingValue:
                mockedRefreshingValue.return_value = False

                assert self.zWaveNetwork.refresh_module_value(1, 1) == False


        #test if method detect error during getting module
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = False

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.refresh_value') as mockedRefreshingValue:
                    mockedRefreshingValue.return_value = True

                    assert self.zWaveNetwork.refresh_module_value(1, 1) == False


        #test if method detect bad zwave network
        self.zWaveNetwork.network = self.goodZWaveNetwork
        assert self.zWaveNetwork.refresh_module_value(1, 1) == False


    def test_refresh_module_values(self):
        """
            1.test if method succes
            2.test if method detect bad moduleId parametters
            3.test if method detect error during refreshing
            4.test if method detect error during getting module
            5.test if method detect bad zwave network
        """
        
        #test if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.refresh_values') as mockedRefreshingValues:
                mockedRefreshingValues.return_value = True

                assert self.zWaveNetwork.refresh_module_values(1) == True

        
        #test if method detect bad moduleId parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.refresh_values') as mockedRefreshingValues:
                mockedRefreshingValues.return_value = True

                assert self.zWaveNetwork.refresh_module_values("1") == False


        #test if method detect error during refreshing
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.refresh_values') as mockedRefreshingValues:
                mockedRefreshingValues.return_value = False

                assert self.zWaveNetwork.refresh_module_values(1) == False


        #test if method detect error during getting module
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.isReady') as mockedIsReady:
            mockedIsReady.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
                mockedGettingModule.return_value = False

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.refresh_values') as mockedRefreshingValues:
                    mockedRefreshingValues.return_value = True

                    assert self.zWaveNetwork.refresh_module_values(1) == False


        #test if method detect bad zwave network
        self.zWaveNetwork.network = False
        assert self.zWaveNetwork.refresh_module_values(1) == False


    def test_soft_reset_network(self):
        """
            1.test if method succes
            2.test if method detect error during resetting
            3.test if method detect bad zwave network
        """
        
        #test if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveNetworkController.ZWaveNetworkController.soft_reset_network') as mockedResetting:
            mockedResetting.return_value = True

            assert self.zWaveNetwork.soft_reset_network() == True


        #test if method detect error during resetting
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveNetworkController.ZWaveNetworkController.soft_reset_network') as mockedResetting:
            mockedResetting.return_value = False

            assert self.zWaveNetwork.soft_reset_network() == False


        #test if method detect bad zwave network
        self.zWaveNetwork.network = False
        assert self.zWaveNetwork.soft_reset_network() == False


    def test_hard_reset_network(self):
        """
            1.test if method succes
            2.test if method detect error during resetting
            3.test if method detect bad zwave network
        """
        
        #test if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveNetworkController.ZWaveNetworkController.hard_reset_network') as mockedResetting:
            mockedResetting.return_value = True

            assert self.zWaveNetwork.hard_reset_network() == True


        #test if method detect error during resetting
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveNetworkController.ZWaveNetworkController.hard_reset_network') as mockedResetting:
            mockedResetting.return_value = False

            assert self.zWaveNetwork.hard_reset_network() == False


        #test if method detect bad zwave network
        self.zWaveNetwork.network = False
        assert self.zWaveNetwork.hard_reset_network() == False


    
    """network interaction"""
    def test_network_started(self):
        """
            test if method succes
        """
        
        #test if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork
        assert self.zWaveNetwork.network_started() == True


    def test_network_ready(self):
        """
            test if method succes
        """

        #test if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork
        assert self.zWaveNetwork.network_ready() == True


    def test_network_awake(self):
        """
            test if method succes
        """

        #test if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork
        assert self.zWaveNetwork.network_awake() == True

    
    def test_network_failed(self):
        """
            1.test if method succes
            2.test if method detect error durring network stopping
        """

        #test if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.stop') as mockedStopping:
            mockedStopping.return_value = True
        
            assert self.zWaveNetwork.network_failed() == True

        #test if method detect error durring network stopping
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.stop') as mockedStopping:
            mockedStopping.return_value = False
        
            assert self.zWaveNetwork.network_failed() == False


    def test_network_stopped(self):
        """
            1.test if method succes
            2.test if method detect error durring network stopping
        """

        #test if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.stop') as mockedStopping:
            mockedStopping.return_value = True
        
            assert self.zWaveNetwork.network_stopped() == True

        #test if method detect error durring network stopping
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.stop') as mockedStopping:
            mockedStopping.return_value = False
        
            assert self.zWaveNetwork.network_stopped() == False


    def test_network_resetted(self):
        """
            1.test if method succes
        """

        #test if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork
        assert self.zWaveNetwork.network_resetted() == True


    def test_driver_ready(self):
        """
            1.test if method succes
        """

        #test if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork
        assert self.zWaveNetwork.driver_ready() == True


    def test_driver_failed(self):
        """
            1.test if method succes
            2.test if method detect error durring network stopping
        """

        #test if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.stop') as mockedStopping:
            mockedStopping.return_value = True
        
            assert self.zWaveNetwork.driver_failed() == True

        #test if method detect error durring network stopping
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.stop') as mockedStopping:
            mockedStopping.return_value = False
        
            assert self.zWaveNetwork.driver_failed() == False


    def test_driver_removed(self):
        """
            1.test if method succes
            2.test if method detect error durring network stopping
        """

        #test if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.stop') as mockedStopping:
            mockedStopping.return_value = True
        
            assert self.zWaveNetwork.driver_removed() == True

        #test if method detect error durring network stopping
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.stop') as mockedStopping:
            mockedStopping.return_value = False
        
            assert self.zWaveNetwork.driver_removed() == False


    def test_driver_resetted(self):
        """
            1.test if method succes
            2.test if method detect error durring network stopping
        """

        #test if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.restart') as mockedRestarting:
            mockedRestarting.return_value = True
        
            assert self.zWaveNetwork.driver_resetted() == True

        #test if method detect error durring network stopping
        self.zWaveNetwork.network = self.goodZWaveNetwork

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.restart') as mockedRestarting:
            mockedRestarting.return_value = False
        
            assert self.zWaveNetwork.driver_resetted() == False


    def test_node_added(self):
        """
            1.test if method succes
            2.check if method detect error durring getting module
            3.check if method detect error during modules updating return route
            4.check if method detect error during modules neighbor update
            5.check if method detect error durring module network update
        """

        #check if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork
        node = FakeNode(1, "bulb", "bulb")

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
            mockedGettingModule.return_value = ZWaveModule(node)

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_return_route') as mockedUpdatingReturnRoute:
                mockedUpdatingReturnRoute.return_value = True

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_neighbors') as mockedNeighborUpdate:
                    mockedNeighborUpdate.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_network') as mockedNetworkUpdate:
                        mockedNetworkUpdate.return_value = True

                        assert self.zWaveNetwork.node_added(node) == True


        #check if method detect error durring getting module
        self.zWaveNetwork.network = self.goodZWaveNetwork
        node = FakeNode(1, "bulb", "bulb")

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
            mockedGettingModule.return_value = False

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_return_route') as mockedUpdatingReturnRoute:
                mockedUpdatingReturnRoute.return_value = True

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_neighbors') as mockedNeighborUpdate:
                    mockedNeighborUpdate.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_network') as mockedNetworkUpdate:
                        mockedNetworkUpdate.return_value = True

                        assert self.zWaveNetwork.node_added(node) == False

        #check if method detect error during modules updating return route
        self.zWaveNetwork.network = self.goodZWaveNetwork
        node = FakeNode(1, "bulb", "bulb")

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
            mockedGettingModule.return_value = ZWaveModule(node)

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_return_route') as mockedUpdatingReturnRoute:
                mockedUpdatingReturnRoute.return_value = False

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_neighbors') as mockedNeighborUpdate:
                    mockedNeighborUpdate.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_network') as mockedNetworkUpdate:
                        mockedNetworkUpdate.return_value = True

                        assert self.zWaveNetwork.node_added(node) == False


        #check if method detect error during modules neighbor update
        self.zWaveNetwork.network = self.goodZWaveNetwork
        node = FakeNode(1, "bulb", "bulb")

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
            mockedGettingModule.return_value = ZWaveModule(node)

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_return_route') as mockedUpdatingReturnRoute:
                mockedUpdatingReturnRoute.return_value = True

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_neighbors') as mockedNeighborUpdate:
                    mockedNeighborUpdate.return_value = False

                    with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_network') as mockedNetworkUpdate:
                        mockedNetworkUpdate.return_value = True

                        assert self.zWaveNetwork.node_added(node) == False


        #check if method detect error durring module network update
        self.zWaveNetwork.network = self.goodZWaveNetwork
        node = FakeNode(1, "bulb", "bulb")

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
            mockedGettingModule.return_value = ZWaveModule(node)

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_return_route') as mockedUpdatingReturnRoute:
                mockedUpdatingReturnRoute.return_value = True

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_neighbors') as mockedNeighborUpdate:
                    mockedNeighborUpdate.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_network') as mockedNetworkUpdate:
                        mockedNetworkUpdate.return_value = False

                        assert self.zWaveNetwork.node_added(node) == False


    def test_node_removed(self):
        """
            1.test if method succes
            2.check if method detect error during modules updating return route
            3.check if method detect error during modules neighbor update
            4.check if method detect error durring module network update
        """

        #check if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork
        node = FakeNode(1, "bulb", "bulb")

        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_return_route') as mockedUpdatingReturnRoute:
            mockedUpdatingReturnRoute.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_neighbors') as mockedNeighborUpdate:
                mockedNeighborUpdate.return_value = True

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_network') as mockedNetworkUpdate:
                    mockedNetworkUpdate.return_value = True

                    assert self.zWaveNetwork.node_removed(node) == True


        #check if method detect error during modules updating return route
        self.zWaveNetwork.network = self.goodZWaveNetwork
        node = FakeNode(1, "bulb", "bulb")

        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_return_route') as mockedUpdatingReturnRoute:
            mockedUpdatingReturnRoute.return_value = False

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_neighbors') as mockedNeighborUpdate:
                mockedNeighborUpdate.return_value = True

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_network') as mockedNetworkUpdate:
                    mockedNetworkUpdate.return_value = True

                    assert self.zWaveNetwork.node_removed(node) == False


        #check if method detect error during modules neighbor update
        self.zWaveNetwork.network = self.goodZWaveNetwork
        node = FakeNode(1, "bulb", "bulb")

        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_return_route') as mockedUpdatingReturnRoute:
            mockedUpdatingReturnRoute.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_neighbors') as mockedNeighborUpdate:
                mockedNeighborUpdate.return_value = False

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_network') as mockedNetworkUpdate:
                    mockedNetworkUpdate.return_value = True

                    assert self.zWaveNetwork.node_removed(node) == False

                
        #check if method detect error durring module network update
        self.zWaveNetwork.network = self.goodZWaveNetwork
        node = FakeNode(1, "bulb", "bulb")

        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_return_route') as mockedUpdatingReturnRoute:
            mockedUpdatingReturnRoute.return_value = True

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_neighbors') as mockedNeighborUpdate:
                mockedNeighborUpdate.return_value = True

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_network') as mockedNetworkUpdate:
                    mockedNetworkUpdate.return_value = False

                    assert self.zWaveNetwork.node_removed(node) == False


    def test_node_ready(self):
        """
            1.test if method succes
            2.check if method detect error durring getting module
            3.check if method detect error during modules updating return route
            4.check if method detect error during modules neighbor update
            5.check if method detect error durring module network update
        """

        #check if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork
        node = FakeNode(1, "bulb", "bulb")

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
            mockedGettingModule.return_value = ZWaveModule(node)

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_return_route') as mockedUpdatingReturnRoute:
                mockedUpdatingReturnRoute.return_value = True

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_neighbors') as mockedNeighborUpdate:
                    mockedNeighborUpdate.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_network') as mockedNetworkUpdate:
                        mockedNetworkUpdate.return_value = True

                        assert self.zWaveNetwork.node_ready(node) == True


        #check if method detect error durring getting module
        self.zWaveNetwork.network = self.goodZWaveNetwork
        node = FakeNode(1, "bulb", "bulb")

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
            mockedGettingModule.return_value = False

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_return_route') as mockedUpdatingReturnRoute:
                mockedUpdatingReturnRoute.return_value = True

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_neighbors') as mockedNeighborUpdate:
                    mockedNeighborUpdate.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_network') as mockedNetworkUpdate:
                        mockedNetworkUpdate.return_value = True

                        assert self.zWaveNetwork.node_ready(node) == False

        #check if method detect error during modules updating return route
        self.zWaveNetwork.network = self.goodZWaveNetwork
        node = FakeNode(1, "bulb", "bulb")

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
            mockedGettingModule.return_value = ZWaveModule(node)

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_return_route') as mockedUpdatingReturnRoute:
                mockedUpdatingReturnRoute.return_value = False

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_neighbors') as mockedNeighborUpdate:
                    mockedNeighborUpdate.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_network') as mockedNetworkUpdate:
                        mockedNetworkUpdate.return_value = True

                        assert self.zWaveNetwork.node_ready(node) == False


        #check if method detect error during modules neighbor update
        self.zWaveNetwork.network = self.goodZWaveNetwork
        node = FakeNode(1, "bulb", "bulb")

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
            mockedGettingModule.return_value = ZWaveModule(node)

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_return_route') as mockedUpdatingReturnRoute:
                mockedUpdatingReturnRoute.return_value = True

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_neighbors') as mockedNeighborUpdate:
                    mockedNeighborUpdate.return_value = False

                    with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_network') as mockedNetworkUpdate:
                        mockedNetworkUpdate.return_value = True

                        assert self.zWaveNetwork.node_ready(node) == False


        #check if method detect error durring module network update
        self.zWaveNetwork.network = self.goodZWaveNetwork
        node = FakeNode(1, "bulb", "bulb")

        with mock.patch('zWaveNetwork.classes.zWaveNetwork.Network.get_module') as mockedGettingModule:
            mockedGettingModule.return_value = ZWaveModule(node)

            with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_return_route') as mockedUpdatingReturnRoute:
                mockedUpdatingReturnRoute.return_value = True

                with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_neighbors') as mockedNeighborUpdate:
                    mockedNeighborUpdate.return_value = True

                    with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_network') as mockedNetworkUpdate:
                        mockedNetworkUpdate.return_value = False

                        assert self.zWaveNetwork.node_ready(node) == False


    def test_value_changed(self):
        pass


    """EVENT"""

    def test_module_moved(self):
        """
            1.test if method succes
            2.test if method detect bad module parametters
            3.test if method detect bad eventDatetime parametters
        """
        
        #check if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork
        module = ZWaveModule(FakeNode(1, "bulb", "bulb"))
        eventDatetime = "0:0:0 0/0/0"

        assert self.zWaveNetwork.module_moved(module, eventDatetime) == True

        #test if method detect bad module parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork
        module = False
        eventDatetime = "0:0:0 0/0/0"

        assert self.zWaveNetwork.module_moved(module, eventDatetime) == False

        #test if method detect bad eventDatetime parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork
        module = ZWaveModule(FakeNode(1, "bulb", "bulb"))
        eventDatetime = False

        assert self.zWaveNetwork.module_moved(module, eventDatetime) == False


    def test_module_renamed(self):
        """
            1.test if method succes
            2.test if method detect bad module parametters
            3.test if method detect bad eventDatetime parametters
        """
        
        #check if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork
        module = ZWaveModule(FakeNode(1, "bulb", "bulb"))
        eventDatetime = "0:0:0 0/0/0"

        assert self.zWaveNetwork.module_renamed(module, eventDatetime) == True

        #test if method detect bad module parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork
        module = False
        eventDatetime = "0:0:0 0/0/0"

        assert self.zWaveNetwork.module_renamed(module, eventDatetime) == False

        #test if method detect bad eventDatetime parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork
        module = ZWaveModule(FakeNode(1, "bulb", "bulb"))
        eventDatetime = False

        assert self.zWaveNetwork.module_renamed(module, eventDatetime) == False


    def test_motion_detection(self):
        """
            1.test if method succes
            2.test if method detect bad module parametters
            3.test if method detect inexistance of motion sensor in sensor list of the sensor
            4.test if method detect bad eventDatetime parametters
        """
        
        #check if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork
        module = ZWaveSensor(FakeNode(1, "motion detector", "motion detector"), {'motion sensor': "test"})
        eventDatetime = "0:0:0 0/0/0"

        assert self.zWaveNetwork.motion_detection(module, eventDatetime) == True

        #test if method detect bad module parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork
        module = False
        eventDatetime = "0:0:0 0/0/0"

        assert self.zWaveNetwork.motion_detection(module, eventDatetime) == False

        #test if method detect inexistance of motion sensor in sensor list of the sensor
        self.zWaveNetwork.network = self.goodZWaveNetwork
        module = ZWaveSensor(FakeNode(1, "motion detector", "motion detector"), {})
        eventDatetime = "0:0:0 0/0/0"

        assert self.zWaveNetwork.motion_detection(module, eventDatetime) == False

        #test if method detect bad eventDatetime parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork
        module = ZWaveSensor(FakeNode(1, "motion detector", "motion detector"), {'motion sensor': "test"})
        eventDatetime = False

        assert self.zWaveNetwork.motion_detection(module, eventDatetime) == False


    def test_acces_opened(self):
        """
            1.test if method succes
            2.test if method detect bad module parametters
            3.test if method detect inexistance of acces control sensor in sensor list of the sensor
            4.test if method detect bad eventDatetime parametters
        """

        #check if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork
        module = ZWaveSensor(FakeNode(1, "door sensor", "door sensor"), {'acces control sensor': "test"})
        eventDatetime = "0:0:0 0/0/0"

        assert self.zWaveNetwork.acces_opened(module, eventDatetime) == True


        #test if method detect bad module parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork
        module = False
        eventDatetime = "0:0:0 0/0/0"

        assert self.zWaveNetwork.acces_opened(module, eventDatetime) == False


        #test if method detect inexistance of acces control sensor in sensor list of the sensor
        self.zWaveNetwork.network = self.goodZWaveNetwork
        module = ZWaveSensor(FakeNode(1, "door sensor", "door sensor"), {})
        eventDatetime = "0:0:0 0/0/0"

        assert self.zWaveNetwork.acces_opened(module, eventDatetime) == False


        #test if method detect bad eventDatetime parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork
        module = ZWaveSensor(FakeNode(1, "door sensor", "door sensor"), {'acces control sensor': "test"})
        eventDatetime = False

        assert self.zWaveNetwork.acces_opened(module, eventDatetime) == False


    def test_acces_closed(self):
        """
            1.test if method succes
            2.test if method detect bad module parametters
            3.test if method detect inexistance of acces control sensor in sensor list of the sensor
            4.test if method detect bad eventDatetime parametters
        """

        #check if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork
        module = ZWaveSensor(FakeNode(1, "door sensor", "door sensor"), {'acces control sensor': "test"})
        eventDatetime = "0:0:0 0/0/0"

        assert self.zWaveNetwork.acces_closed(module, eventDatetime) == True


        #test if method detect bad module parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork
        module = False
        eventDatetime = "0:0:0 0/0/0"

        assert self.zWaveNetwork.acces_closed(module, eventDatetime) == False


        #test if method detect inexistance of acces control sensor in sensor list of the sensor
        self.zWaveNetwork.network = self.goodZWaveNetwork
        module = ZWaveSensor(FakeNode(1, "door sensor", "door sensor"), {})
        eventDatetime = "0:0:0 0/0/0"

        assert self.zWaveNetwork.acces_closed(module, eventDatetime) == False


        #test if method detect bad eventDatetime parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork
        module = ZWaveSensor(FakeNode(1, "door sensor", "door sensor"), {'acces control sensor': "test"})
        eventDatetime = False

        assert self.zWaveNetwork.acces_closed(module, eventDatetime) == False


    def test_light_turning_on(self):
        """
            1.test if method succes
            2.test if method detect bad module parametters
            3.test if method detect bad eventDatetime parametters
        """

        #check if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork
        module = ZWaveLightController(FakeNode(1, "light controller", "light controller"))
        eventDatetime = "0:0:0 0/0/0"

        assert self.zWaveNetwork.light_turning_on(module, eventDatetime) == True


        #test if method detect bad module parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork
        module = False
        eventDatetime = "0:0:0 0/0/0"

        assert self.zWaveNetwork.light_turning_on(module, eventDatetime) == False


        #test if method detect bad eventDatetime parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork
        module = ZWaveLightController(FakeNode(1, "light controller", "light controller"))
        eventDatetime = False

        assert self.zWaveNetwork.light_turning_on(module, eventDatetime) == False


    def test_light_turning_off(self):
        """
            1.test if method succes
            2.test if method detect bad module parametters
            3.test if method detect bad eventDatetime parametters
        """

        #check if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork
        module = ZWaveLightController(FakeNode(1, "light controller", "light controller"))
        eventDatetime = "0:0:0 0/0/0"

        assert self.zWaveNetwork.light_turning_off(module, eventDatetime) == True


        #test if method detect bad module parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork
        module = False
        eventDatetime = "0:0:0 0/0/0"

        assert self.zWaveNetwork.light_turning_off(module, eventDatetime) == False


        #test if method detect bad eventDatetime parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork
        module = ZWaveLightController(FakeNode(1, "light controller", "light controller"))
        eventDatetime = False

        assert self.zWaveNetwork.light_turning_off(module, eventDatetime) == False


    def test_light_color_modified(self):
        """
            1.test if method succes
            2.test if method detect bad module parametters
            3.test if method detect bad eventDatetime parametters
        """

        #check if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork
        module = ZWaveColorLightController(FakeNode(1, "light controller", "light controller"))
        eventDatetime = "0:0:0 0/0/0"

        assert self.zWaveNetwork.light_color_modified(module, eventDatetime) == True


        #test if method detect bad module parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork
        module = False
        eventDatetime = "0:0:0 0/0/0"

        assert self.zWaveNetwork.light_color_modified(module, eventDatetime) == False


        #test if method detect bad eventDatetime parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork
        module = ZWaveColorLightController(FakeNode(1, "light controller", "light controller"))
        eventDatetime = False

        assert self.zWaveNetwork.light_color_modified(module, eventDatetime) == False


    def test_light_intensity_modified(self):
        """
            1.test if method succes
            2.test if method detect bad module parametters
            3.test if method detect bad eventDatetime parametters
        """

        #check if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork
        module = ZWaveColorLightController(FakeNode(1, "light controller", "light controller"))
        eventDatetime = "0:0:0 0/0/0"

        assert self.zWaveNetwork.light_intensity_modified(module, eventDatetime) == True


        #test if method detect bad module parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork
        module = False
        eventDatetime = "0:0:0 0/0/0"

        assert self.zWaveNetwork.light_intensity_modified(module, eventDatetime) == False


        #test if method detect bad eventDatetime parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork
        module = ZWaveColorLightController(FakeNode(1, "light controller", "light controller"))
        eventDatetime = False

        assert self.zWaveNetwork.light_intensity_modified(module, eventDatetime) == False


    def test_relay_setting_on(self):
        """
            1.test if method succes
            2.test if method detect bad module parametters
            3.test if method detect bad eventDatetime parametters
        """

        #check if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork
        module = ZWaveRelay(FakeNode(1, "relay", "relay"))
        eventDatetime = "0:0:0 0/0/0"

        assert self.zWaveNetwork.relay_setting_on(module, eventDatetime) == True


        #test if method detect bad module parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork
        module = False
        eventDatetime = "0:0:0 0/0/0"

        assert self.zWaveNetwork.relay_setting_on(module, eventDatetime) == False


        #test if method detect bad eventDatetime parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork
        module = ZWaveRelay(FakeNode(1, "relay", "relay"))
        eventDatetime = False

        assert self.zWaveNetwork.relay_setting_on(module, eventDatetime) == False


    def test_relay_setting_off(self):
        """
            1.test if method succes
            2.test if method detect bad module parametters
            3.test if method detect bad eventDatetime parametters
        """

        #check if method succes
        self.zWaveNetwork.network = self.goodZWaveNetwork
        module = ZWaveRelay(FakeNode(1, "relay", "relay"))
        eventDatetime = "0:0:0 0/0/0"

        assert self.zWaveNetwork.relay_setting_off(module, eventDatetime) == True


        #test if method detect bad module parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork
        module = False
        eventDatetime = "0:0:0 0/0/0"

        assert self.zWaveNetwork.relay_setting_off(module, eventDatetime) == False


        #test if method detect bad eventDatetime parametters
        self.zWaveNetwork.network = self.goodZWaveNetwork
        module = ZWaveRelay(FakeNode(1, "relay", "relay"))
        eventDatetime = False

        assert self.zWaveNetwork.relay_setting_off(module, eventDatetime) == False
