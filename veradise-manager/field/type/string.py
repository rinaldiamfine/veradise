class String(str):
    def __new__(cls, value):
        return str.__new__(cls, value)

    def __init__(self, value):
        str.__init__(self, value)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"String({self.value})"

class StringList([str]):
    def __new__(cls, value):
        return str.__new__(cls, value)

    def __init__(self, value):
        str.__init__(self, value)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"StringList({self.value})"