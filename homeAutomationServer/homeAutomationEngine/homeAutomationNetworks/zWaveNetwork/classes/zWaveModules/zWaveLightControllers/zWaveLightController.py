from ..zWaveModule import *


class ZWaveLightController(ZWaveModule):
	"""
		class bringing all the information and functionality of an bulb.
			attributes:
                moduleNode: network node of the module
                role: role of the module
            
            property:
                id: id of the module(str)
                name: name of the module(str)
                location: location(room id (int))

                manufacturerName: manufacturer name of the module(str)
                productName: product name of the module(str)

                productType: product type of the module(str)
                deviceType: device tye of the module(str)
                type: type of the node(str)

                values: list of node values(list of value class)
                parammetters: list of node parametters(list of parametters class)

                canWakeUp: property allow to know if the module can be wake up(True/False)

                isAwake: property allow to know if the module is awake(True/False)
                isFailed: property allow to know if the module is failed(True/False)
                isReady: property allow to know if the module is ready(True/False)
                isSleeping: property allow to know if the module is sleeping(True/False)

                batteryLevel: property allow to know the battery level of the module(int/false)

                commandClassAsString: list of command class(list (str))

                role: role of the module (str)

				#light Controller property
					level: intensity level of the light(int)
					lightUp: allow to know if the light was on
					startLevel: allow to get the start level of the light

            methods:
                get methods:
                    get_value: method allow to get an value of the module

                set methods:
                    set_name: method allow to set the name of the module
                    set_location: method allow to set the location of the module
                    set_value_data: method allow to set an value data of the module

                update methods:
                    update_return_route: method used for update the return route
                    neighbor_update: method used for updated the neigbor list of the module
                    network_update: method used for update the network of the module

                refresh method:
                    refresh_info: method used for update the info of the module
                    refresh_value: method used for refresh an value of the module
                    refresh_values: method used fot refresh all values of the module

                heal methods:
                    heal: method used for heal the module

                serialize method:
                    serialize: method used for serialize the class
	
				#light controller methods
					switch methods:
						switch_on: method allow to set the light on
						switch_off: method allow to set the light off
	"""

	def __init__(self, moduleNode, role='light controller'):
		ZWaveModule.__init__(self, moduleNode, role)



	"""PROPERTY"""
	@property
	def level(self):
		"""
			property representing the intensiy level of the light
		
				return:
					level (int)
		"""
		
		level = False

		for value in self.values:
			if value.label == "level":
				try:
					level = int(value.data)
					break
				except:
					level = False
					break
			else:
				level = False
		
		return level


	@property
	def lightUp(self):
		"""
			property allow to know is the light was on
		"""
		
		if self.level != False and self.level > 0:
			return True
		else:
			return False


	@property
	def maxLevel(self):
		"""
			property allow to know the max intensity level of the light
		"""

		maxLevel = False

		for value in self.values:
			if value.label == "level":
				maxLevel = value.max
				break
			else:
				maxLevel = False

		return maxLevel
		

	@property
	def minLevel(self):
		"""
			property allow to know the min intensity level of the light
		"""

		minLevel = False

		for value in self.values:
			if value.label == "level":
				minLevel = value.min
				break
			else:
				minLevel = False

		return minLevel


	@property
	def startLevel(self):
		startLevel = False

		for value in self.values:
			if value.label == "start level":
				startLevel = int(value.data)
				break
			else:
				startLevel = False

		return startLevel



	"""BASE METHOD"""	
	def switch_on(self):
		"""
			method allow to switch the light on

				functionning:
					check ignore start level state
					if ignore start level was on true set level of the light on start level
					else set level of the light on max
				return:
					if succes return true
					else return false
		"""
		
		ignoreStartLevel = succes = False

		for value in self.values:
			if value.label.lower() == 'ignore start level':
				ignoreStartLevel = value.data
				break
			else:
				ignoreStartLevel = True

		if ignoreStartLevel == False and self.startLevel > 0 and self.startLevel != False:
			if self.set_level(self.startLevel):
				succes = True
			else:
				succes = False
		else:
			if self.set_level(self.maxLevel):
				succes = True
			else:
				succes = False

		return succes


	def switch_off(self):
		"""
			method used for switch the ligt off

				functionning:
					set light level on min
		"""

		succes = False
		
		if self.set_level(int(self.minLevel)):
			succes = True
		else:
			succes = False

		return succes



	"""SET METHOD"""
	def set_level(self, level):
		levelValue = succes = False

		if isinstance(level, int):
			for value in self.values:
				if value.label == "level":
					levelValue = value
					break
				else:
					levelValue = False

			if levelValue != False:
				if levelValue.set_data(level):
					succes = True
				else:
					succes = False
			else:
				succes = False
		else:
			succes = False

		return succes


	def serialize(self):
		data = super().serialize()

		#level
		data['level'] = self.level

		#light up
		data['lightUp'] = self.lightUp

		#max level
		data['maxLevel'] = self.maxLevel

		#min level
		data['minLevel'] = self.minLevel

		#start level
		data['startLevel'] = self.startLevel

		return data
