import os
import unittest
import sys
import mock

from unittest.mock import patch, mock_open, MagicMock

sys.path.append("..")

from fakeClasses.fakeNode import *
from fakeClasses.fakeValue import *

from zWaveNetwork.classes.zWaveModules.zWaveSensors.zWaveLuminanceSensor import *


class Test_ZWaveLuminanceSensor:
    """
        testing class of an zwave luminance sensor
    """

    goodLuminanceSensor = ZWaveLuminanceSensor(FakeNode(1, "module", "module"), {})
    badLuminanceSensor = ZWaveLuminanceSensor(False, {})


    def test_luminance_property(self):
        """
            1.test if method succes
            2.test if method return good type of data
            3.test if method detect luminance value not found
        """

        self.goodLuminanceSensor.moduleNode.values = {'1': FakeZWaveValue(1, 'luminance')}
        self.goodLuminanceSensor.moduleNode.values['1'].data = 22

        #test if method succes
        assert self.goodLuminanceSensor.luminance == 22

        #test if method return good type of data
        assert isinstance(self.goodLuminanceSensor.luminance, int) == True

        #test if method detect luminance value not found
        self.goodLuminanceSensor.moduleNode.values = {}

        assert self.goodLuminanceSensor.luminance == False
        

        