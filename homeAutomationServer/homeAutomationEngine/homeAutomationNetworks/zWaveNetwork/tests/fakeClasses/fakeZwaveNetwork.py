from .fakeNode import *
from .fakeController import *

class FakeZwaveNetwork:
	def __init__(self, homeId, state, ready):
		"""
			class created for substitute the zwaveNetwork class
			during the test
		"""
		self.home_id = homeId
		self.state = state
		self.is_ready = ready
		self.nodes = {'0001': FakeNode(1, "bulb", "bulb"), '002': FakeNode(2, "light", "bulb")}
		self.controller = FakeController(FakeNode(3, "main controller","controller"))
		self.modulesList = []

	def start(self):
		pass

	def stop(self):
		pass

	def write_config(self):
		pass

	def heal(self):
		pass

	def destroy(self):
		pass

	def SIGNAL_NETWORK_STARTED(self):
		pass

	def SIGNAL_NETWORK_READY(self):
		pass

	def SIGNAL_NETWORK_AWAKED(self):
		pass


	def SIGNAL_NETWORK_FAILED(self):
		pass

	def SIGNAL_NETWORK_STOPPED(self):
		pass

	def SIGNAL_NETWORK_RESETTED(self):
		pass


	def SIGNAL_DRIVER_READY(self):
		pass

	def SIGNAL_DRIVER_FAILED(self):
		pass

	def SIGNAL_DRIVER_REMOVED(self):
		pass

	def SIGNAL_DRIVER_RESET(self):
		pass


	def SIGNAL_NODE_ADDED(self):
		pass

	def SIGNAL_NODE_REMOVED(self):
		pass

	def SIGNAL_NODE_READY(self):
		pass


	def SIGNAL_VALUE_CHANGED(self):
		pass