import bge
import logzero
from . import loader
from . import control
from . import datatypes

log = logzero.logger


class Chassis:
    '''All chassis must inherit from this. This class defines how objects
    are loaded into/out of the environment'''
    def __init__(self, blend_file_path, core_obj_name):
        self._libname, self._all_objects = loader.lib_load_unique(blend_file_path)
        self.obj = next(o for o in self._all_objects if o.name == core_obj_name)
        self.inputs = datatypes.NamedObjectList()
        self.outputs = datatypes.NamedObjectList()
        self._controller = None

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, val:control.Controller):
        self._controller = val
        self._controller.register_inputs(self.inputs)
        self._controller.register_outputs(self.outputs)

    def update(self):
        if self.controller is not None:
            self.controller.update()

    def __del__(self):
        bge.logic.LibFree(self._libname)