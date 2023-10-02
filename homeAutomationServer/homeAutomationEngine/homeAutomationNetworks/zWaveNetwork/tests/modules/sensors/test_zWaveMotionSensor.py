import os
import unittest
import sys
import mock

from unittest.mock import patch, mock_open, MagicMock

sys.path.append("..")

from fakeClasses.fakeNode import *
from fakeClasses.fakeValue import *

from zWaveNetwork.classes.zWaveModules.zWaveSensors.zWaveMotionSensor import *


class Test_ZWaveMotionSensor:
    """
        testing class of an zwave motion sensor
    """

    goodLuminanceSensor = ZWaveMotionSensor(FakeNode(1, "module", "module"), {})
    badLuminanceSensor = ZWaveMotionSensor(False, {})