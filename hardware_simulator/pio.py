

class Input():
    def __init__(self, pin, is_digital=False):
        """ self.pin also takes function handles. """
        self.pin = pin
        self.is_digital = is_digital
        
    def read(self):
        if callable(self.pin):
            value = self.pin()
        else:
            value = self.pin
            
        if self.is_digital:
            assert(isinstance(value, bool))
        return value
        
    def __repr__(self):
        return "Input({0}, {1})".format(self.pin, self.is_digital)
    
class Output():
    def __init__(self, pin, is_digital=False):
        """ self.pin also takes function handles. """
        self.pin = pin
        self.is_digital = is_digital
        
    def write(self, value):
        if self.is_digital:
            assert(isinstance(value, bool))
        
        if callable(self.pin):
            self.pin(value)
        else:
            self.pin = value
        
    def __repr__(self):
        return "Output({0}, {1})".format(self.pin, self.is_digital)

