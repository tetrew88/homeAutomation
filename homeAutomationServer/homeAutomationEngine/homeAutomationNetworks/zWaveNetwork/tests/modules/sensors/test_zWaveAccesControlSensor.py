import os
import unittest
import sys
import mock

from unittest.mock import patch, mock_open, MagicMock

sys.path.append("..")

from fakeClasses.fakeNode import *
from fakeClasses.fakeValue import *

from zWaveNetwork.classes.zWaveModules.zWaveSensors.zWaveAccesControlSensor import *


class Test_ZWaveAccesControlSensor:
    """
        testing class of an zwave acces control sensor
    """

    goodAccesControlSensor = ZWaveAccesControlSensor(FakeNode(1, "module", "module"), {})
    badAccesControlSensor = ZWaveAccesControlSensor(False, {})


    def test_acces_state_property(self):
        """
            1.test if method succes
            2.test if method return good type of data
            3.test if method detect acces control value not found
        """

        self.goodAccesControlSensor.moduleNode.values = {'1': FakeZWaveValue(1, 'access control')}
        self.goodAccesControlSensor.moduleNode.values['1'].data = 22

        #test if method succes
        assert self.goodAccesControlSensor.acces_state == "open"

        #test if method return good type of data
        assert isinstance(self.goodAccesControlSensor.acces_state, str) == True

        #test if method detect acces control value not found
        self.goodAccesControlSensor.moduleNode.values = {}

        assert self.goodAccesControlSensor.acces_state == "unknow"
        

        