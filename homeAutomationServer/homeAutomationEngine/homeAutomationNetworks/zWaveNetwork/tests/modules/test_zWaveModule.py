import os
import unittest
import sys
import mock

from unittest.mock import patch, mock_open, MagicMock

sys.path.append("..")

from fakeClasses.fakeNode import *
from fakeClasses.fakeValue import *

from zWaveNetwork.classes.zWaveModules.zWaveModule import *

class Test_ZWaveModule:
    """
        testing class of an zwave module
    """  

    goodModule = ZWaveModule(FakeNode(1, "module", "module"))
    badModule = ZWaveModule(False)

    def test_id_property(self):
        """
            1.test if method return good data
            2.test if method return good type of data
            3.test if method detect error
        """

        self.goodModule.moduleNode.id = 1
        
        assert self.goodModule.id == 1
        assert isinstance(self.goodModule.id, int) == True
        assert self.badModule.id == False


    def test_name_property(self):
        """
            1.test if method return good data
            2.test if method return good type of data
            3.test if method detect error
        """

        self.goodModule.moduleNode.name = "test"

        assert self.goodModule.name == "test"
        assert isinstance(self.goodModule.name, str) == True
        assert self.badModule.name == False


    def test_location_property(self):
        """
            1.test if method return good data
            2.test if method return good type of data
            3.test if method detect error
        """

        self.goodModule.moduleNode.location = 1

        assert self.goodModule.location == 1
        assert isinstance(self.goodModule.location, int) == True
        assert self.badModule.location == False


    def test_manufacturerName_property(self):
        """
            1.test if method return good data
            2.test if method return good type of data
            3.test if method detect error
        """

        self.goodModule.moduleNode.manufacturer_name = "test"

        assert self.goodModule.manufacturerName == "test"
        assert isinstance(self.goodModule.manufacturerName, str) == True
        assert self.badModule.manufacturerName == False


    def test_productName_property(self):
        """
            1.test if method return good data
            2.test if method return good type of data
            3.test if method detect error
        """

        self.goodModule.moduleNode.product_name = "test"

        assert self.goodModule.productName == "test"
        assert isinstance(self.goodModule.productName, str) == True
        assert self.badModule.productName == False


    def test_productType_property(self):
        """
            1.test if method return good data
            2.test if method return good type of data
            3.test if method detect error
        """

        self.goodModule.moduleNode.product_type = "test"

        assert self.goodModule.productType == "test"
        assert isinstance(self.goodModule.productType, str) == True
        assert self.badModule.productType == False


    def test_deviceType_property(self):
        """
            1.test if method return good data
            2.test if method return good type of data
            3.test if method detect error
        """

        self.goodModule.moduleNode.device_type = "test"

        assert self.goodModule.deviceType == "test"
        assert isinstance(self.goodModule.deviceType, str) == True
        assert self.badModule.deviceType == False


    def test_type_property(self):
        """
            1.test if method return good data
            2.test if method return good type of data
            3.test if method detect error
        """

        self.goodModule.moduleNode.type = "test"

        assert self.goodModule.type == "test"
        assert isinstance(self.goodModule.type, str) == True
        assert self.badModule.type == False


    def test_values_property(self):
        """
            1.test if method return good type of data
            2.check list content conformity
            3.test if method detect error
        """

        #test if method return good type of data
        self.goodModule.moduleNode.values = {'1': FakeZWaveValue(1, 'test1'), '2': FakeZWaveValue(1, 'test2')}
        assert isinstance(self.goodModule.values, list) == True
        assert len(self.goodModule.values) == 2

        #check list content conformity
        self.goodModule.moduleNode.values = {'1': FakeZWaveValue(1, 'test1'), '2': FakeZWaveValue(1, 'test2')}
        for values in self.goodModule.values:
            assert isinstance(values, ZWaveValue) == True

        #test if method detect error
        self.goodModule.moduleNode.values = False
        assert self.goodModule.values == []
        assert len(self.goodModule.values) == 0

        assert self.badModule.values == []


    def test_parametters_property(self):
        """
            1.test if method return good type of data
            2.check list content conformity
            3.test if method detect error
        """

        #test if method return good type of data
        self.goodModule.moduleNode.values = {'1': FakeZWaveValue(1, 'test1'), '2': FakeZWaveValue(1, 'test2')}
        self.goodModule.moduleNode.values['1'].is_read_only = False
        self.goodModule.moduleNode.values['2'].is_read_only = True

        assert isinstance(self.goodModule.parametters, list) == True
        assert len(self.goodModule.parametters) == 1

        #check list content conformity
        for parametter in self.goodModule.parametters:
            assert isinstance(parametter, ZWaveParametter) == True

        #test if method detect error
        self.goodModule.moduleNode.values = False
        assert self.goodModule.parametters == []
        assert len(self.goodModule.parametters) == 0

        assert self.badModule.parametters == []


    def test_canWakeUp_property(self):
        """
            1.test if method return good type of data
            2.test if method detect error
        """

        #test if method return good type of data
        self.goodModule.moduleNode.canWakeUp = True

        assert self.goodModule.canWakeUp == True
        assert isinstance(self.goodModule.canWakeUp, bool)

        #test if method detect error
        assert self.badModule.canWakeUp == False


    def test_isAwake_property(self):
        """
            1.test if method return good type of data
            2.test if method detect error
        """

        #test if method return good type of data
        self.goodModule.moduleNode.is_awake = True

        assert self.goodModule.isAwake == True
        assert isinstance(self.goodModule.isAwake, bool)

        #test if method detect error
        assert self.badModule.isAwake == False


    def test_isFailed_property(self):
        """
            1.test if method return good type of data
            2.test if method detect error
        """

        #test if method return good type of data
        self.goodModule.moduleNode.is_failed = False

        assert self.goodModule.isFailed == False
        assert isinstance(self.goodModule.isFailed, bool)

        #test if method detect error
        assert self.badModule.isFailed == True


    def test_isReady_property(self):
        """
            1.test if method return good type of data
            2.test if method detect error
        """

        #test if method return good type of data
        self.goodModule.moduleNode.is_ready = True

        assert self.goodModule.isReady == True
        assert isinstance(self.goodModule.isReady, bool)

        #test if method detect error
        assert self.badModule.isReady == False


    def test_isSleeping_property(self):
        """
            1.test if method return good type of data
            2.test if method detect error
        """

        #test if method return good type of data
        self.goodModule.moduleNode.is_sleeping = True

        assert self.goodModule.isSleeping == True
        assert isinstance(self.goodModule.isSleeping, bool)

        #test if method detect error
        assert self.badModule.isSleeping == False


    def test_batteryLevel_property(self):
        """
            1.test if method return good type of data
            2.test if method detect error durring getting battery level
            3.test if method detect error
        """

        #test if method return good type of data
        self.goodModule.moduleNode.batteryLevel = 100

        assert self.goodModule.batteryLevel == 100
        assert isinstance(self.goodModule.batteryLevel, int)

        #test if method detect error durring getting battery level
        self.goodModule.moduleNode.batteryLevel = 'none'
        assert self.goodModule.batteryLevel == False

        #test if method detect error
        assert self.badModule.batteryLevel == False


    def test_commandClassAsString_property(self):
        """
            1.test if method return good type of data
            2.test if method detect error durring getting command class
            3.test if method detect error
        """

        #test if method return good type of data
        self.goodModule.moduleNode.command_classes_as_string = ['relay', 'test']

        assert self.goodModule.commandClassAsString == ['relay', 'test']
        assert isinstance(self.goodModule.commandClassAsString, list)
        for commandClass in self.goodModule.commandClassAsString:
            assert isinstance(commandClass, str)

        #test if method detect error durring getting battery level
        self.goodModule.moduleNode.command_classes_as_string = False
        assert self.goodModule.commandClassAsString == False

        #test if method detect error
        assert self.badModule.commandClassAsString == False



    def test_getting_value(self):
        """
            1.test if method succes
            2.test if method return good type of data
            3.test if method detect bad parrametters
            4.test if method detect inexistant value
            5.test if method detect error
        """

        #test if method succes
        self.goodModule.moduleNode.values = {'1': FakeZWaveValue(1, 'test1'), '2': FakeZWaveValue(2, 'test2')}
        assert self.goodModule.get_value(1).id == 1

        #test if method return good type of data
        self.goodModule.moduleNode.values = {'1': FakeZWaveValue(1, 'test1'), '2': FakeZWaveValue(2, 'test2')}
        assert isinstance(self.goodModule.get_value(1), ZWaveValue) == True

        #test if method detect bad parrametters
        self.goodModule.moduleNode.values = {'1': FakeZWaveValue(1, 'test1'), '2': FakeZWaveValue(2, 'test2')}
        assert self.goodModule.get_value("1") == False

        #test if method detect inexistant value
        self.goodModule.moduleNode.values = {'1': FakeZWaveValue(1, 'test1'), '2': FakeZWaveValue(2, 'test2')}
        assert self.goodModule.get_value(3) == False

        #test if method detect error
        assert self.badModule.get_value(1) == False


    def test_setting_name(self):
        """
            1.test if method succes
            2.test if method return good type of data
            3.test if method detect bad parrametters
            4.test if method detect error during updating network
            5.test if method detect error
        """

        #test if method succes
        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_network') as mockedUpdatingNetwork:
            mockedUpdatingNetwork.return_value = True

            self.goodModule.moduleNode.name == "test"
            self.goodModule.set_name("testRename")
            assert self.goodModule.name == "testRename"

        #test if method return good type of data
        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_network') as mockedUpdatingNetwork:
            mockedUpdatingNetwork.return_value = True
            assert self.goodModule.set_name("testRename") == True

        #test if method detect bad parrametters
        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_network') as mockedUpdatingNetwork:
            mockedUpdatingNetwork.return_value = True
            assert self.goodModule.set_name(1) == False

        #test if method detect error during updating network
        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_network') as mockedUpdatingNetwork:
            mockedUpdatingNetwork.return_value = False
            assert self.goodModule.set_name("testRename") == False

        #test if method detect error
        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_network') as mockedUpdatingNetwork:
            mockedUpdatingNetwork.return_value = True
            assert self.badModule.set_name("testRename") == False


    def test_setting_location(self):
        """
            1.test if method succes
            2.test if method return good type of data
            3.test if method detect bad parrametters
            4.test if method detect error during updating network
            5.test if method detect error
        """

        #test if method succes
        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_network') as mockedUpdatingNetwork:
            mockedUpdatingNetwork.return_value = True

            self.goodModule.moduleNode.location = 1
            self.goodModule.set_location(6)
            assert self.goodModule.location == 6

        #test if method return good type of data
        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_network') as mockedUpdatingNetwork:
            mockedUpdatingNetwork.return_value = True
            assert self.goodModule.set_location(6) == True

        #test if method detect bad parrametters
        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_network') as mockedUpdatingNetwork:
            mockedUpdatingNetwork.return_value = True
            assert self.goodModule.set_location("6") == False

        #test if method detect error during updating network
        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_network') as mockedUpdatingNetwork:
            mockedUpdatingNetwork.return_value = False
            assert self.goodModule.set_location(6) == False

        #test if method detect error
        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_network') as mockedUpdatingNetwork:
            mockedUpdatingNetwork.return_value = True
            assert self.badModule.set_location(1) == False


    def test_setting_value_data(self):
        """
            1.test if method succes
            2.test if method return good type of data
            3.test if method detect bad module id
            4.test if method detect bad data type
            5.test if method detect value not found
            6.test if method detect error
        """

        #test if method succes
        self.goodModule.moduleNode.values = {'1': FakeZWaveValue(1, 'test1'), '2': FakeZWaveValue(2, 'test2')}
        self.goodModule.moduleNode.values['1'].type = 'string'
        self.goodModule.moduleNode.values['1'].data = "test"

        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_network') as mockedUpdatingNetwork:
            mockedUpdatingNetwork.return_value = True
            
            assert self.goodModule.set_value_data(1, "testModification") == True
            assert self.goodModule.get_value(1).data == "testModification"

        #test if method return good type of data
        self.goodModule.moduleNode.values = {'1': FakeZWaveValue(1, 'test1'), '2': FakeZWaveValue(2, 'test2')}
        self.goodModule.moduleNode.values['1'].type = 'string'
        self.goodModule.moduleNode.values['1'].data = "test"

        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_network') as mockedUpdatingNetwork:
            mockedUpdatingNetwork.return_value = True
            
            assert isinstance(self.goodModule.set_value_data(1, "testModification"), bool) == True

        #test if method detect bad module id
        self.goodModule.moduleNode.values = {'1': FakeZWaveValue(1, 'test1'), '2': FakeZWaveValue(2, 'test2')}
        self.goodModule.moduleNode.values['1'].type = 'string'
        self.goodModule.moduleNode.values['1'].data = "test"

        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_network') as mockedUpdatingNetwork:
            mockedUpdatingNetwork.return_value = True
            
            assert self.goodModule.set_value_data("1", "testModification") == False

        #test if method detect bad data type
        self.goodModule.moduleNode.values = {'1': FakeZWaveValue(1, 'test1'), '2': FakeZWaveValue(2, 'test2')}
        self.goodModule.moduleNode.values['1'].type = 'string'
        self.goodModule.moduleNode.values['1'].data = "test"

        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_network') as mockedUpdatingNetwork:
            mockedUpdatingNetwork.return_value = True
            
            assert self.goodModule.set_value_data(1, 100) == False

        #test if method detect value not found
        self.goodModule.moduleNode.values = {'1': FakeZWaveValue(1, 'test1'), '2': FakeZWaveValue(2, 'test2')}
        self.goodModule.moduleNode.values['1'].type = 'string'
        self.goodModule.moduleNode.values['1'].data = "test"

        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.update_network') as mockedUpdatingNetwork:
            mockedUpdatingNetwork.return_value = True
            
            assert self.goodModule.set_value_data(100, "testModification") == False

        #test if method detect error
        assert self.badModule.set_value_data(1, "testModification") == False


    def test_updating_return_route(self):
        """
            1.test if method succes
            2.test if method return good type of data
            3.test if method detect error during Assignating Return Route
            4.test if method detect error
        """

        with mock.patch('fakeClasses.fakeNode.FakeNode.assign_return_route') as mockedAssignatingReturnRoute:
            mockedAssignatingReturnRoute = True

            #test if method succes
            assert self.goodModule.update_return_route() == True

            #test if method return good type of data
            assert isinstance(self.goodModule.update_return_route(), bool) == True

        #test if method detect error during Assignating Return Route
        with mock.patch('fakeClasses.fakeNode.FakeNode.assign_return_route') as mockedAssignatingReturnRoute:
            mockedAssignatingReturnRoute.side_effect = Exception()

            #test if method succes
            assert self.goodModule.update_return_route() == False

        #test if method detect error
        with mock.patch('fakeClasses.fakeNode.FakeNode.assign_return_route') as mockedAssignatingReturnRoute:
            mockedAssignatingReturnRoute = True

            #test if method succes
            assert self.badModule.update_return_route() == False


    def test_updating_neighbors(self):
        """
            1.test if method succes
            2.test if method return good type of data
            3.test if method detect error during updating neighbor
            4.test if method detect error
        """

        with mock.patch('fakeClasses.fakeNode.FakeNode.neighbor_update') as mockedNeighborUpdate:
            mockedNeighborUpdate = True

            #test if method succes
            assert self.goodModule.update_neighbors() == True

            #test if method return good type of data
            assert isinstance(self.goodModule.update_neighbors(), bool) == True

        #test if method detect error during updating neighbor
        with mock.patch('fakeClasses.fakeNode.FakeNode.neighbor_update') as mockedNeighborUpdate:
            mockedNeighborUpdate.side_effect = Exception()

            #test if method succes
            assert self.goodModule.update_neighbors() == False

        #test if method detect error
        with mock.patch('fakeClasses.fakeNode.FakeNode.neighbor_update') as mockedNeighborUpdate:
            mockedNeighborUpdate = True

            #test if method succes
            assert self.badModule.update_neighbors() == False


    def test_update_network(self):
        """
            1.test if method succes
            2.test if method return good type of data
            3.test if method detect error during updating network
            4.test if method detect error
        """
        
        with mock.patch('fakeClasses.fakeNode.FakeNode.network_update') as mockedNetworkUpdate:
            mockedNetworkUpdate = True

            #test if method succes
            assert self.goodModule.update_network() == True

            #test if method return good type of data
            assert isinstance(self.goodModule.update_network(), bool) == True

        #test if method detect error during updating network
        with mock.patch('fakeClasses.fakeNode.FakeNode.network_update') as mockedNetworkUpdate:
            mockedNetworkUpdate.side_effect = Exception()

            #test if method succes
            assert self.goodModule.update_network() == False

        #test if method detect error
        with mock.patch('fakeClasses.fakeNode.FakeNode.network_update') as mockedNetworkUpdate:
            mockedNetworkUpdate = True

            #test if method succes
            assert self.badModule.update_network() == False


    def test_refreshing_info(self):
        """
            1.test if method succes
            2.test if method return good type of data
            3.test if method detect error during refreshing info
            4.test if method detect error
        """
        
        with mock.patch('fakeClasses.fakeNode.FakeNode.refresh_info') as mockedRefreshingInformation:
            mockedRefreshingInformation = True

            #test if method succes
            assert self.goodModule.refresh_info() == True

            #test if method return good type of data
            assert isinstance(self.goodModule.refresh_info(), bool) == True

        #test if method detect error during refreshing info
        with mock.patch('fakeClasses.fakeNode.FakeNode.refresh_info') as mockedRefreshingInformation:
            mockedRefreshingInformation.side_effect = Exception()

            #test if method succes
            assert self.goodModule.refresh_info() == False

        #test if method detect error
        with mock.patch('fakeClasses.fakeNode.FakeNode.refresh_info') as mockedRefreshingInformation:
            mockedRefreshingInformation = True

            #test if method succes
            assert self.badModule.refresh_info() == False


    def test_refreshing_value(self):
        """
            1.test if method succes
            2.test if method return good type of data
            3.test if method detect error during refreshing value
            4.test if method detect bad parametters
            5.test if method detect error
        """

        #test if method succes
        self.goodModule.moduleNode.values = {'1': FakeZWaveValue(1, 'test1'), '2': FakeZWaveValue(2, 'test2')}
        
        with mock.patch('fakeClasses.fakeNode.FakeNode.refresh_value') as mockedRefreshingValue:
            mockedRefreshingValue = True

            assert self.goodModule.refresh_value(1) == True

            #test if method return good type of data
            assert isinstance(self.goodModule.refresh_value(1), bool) == True

        #test if method detect error during refreshing value
        self.goodModule.moduleNode.values = {'1': FakeZWaveValue(1, 'test1'), '2': FakeZWaveValue(2, 'test2')}
        
        with mock.patch('fakeClasses.fakeNode.FakeNode.refresh_value') as mockedRefreshingValue:
            mockedRefreshingValue.side_effect = Exception()

            assert self.goodModule.refresh_value(1) == False

        #test if method detect bad parametters
        self.goodModule.moduleNode.values = {'1': FakeZWaveValue(1, 'test1'), '2': FakeZWaveValue(2, 'test2')}
        
        with mock.patch('fakeClasses.fakeNode.FakeNode.refresh_value') as mockedRefreshingValue:
            mockedRefreshingValue = True

            assert self.goodModule.refresh_value("1") == False

        #test if method detect error
        self.goodModule.moduleNode.values = {'1': FakeZWaveValue(1, 'test1'), '2': FakeZWaveValue(2, 'test2')}
        
        with mock.patch('fakeClasses.fakeNode.FakeNode.refresh_value') as mockedRefreshingValue:
            mockedRefreshingValue = True

            assert self.badModule.refresh_value(1) == False


    def test_refresh_values(self):
        """
            1.test if method succes
            2.test if method return good type of data
            3.test if method detect error during refreshing value
            4.test if method detect error
        """

        self.goodModule.moduleNode.values = {'1': FakeZWaveValue(1, 'test1'), '2': FakeZWaveValue(2, 'test2')}
        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.refresh_value') as mockedRefreshingValue:
            mockedRefreshingValue = True

            #test if method succes
            assert self.goodModule.refresh_values() == True

            #test if method return good type of data
            assert isinstance(self.goodModule.refresh_values(), bool) == True

        #test if method detect error during refreshing value
        self.goodModule.moduleNode.values = {'1': FakeZWaveValue(1, 'test1'), '2': FakeZWaveValue(2, 'test2')}
        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.refresh_value') as mockedRefreshingValue:
            mockedRefreshingValue.return_value = False

            assert self.goodModule.refresh_values() == False

        #test if method detect error
        self.goodModule.moduleNode.values = {'1': FakeZWaveValue(1, 'test1'), '2': FakeZWaveValue(2, 'test2')}
        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.refresh_value') as mockedRefreshingValue:
            mockedRefreshingValue = True

            assert self.badModule.refresh_values() == False


    def test_heal(self):
        """
            1.test if method succes
            2.test if method return good type of data
            3.test if method detect error during healing
            4.test if method detect error
        """
        
        with mock.patch('fakeClasses.fakeNode.FakeNode.heal') as mockedHealing:
            mockedHealing = True

            #test if method succes
            assert self.goodModule.heal() == True

            #test if method return good type of data
            assert isinstance(self.goodModule.heal(), bool) == True

        #test if method detect error during healing
        with mock.patch('fakeClasses.fakeNode.FakeNode.heal') as mockedHealing:
            mockedHealing.side_effect = Exception()

            #test if method succes
            assert self.goodModule.heal() == False

        #test if method detect error
        with mock.patch('fakeClasses.fakeNode.FakeNode.heal') as mockedHealing:
            mockedHealing.side_effect = Exception()

            #test if method succes
            assert self.badModule.heal() == False