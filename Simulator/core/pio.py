class Input():
    def __init__(self, name, pin):
        """ self.pin also takes function handles. """
        self.pin = pin
        self.name = name
        
    def read(self):
        if callable(self.pin):
            value = self.pin()
        else:
            value = self.pin
        return value
        
    def __repr__(self):
        return "Input({0}, {1})".format(self.name, self.pin)


class Output():
    def __init__(self, name, pin):
        """ self.pin also takes function handles. """
        self.pin = pin
        self.name = name
        
    def write(self, value):
        if callable(self.pin):
            self.pin(value)
        else:
            self.pin = value
        
    def __repr__(self):
        return "Output({0}, {1})".format(self.name, self.pin)

