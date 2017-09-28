
class Controller(object):
    def __init__(self, chassis):
        self.chassis = chassis
        
    def run(self):
        raise NotImplementedError("Please use the child classes")