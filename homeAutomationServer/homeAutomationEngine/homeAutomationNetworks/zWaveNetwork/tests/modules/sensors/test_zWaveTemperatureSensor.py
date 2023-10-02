import os
import unittest
import sys
import mock

from unittest.mock import patch, mock_open, MagicMock

sys.path.append("..")

from fakeClasses.fakeNode import *
from fakeClasses.fakeValue import *

from zWaveNetwork.classes.zWaveModules.zWaveSensors.zWaveTemperatureSensor import *


class Test_ZWaveTemperatureSensor:
    """
        testing class of an zwave temperature sensor
    """

    goodTemperatureSensor = ZWaveTemperatureSensor(FakeNode(1, "module", "module"), {})
    badTemperatureSensor = ZWaveTemperatureSensor(False, {})


    def test_temperature_property(self):
        """
            1.test if method succes
            2.test if method return good type of data
            3.test if method detect temperature value not found
        """

        self.goodTemperatureSensor.moduleNode.values = {'1': FakeZWaveValue(1, 'temperature')}
        self.goodTemperatureSensor.moduleNode.values['1'].data = 22

        #test if method succes
        assert self.goodTemperatureSensor.temperature == 22

        #test if method return good type of data
        assert isinstance(self.goodTemperatureSensor.temperature, int) == True

        #test if method detect temperature value not found
        self.goodTemperatureSensor.moduleNode.values = {}

        assert self.goodTemperatureSensor.temperature == False
        

        