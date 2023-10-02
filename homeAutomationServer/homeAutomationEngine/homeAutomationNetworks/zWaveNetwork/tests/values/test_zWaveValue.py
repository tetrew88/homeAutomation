import os
import unittest
import sys
import mock

from unittest.mock import patch, mock_open, MagicMock

sys.path.append("..")


from fakeClasses.fakeValue import *
from fakeClasses.fakeNode import *

from zWaveNetwork.classes.zWaveValues.zWaveValue import *


class Test_ZWaveValue:
    """
        testing class of an zwave value
    """


    goodValue = ZWaveValue(FakeZWaveValue(1, 'test1'))
    badValue = ZWaveValue(False)


    def test_id_property(self):
        """
            1.test if method return good data
            2.test if method return good type of data
            3.test if method detect error
        """

        self.goodValue.zwaveValue.id = 1
        
        assert self.goodValue.id == 1
        assert isinstance(self.goodValue.id, int) == True
        assert self.badValue.id == False


    def test_data_property(self):
        """
            1.test if method return good data
            2.test if method return good type of data
            3.test if method detect error
        """

        self.goodValue.zwaveValue.data = 100
        
        assert self.goodValue.data == 100
        assert isinstance(self.goodValue.data, int) == True
        assert self.badValue.data == False


    def test_dataItems_property(self):
        """
            1.test if method return good data
            2.test if method return good type of data
            3.test if method detect error
        """

        self.goodValue.zwaveValue.data_items = set(["test", "test2"])
        
        assert self.goodValue.dataItems == ["test", "test2"] or self.goodValue.dataItems == ["test2", "test"]
        assert isinstance(self.goodValue.dataItems, list) == True
        assert self.badValue.dataItems == False


    def test_networkId_property(self):
        """
            1.test if method return good data
            2.test if method return good type of data
            3.test if method detect error
        """

        self.goodValue.zwaveValue.id_on_network = 100
        
        assert self.goodValue.networkId == 100
        assert isinstance(self.goodValue.networkId, int) == True
        assert self.badValue.networkId == False


    def test_label_property(self):
        """
            1.test if method return good data
            2.test if method return good type of data
            3.test if method detect error
        """

        self.goodValue.zwaveValue.label = "test"
        
        assert self.goodValue.label == "test"
        assert isinstance(self.goodValue.label, str) == True
        assert self.badValue.label == False


    def test_max_property(self):
        """
            1.test if method return good data
            2.test if method return good type of data
            3.test if method detect error
        """

        self.goodValue.zwaveValue.max = 100
        
        assert self.goodValue.max == 100
        assert isinstance(self.goodValue.max, int) == True
        assert self.badValue.max == False


    def test_min_property(self):
        """
            1.test if method return good data
            2.test if method return good type of data
            3.test if method detect error
        """

        self.goodValue.zwaveValue.min = 1
        
        assert self.goodValue.min == 1
        assert isinstance(self.goodValue.min, int) == True
        assert self.badValue.min == False


    def test_nodeId_property(self):
        """
            1.test if method return good data
            2.test if method return good type of data
            3.test if method detect error
        """

        self.goodValue.zwaveValue.node = 1
        
        assert self.goodValue.nodeId == 1
        assert isinstance(self.goodValue.nodeId, int) == True
        assert self.badValue.nodeId == False


    def test_type_property(self):
        """
            1.test if method return good data
            2.test if method return good type of data
            3.test if method detect error
        """

        self.goodValue.zwaveValue.type = "string"
        
        assert self.goodValue.type == "string"
        assert isinstance(self.goodValue.type, str) == True
        assert self.badValue.type == False


    def test_units_property(self):
        """
            1.test if method return good data
            2.test if method return good type of data
            3.test if method detect error
        """

        self.goodValue.zwaveValue.units = "°c"
        
        assert self.goodValue.units == "°c"
        assert isinstance(self.goodValue.units, str) == True
        assert self.badValue.units == False


    def test_set_data(self):
        """
            1.test if method return good type of data
            2.check if method detect unvalid data
            3.test if method detect error
        """

        self.goodValue.zwaveValue.type = 'string'
        self.goodValue.zwaveValue.data = "test"

        #.test if method succes
        self.goodValue.set_data('test2')
        assert self.goodValue.data == "test2"

        #test if method return good type of data
        assert self.goodValue.set_data('test2') == True

        #check if method detect unvalid data
        assert self.goodValue.set_data(1) == False

        #test if method detect error
        assert self.badValue.set_data('test2') == False