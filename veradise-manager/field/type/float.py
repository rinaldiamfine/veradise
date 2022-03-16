class Float(float):
    def __new__(cls, value):
        return float.__new__(cls, value)

    def __init__(self, value):
        float.__init__(self, value)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"Float({self.value})"

class FloatList([float]):
    def __new__(cls, value):
        return float.__new__(cls, value)

    def __init__(self, value):
        float.__init__(self, value)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"FloatList({self.value})"