import os
import unittest
import sys
import mock

from unittest.mock import patch, mock_open, MagicMock

sys.path.append("..")


from fakeClasses.fakeValue import *
from fakeClasses.fakeNode import *

from zWaveNetwork.classes.zWaveValues.zWaveParametter import *


class Test_ZWaveValue:
    """
        testing class of an zwave value
    """


    goodParametter = ZWaveParametter(FakeZWaveValue(1, 'test1'))
    badParametter = ZWaveParametter(False)