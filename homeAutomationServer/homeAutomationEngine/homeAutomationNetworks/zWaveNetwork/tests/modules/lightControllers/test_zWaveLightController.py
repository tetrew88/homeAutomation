import os
import unittest
import sys
import mock

from unittest.mock import patch, mock_open, MagicMock

sys.path.append("..")

from fakeClasses.fakeNode import *
from fakeClasses.fakeValue import *

from zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveLightController import *


class Test_ZWaveLightController:
    """
        testing class of an zwave light controller
    """  

    goodLightController = ZWaveLightController(FakeNode(1, "module", "module"))
    badLightController = ZWaveLightController(False)


    def test_level_property(self):
        """
            1.test if method succes
            2.test if method return good type of data
            3.test if method detect level value not found
            4.test if method detect error
        """

        self.goodLightController.moduleNode.values = {'1': FakeZWaveValue(1, 'level')}
        self.goodLightController.moduleNode.values['1'].data = 100

        #test if method succes
        assert self.goodLightController.level == 100

        #test if method return good type of data
        assert isinstance(self.goodLightController.level, int) == True

        #test if method detect level value not found
        self.goodLightController.moduleNode.values = {}
        assert self.goodLightController.level == False

        #test if method detect error
        assert self.badLightController.level == False


    def test_lightUp_property(self):
        """
            1.test if method succes
            2.test if method return good type of data
            4.test if method detect error
        """

        self.goodLightController.moduleNode.values = {'1': FakeZWaveValue(1, 'level')}
        self.goodLightController.moduleNode.values['1'].data = 100

        #test if method succes
        assert self.goodLightController.lightUp == True

        self.goodLightController.moduleNode.values['1'].data = 0
        assert self.goodLightController.lightUp == False

        #test if method return good type of data
        assert isinstance(self.goodLightController.lightUp, bool) == True

        #test if method detect error
        assert self.badLightController.lightUp == False
        
        
    def test_maxLevel_property(self):
        """
            1.test if method succes
            2.test if method return good type of data
            3.test if method detect maxlevel value not found
            4.test if method detect error
        """

        self.goodLightController.moduleNode.values = {'1': FakeZWaveValue(1, 'level')}
        self.goodLightController.moduleNode.values['1'].max = 100

        #test if method succes
        assert self.goodLightController.maxLevel == 100

        #test if method return good type of data
        assert isinstance(self.goodLightController.maxLevel, int) == True

        #test if method detect maxlevel value not found
        self.goodLightController.moduleNode.values = {}
        assert self.goodLightController.maxLevel == False

        #test if method detect error
        assert self.badLightController.maxLevel == False


    def test_minLevel_property(self):
        """
            1.test if method succes
            2.test if method return good type of data
            3.test if method detect minlevel value not found
            4.test if method detect error
        """

        self.goodLightController.moduleNode.values = {'1': FakeZWaveValue(1, 'level')}
        self.goodLightController.moduleNode.values['1'].min = 100

        #test if method succes
        assert self.goodLightController.minLevel == 100

        #test if method return good type of data
        assert isinstance(self.goodLightController.minLevel, int) == True

        #test if method detect maxlevel value not found
        self.goodLightController.moduleNode.values = {}
        assert self.goodLightController.minLevel == False

        #test if method detect error
        assert self.badLightController.minLevel == False


    def test_startLevel_property(self):
        """
            1.test if method succes
            2.test if method return good type of data
            3.test if method detect minlevel value not found
            4.test if method detect error
        """

        self.goodLightController.moduleNode.values = {'1': FakeZWaveValue(1, 'start level')}
        self.goodLightController.moduleNode.values['1'].data = 100

        #test if method succes
        assert self.goodLightController.startLevel == 100

        #test if method return good type of data
        assert isinstance(self.goodLightController.startLevel, int) == True

        #test if method detect maxlevel value not found
        self.goodLightController.moduleNode.values = {}
        assert self.goodLightController.startLevel == False

        #test if method detect error
        assert self.badLightController.startLevel == False


    def test_switch_on(self):
        """
            1.test if method succes
            2.test if method return good type of data
            4.test if method detect error during setting level
        """
        
        self.goodLightController.moduleNode.values = {'1': FakeZWaveValue(1, 'level')}
        self.goodLightController.moduleNode.values['1'].max = 100

        #test if method succes
        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveLightController.ZWaveLightController.set_level') as mockedSettingLevel:
            mockedSettingLevel.return_value = True

            assert self.goodLightController.switch_on() == True

        #test if method return good type of data
        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveLightController.ZWaveLightController.set_level') as mockedSettingLevel:
            mockedSettingLevel.return_value = True

            assert isinstance(self.goodLightController.switch_on(), bool) == True

        #test if method detect error during setting level
        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveLightController.ZWaveLightController.set_level') as mockedSettingLevel:
            mockedSettingLevel.return_value = False

            assert self.goodLightController.switch_on() == False


    def test_switch_off(self):
        """
            1.test if method succes
            2.test if method return good type of data
            4.test if method detect error during setting level
        """
        
        self.goodLightController.moduleNode.values = {'1': FakeZWaveValue(1, 'level')}
        self.goodLightController.moduleNode.values['1'].min = 0

        #test if method succes
        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveLightController.ZWaveLightController.set_level') as mockedSettingLevel:
            mockedSettingLevel.return_value = True

            assert self.goodLightController.switch_off() == True

        #test if method return good type of data
        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveLightController.ZWaveLightController.set_level') as mockedSettingLevel:
            mockedSettingLevel.return_value = True

            assert isinstance(self.goodLightController.switch_off(), bool) == True

        #test if method detect error during setting level
        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveLightController.ZWaveLightController.set_level') as mockedSettingLevel:
            mockedSettingLevel.return_value = False

            assert self.goodLightController.switch_off() == False


    def test_set_level(self):
        """
            1.test if method succes
            2.test if method return good type of data
            3.test if method detect bad parametters
            4.test if method detect level value not found
            5.test if method detect error during setting level
            6.test if method detect error
        """

        self.goodLightController.moduleNode.values = {'1': FakeZWaveValue(1, 'level')}
        self.goodLightController.moduleNode.values['1'].data = 100

        with mock.patch('zWaveNetwork.classes.zWaveValues.zWaveValue.ZWaveValue.set_data') as mockedSettingData:
            mockedSettingData.return_value = True

            #test if method succes
            assert self.goodLightController.set_level(20) == True

            #test if method return good type of data
            assert isinstance(self.goodLightController.set_level(20), bool) == True

            #test if method detect bad parametters
            assert self.goodLightController.set_level("20") == False

        #test if method detect level value not found
        self.goodLightController.moduleNode.values = {}

        with mock.patch('zWaveNetwork.classes.zWaveValues.zWaveValue.ZWaveValue.set_data') as mockedSettingData:
            mockedSettingData.return_value = True

            assert self.goodLightController.set_level(20) == False

        #test if method detect error during setting level
        self.goodLightController.moduleNode.values = {'1': FakeZWaveValue(1, 'level')}
        self.goodLightController.moduleNode.values['1'].data = 100

        with mock.patch('zWaveNetwork.classes.zWaveValues.zWaveValue.ZWaveValue.set_data') as mockedSettingData:
            mockedSettingData.return_value = False

            assert self.goodLightController.set_level(20) == False

        #test if method detect error
        assert self.badLightController.set_level(20) == False