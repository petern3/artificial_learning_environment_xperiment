from . import datatypes


class Controller(object):
    def __init__(self):
        self._inputs = datatypes.NamedObjectList()
        self._outputs = datatypes.NamedObjectList()

    def register_inputs(self, inputs: dict):
        self._inputs = inputs

    def register_outputs(self, outputs: dict):
        self._outputs = outputs
        
    def update(self):
        raise NotImplementedError("Please use the child classes")