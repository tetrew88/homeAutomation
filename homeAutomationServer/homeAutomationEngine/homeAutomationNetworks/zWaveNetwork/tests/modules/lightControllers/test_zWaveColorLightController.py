import os
import unittest
import sys
import mock

from unittest.mock import patch, mock_open, MagicMock

sys.path.append("..")

from fakeClasses.fakeNode import *
from fakeClasses.fakeValue import *

from zWaveNetwork.classes.zWaveModules.zWaveLightControllers.zWaveColorLightController import *

from zWaveNetwork.classes.zWaveModules.zWaveModule import *


class Test_ZWaveLightController:
    """
        testing class of an zwave color light controller
    """  

    goodColorLightController = ZWaveColorLightController(FakeNode(1, "module", "module"))
    badColorLightController = ZWaveColorLightController(False)

    def test_colorLabel_property(self):
        """
            1.test if method succes
            2.test if method return good type of data
            3.test if method detect color label value not found
            4.test if method detect error
        """

        self.goodColorLightController.moduleNode.values = {'1': FakeZWaveValue(1, 'color index')}
        self.goodColorLightController.moduleNode.values['1'].data = "red"

        #test if method succes
        assert self.goodColorLightController.colorLabel == "red"

        #test if method return good type of data
        assert isinstance(self.goodColorLightController.colorLabel, str) == True

        #test if method detect color label value not found
        self.goodColorLightController.moduleNode.values = {}

        assert self.goodColorLightController.colorLabel == False

        #test if method detect error
        assert self.badColorLightController.colorLabel == False


    def test_colorValue_property(self):
        """
            1.test if method succes
            2.test if method return good type of data
            3.test if method detect color label value not found
            4.test if method detect error
        """

        self.goodColorLightController.moduleNode.values = {'1': FakeZWaveValue(1, 'color')}
        self.goodColorLightController.moduleNode.values['1'].data = "#0000"

        #test if method succes
        assert self.goodColorLightController.colorValue == "#0000"

        #test if method return good type of data
        assert isinstance(self.goodColorLightController.colorValue, str) == True

        #test if method detect color label value not found
        self.goodColorLightController.moduleNode.values = {}

        assert self.goodColorLightController.colorValue == False

        #test if method detect error
        assert self.badColorLightController.colorValue == False


    def test_colorPalette_property(self):
        """
            1.test if method succes
            2.test if method return good type of data
            3.test if method detect color label value not found
            4.test if method detect error
        """

        self.goodColorLightController.moduleNode.values = {'1': FakeZWaveValue(1, 'color index')}
        self.goodColorLightController.moduleNode.values['1'].data_items = set(["red", "blue", "green"])

        #test if method succes
        #test if method return good type of data
        assert isinstance(self.goodColorLightController.colorPalette, list) == True

        #test if method detect color label value not found
        self.goodColorLightController.moduleNode.values = {}

        assert self.goodColorLightController.colorPalette == False

        #test if method detect error
        assert self.badColorLightController.colorPalette == False


    def test_setting_color_by_label(self):
        """
            1.test if method succes
            2.test if method return good type of data
            3.test if method detect bad parametter
            4.test if method detect color label value not found
            5.test if method detect setting value data error
            6.test if method detect error
        """

        self.goodColorLightController.moduleNode.values = {'1': FakeZWaveValue(1, 'color index')}
        self.goodColorLightController.moduleNode.values['1'].data = "red"

        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.set_value_data') as mockedSettingValueData:
            mockedSettingValueData = True

            #test if method succes
            assert self.goodColorLightController.set_color_by_label("blue") == True

            #test if method return good type of data
            assert isinstance(self.goodColorLightController.set_color_by_label("blue"), bool) == True

            #test if method detect bad parametter
            assert self.goodColorLightController.set_color_by_label(1) == False

        #test if method detect color label value not found
        self.goodColorLightController.moduleNode.values = {}

        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.set_value_data') as mockedSettingValueData:
            mockedSettingValueData = True

            assert self.goodColorLightController.set_color_by_label("blue") == False

        #test if method detect setting value data error
        self.goodColorLightController.moduleNode.values = {'1': FakeZWaveValue(1, 'color index')}
        self.goodColorLightController.moduleNode.values['1'].data = "red"

        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.set_value_data') as mockedSettingValueData:
            mockedSettingValueData.return_value = False

            assert self.goodColorLightController.set_color_by_label("blue") == False

        #test if method detect error
        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.set_value_data') as mockedSettingValueData:
            mockedSettingValueData = True
        
            assert self.badColorLightController.set_color_by_label("blue") == False


    def test_setting_color_by_rgbw(self):
        """
            1.test if method succes
            2.test if method return good type of data
            3.test if method detect bad parametter
            4.test if method detect color value not found
            5.test if method detect setting value data error
            6.test if method detect error
        """

        self.goodColorLightController.moduleNode.values = {'1': FakeZWaveValue(1, 'color')}
        self.goodColorLightController.moduleNode.values['1'].data = "#0066"

        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.set_value_data') as mockedSettingValueData:
            mockedSettingValueData = True

            #test if method succes
            assert self.goodColorLightController.set_color_by_rgbw("#0000") == True

            #test if method return good type of data
            assert isinstance(self.goodColorLightController.set_color_by_rgbw("#0000"), bool) == True

            #test if method detect bad parametter
            assert self.goodColorLightController.set_color_by_rgbw(1) == False

        #test if method detect color label value not found
        self.goodColorLightController.moduleNode.values = {}

        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.set_value_data') as mockedSettingValueData:
            mockedSettingValueData = True

            assert self.goodColorLightController.set_color_by_rgbw("#0000") == False

        #test if method detect setting value data error
        self.goodColorLightController.moduleNode.values = {'1': FakeZWaveValue(1, 'color')}
        self.goodColorLightController.moduleNode.values['1'].data = "#0066"

        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.set_value_data') as mockedSettingValueData:
            mockedSettingValueData.return_value = False

            assert self.goodColorLightController.set_color_by_rgbw("#0000") == False

        #test if method detect error
        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.set_value_data') as mockedSettingValueData:
            mockedSettingValueData = True
        
            assert self.badColorLightController.set_color_by_rgbw("#0000") == False