import os
import unittest
import sys
import mock

from unittest.mock import patch, mock_open, MagicMock

sys.path.append("..")

from fakeClasses.fakeNode import *
from fakeClasses.fakeValue import *

from zWaveNetwork.classes.zWaveModules.zWaveRelays.zWaveRelay import *


class Test_ZWaveRelay:
    """
        testing class of an zwave relay
    """

    goodRelay = ZWaveRelay(FakeNode(1, "module", "module"))
    badRelay = ZWaveRelay(False)


    def test_state(self):
        """
            1.test if method succes
            2.test if method return good type of data
            3.test if method detect switch value not found
            4.test if method detect error
        """

        self.goodRelay.moduleNode.values = {'1': FakeZWaveValue(1, 'switch')}
        self.goodRelay.moduleNode.values['1'].data = True

        #test if method succes
        assert self.goodRelay.state == True

        #test if method return good type of data
        assert isinstance(self.goodRelay.state, bool) == True

        #test if method detect switch value not found
        self.goodRelay.moduleNode.values = {}

        assert self.goodRelay.state == False

        #test if method detect error
        assert self.badRelay.state == False


    def test_switch_on(self):
        """
            1.test if method succes
            2.test if method return good type of data
            3.test if method detect switch value not found
            4.test if method detect error durring setting value
            5.test if method detect error
        """

        self.goodRelay.moduleNode.values = {'1': FakeZWaveValue(1, 'switch')}
        self.goodRelay.moduleNode.values['1'].data = True

        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.set_value_data') as mockedSettingValueData:
            mockedSettingValueData.return_value = True

            #test if method succes
            assert self.goodRelay.switch_on() == True

            #test if method return good type of data
            assert isinstance(self.goodRelay.switch_on(), bool) == True

        #test if method detect switch value not found
        self.goodRelay.moduleNode.values = {}
        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.set_value_data') as mockedSettingValueData:
            mockedSettingValueData.return_value = True

            assert self.goodRelay.switch_on() == False

        #test if method detect error durring setting value
        self.goodRelay.moduleNode.values = {'1': FakeZWaveValue(1, 'switch')}
        self.goodRelay.moduleNode.values['1'].data = True

        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.set_value_data') as mockedSettingValueData:
            mockedSettingValueData.return_value = False

            assert self.goodRelay.switch_on() == False

        #test if method detect error
        assert self.badRelay.switch_on() == False


    def test_switch_off(self):
        """
            1.test if method succes
            2.test if method return good type of data
            3.test if method detect switch value not found
            4.test if method detect error durring setting value
            5.test if method detect error
        """

        self.goodRelay.moduleNode.values = {'1': FakeZWaveValue(1, 'switch')}
        self.goodRelay.moduleNode.values['1'].data = True

        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.set_value_data') as mockedSettingValueData:
            mockedSettingValueData.return_value = True

            #test if method succes
            assert self.goodRelay.switch_off() == True

            #test if method return good type of data
            assert isinstance(self.goodRelay.switch_off(), bool) == True

        #test if method detect switch value not found
        self.goodRelay.moduleNode.values = {}
        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.set_value_data') as mockedSettingValueData:
            mockedSettingValueData.return_value = True

            assert self.goodRelay.switch_off() == False

        #test if method detect error durring setting value
        self.goodRelay.moduleNode.values = {'1': FakeZWaveValue(1, 'switch')}
        self.goodRelay.moduleNode.values['1'].data = True

        with mock.patch('zWaveNetwork.classes.zWaveModules.zWaveModule.ZWaveModule.set_value_data') as mockedSettingValueData:
            mockedSettingValueData.return_value = False

            assert self.goodRelay.switch_off() == False

        #test if method detect error
        assert self.badRelay.switch_off() == False