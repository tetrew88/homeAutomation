import os
import unittest
import sys
import mock

from unittest.mock import patch, mock_open, MagicMock

sys.path.append("..")

from fakeClasses.fakeNode import *
from fakeClasses.fakeValue import *

from zWaveNetwork.classes.zWaveModules.zWaveSensors.zWaveSensor import *
from zWaveNetwork.classes.zWaveModules.zWaveSensors.zWaveLuminanceSensor import *


class Test_ZWaveSensor:
      
    goodSensor = ZWaveSensor(FakeNode(1, "module", "module"), {})
    badSensor = ZWaveSensor(False, {})


    def test_strSensorsList_property(self):
        """
            1.test if method succes
            2.test if method return good type of data
        """

        self.goodSensor.sensors = {'luminance sensor': ZWaveLuminanceSensor(FakeNode(1, "module", "module"))}

        #test if method succes
        assert self.goodSensor.strSensorsList == ['luminance sensor']

        #test if method return good type of data
        assert isinstance(self.goodSensor.strSensorsList, list) == True



