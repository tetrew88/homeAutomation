from .zWaveLightController import *


class ZWaveColorLightController(ZWaveLightController):
    """
		class bringing all the information and functionality of an color bulb.
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
					lightUp: allow to know if the light was on(true/false)
					startLevel: allow to get the start level of the light(int)

                #color light controller property
                    colorLabel: label of the color used by the light(str)
                    colorValue: rgbw value of the color used by the light(str)
                    colorPalette: list of color can be used by the light controller (list(str))
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

                #color light controller methods:
                    set_color_by_label: method used for modify the color of the light by an label color
	"""

    def __init__(self, moduleNode, type="color light controller"):
        ZWaveLightController.__init__(self, moduleNode, type)


    
    @property
    def colorLabel(self):
        """
            property allow to know the label of the color used by the light

                return:
                    if succes return str
                    else return false
        """

        colorLabel = False
        
        for value in self.values:
            if value.label == "color index":
                colorLabel = value.data
                break
            else:
                colorLabel = False

        return colorLabel


    @property
    def colorValue(self):
        """
            property allow to know the rgbw value of the color used by the light

                return:
                    if succes return str(rgbw data)
                    else return false
        """

        colorValue = 0
        for value in self.values:
            if value.label == "color":
                colorValue = str(value.data)
                break
            else:
                colorValue = False
        
        return colorValue


    @property
    def colorPalette(self):
        """
            property representing the list of color can be used by the light controller (list(str))
        
                return:
                    if succes return list of color label
                    else return false
        """
        
        colorPalette = False
        
        for value in self.values:
            if value.label == "color index":
                colorPalette = value.dataItems
                break
            else:
                colorPalette = False

        return colorPalette



    """SET METHOD"""
    def set_color_by_label(self, label):
        """
            method used for modify the color of the light by an label color

                return:
                    true if succes
                    else false
        """
        
        colorLabelValue = succes = False
        
        if isinstance(label, str):
            for value in self.values:
                if value.label.lower() == "color index":
                    colorLabelValue = value
                    break
                else:
                    colorLabelValue = False
            
            if colorLabelValue != False:
                if self.set_value_data(colorLabelValue.id, label):
                    succes = True
                else:
                    succes = False
            else:
                succes = False
        else:
            succes = False

        return succes


    def set_color_by_rgbw(self, rgbwValue):
        colorValue = succes = False
        
        if isinstance(rgbwValue, str):
            for value in self.values:
                if value.label.lower() == "color":
                    colorValue = value
                    break
                else:
                    colorValue = False
            
            if colorValue != False:
                if self.set_value_data(colorValue.id, rgbwValue):
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

        #color label
        data["colorLabel"] = self.colorLabel

        #color value
        data["colorValue"] = self.colorValue

        #color palette
        data["colorPalette"] = self.colorPalette

        return data