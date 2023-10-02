from .fakeNode import *


class FakeController():
	def __init__(self, node):
		self.node = node
		self.id = self.node.node_id
		self.zwaveNetwork = False

	def add_node(self):
		key = len(self.zwaveNetwork.nodes) + 2
		self.zwaveNetwork.nodes[key] = FakeNode(key, "bulb", "light système")

	def remove_node(self):
		self.zwaveNetwork.nodes.pop('0001')