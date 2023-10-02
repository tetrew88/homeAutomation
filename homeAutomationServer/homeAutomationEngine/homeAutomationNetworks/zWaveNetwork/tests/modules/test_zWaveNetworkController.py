import os
import unittest
import sys
import mock

from unittest.mock import patch, mock_open, MagicMock

sys.path.append("..")

from fakeClasses.fakeNode import *
from fakeClasses.fakeValue import *

from zWaveNetwork.classes.zWaveModules.zWaveNetworkController import *


class Test_ZWaveModule:
    """
        testing class of an zwave module
    """  

    goodZWaveNetworkController = ZWaveNetworkController(FakeNode(1, "module", "module"))


    def test_adding_node(self):
        """
            1.test if method succes
            2.test if method return good type of data
            3.test if method detect error durring adding node
        """

        with mock.patch('fakeClasses.fakeNode.FakeNode.add_node') as mockedAddingNode:
            mockedAddingNode.return_value = True

            #test if method succes
            assert self.goodZWaveNetworkController.add_node() == True

            #test if method return good type of data
            assert isinstance(self.goodZWaveNetworkController.add_node(), bool) == True

        #test if method detect error durring adding node
        with mock.patch('fakeClasses.fakeNode.FakeNode.add_node') as mockedAddingNode:
            mockedAddingNode.side_effect = Exception()

            assert self.goodZWaveNetworkController.add_node() == False


    def test_removing_node(self):
        """
            1.test if method succes
            2.test if method return good type of data
            3.test if method detect error durring removing node
        """

        with mock.patch('fakeClasses.fakeNode.FakeNode.remove_node') as mockedRemovingNode:
            mockedRemovingNode.return_value = True

            #test if method succes
            assert self.goodZWaveNetworkController.remove_node() == True

            #test if method return good type of data
            assert isinstance(self.goodZWaveNetworkController.remove_node(), bool) == True

        #test if method detect error durring adding node
        with mock.patch('fakeClasses.fakeNode.FakeNode.remove_node') as mockedRemovingNode:
            mockedRemovingNode.side_effect = Exception()

            assert self.goodZWaveNetworkController.remove_node() == False


    def test_soft_resetting_network(self):
        """
            1.test if method succes
            2.test if method return good type of data
            3.test if method detect error durring soft resetting network
        """

        with mock.patch('fakeClasses.fakeNode.FakeNode.soft_reset') as mockedSoftReset:
            mockedSoftReset.return_value = True

            #test if method succes
            assert self.goodZWaveNetworkController.soft_reset_network() == True

            #test if method return good type of data
            assert isinstance(self.goodZWaveNetworkController.soft_reset_network(), bool) == True

        #test if method detect error durring adding node
        with mock.patch('fakeClasses.fakeNode.FakeNode.soft_reset') as mockedSoftReset:
            mockedSoftReset.side_effect = Exception()

            assert self.goodZWaveNetworkController.soft_reset_network() == False


    def test_hard_resetting_network(self):
        """
            1.test if method succes
            2.test if method return good type of data
            3.test if method detect error durring hard resetting network
        """

        with mock.patch('fakeClasses.fakeNode.FakeNode.hard_reset') as mockedHardReset:
            mockedHardReset.return_value = True

            #test if method succes
            assert self.goodZWaveNetworkController.hard_reset_network() == True

            #test if method return good type of data
            assert isinstance(self.goodZWaveNetworkController.hard_reset_network(), bool) == True

        #test if method detect error durring adding node
        with mock.patch('fakeClasses.fakeNode.FakeNode.hard_reset') as mockedHardReset:
            mockedHardReset.side_effect = Exception()

            assert self.goodZWaveNetworkController.hard_reset_network() == False