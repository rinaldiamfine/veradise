class Int(int):
    def __new__(cls, value):
        return int.__new__(cls, value)

    def __init__(self, value):
        int.__init__(self, value)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"Int({self.value})"

class IntList([int]):
    def __new__(cls, value):
        return list.__new__(cls, value)

    def __init__(self, value):
        list.__init__(self, value)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"IntList({self.value})"