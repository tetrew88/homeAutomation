class Room:
    def __init__(self, id, name, type):
        self.id = id
        self.name = name
        self.type = type
        self.content = []
        self.events = []



    @property
    def temperature(self):
        pass


    @property
    def luminance(self):
        pass



    def serialize(self):
        data = []
        content = []

        data["id"] = self.id
        data['name'] = self.name
        data['type'] = self.type

        for module in self.content:
            content.append(module.serialize())
        data['content'] = content
        
        data['temperature'] = self.temperature
        data['luminance'] = self.luminance
    
        return data
