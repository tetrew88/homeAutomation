class FakeZWaveValue:
    def __init__(self, value_id, label):
        self.value_id = value_id
        self.label = label
        self.data = "test"
        self.data_items = []
        self.id_on_network = 1
        self.max = 1
        self.min = 1
        self.node = 1
        self.type = "int"
        self.units = "°c"
        self.is_read_only = True