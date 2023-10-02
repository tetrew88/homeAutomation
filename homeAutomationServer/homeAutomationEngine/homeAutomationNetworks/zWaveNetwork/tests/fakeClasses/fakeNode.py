class FakeNode:
	def __init__(self, id, deviceType, cmdClass):
		self.node_id = id
		self.device_type = deviceType
		self.command_classes_as_string = cmdClass
		self.name = "test"
		self.location = 1
		self.is_awake = True
		self.is_failed = False
		self.is_ready = True
		self.is_sleeping = False
		self.manufacturer_name = "test"
		self.product_name = "test"
		self.product_type = "test"
		self.type = "test"
		self.values = {}
		self.canWakeUp = False
		self.is_awake = False
		self.is_failed = False
		self.is_ready = False
		self.is_sleeping = False
		self.batteryLevel = 100
		self.command_classes_as_string = ['relay', 'test']
		self.node = self

	def set_field(self, field, fieldData):
		if field == 'name':
			self.name = fieldData
		if field == 'location':
			self.location = fieldData
			
	
	def get_values(self, *args, **kwargs):
		return self.values

	
	def can_wake_up(self):
		return self.canWakeUp

	def get_battery_level(self):
		return self.batteryLevel

	def assign_return_route(self):
		return True

	def neighbor_update(self):
		return True

	def network_update(self):
		return True

	def refresh_info(self):
		return True

	def refresh_value(self):
		return True

	def heal(self):
		return True

	def add_node(self):
		return True

	def remove_node(self):
		return True

	def soft_reset(self):
		return True

	def hard_reset(self):
		return True