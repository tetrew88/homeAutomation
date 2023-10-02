class Value:

    def __init__(self, id, label, data):
        self.id = id
        self.label = label
        self.data = data


    
    def serialize(self):
        data = {}

        data['id'] = self.id
        data['label'] = self.label
        data['data'] = self.data

        return data