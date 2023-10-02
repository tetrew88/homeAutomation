class Module:
    """

    """
    
    
    def __init__(self, id, name, location, role, protocol):
        """constructor"""
        
        self.id = id
        self.name = name
        self.location = location
        self.role = role
        
        self.protocol = protocol


    def serialize(self):
        data = {}
        valuesList = []
        paramettersList = []

        data["id"] = self.id
        data['name'] = self.name
        data['location'] = self.location
        data['role'] = self.role
        
        data['protocol'] = self.protocol

        return data