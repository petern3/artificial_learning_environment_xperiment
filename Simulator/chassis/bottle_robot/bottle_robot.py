import bge
import math
import os
from core import pio
from core import chassis


BLEND_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), "bottle_robot.blend")
        

class BottleRobot(chassis.Chassis):
    def __init__(self):
        super().__init__(BLEND_PATH, 'chassis')
        self._make_joints()
        
        self.outputs.append(pio.Output('left_wheel', self.set_left_wheel_speed))
        self.outputs.append(pio.Output('right_wheel', self.set_right_wheel_speed))
        self.inputs.append(pio.Input('left_wheel', self.get_left_wheel_rotation))
        self.inputs.append(pio.Input('right_wheel', self.get_right_wheel_rotation))

    def _make_joints(self):
        to_make = [o for o in self._all_objects if 'JointTarget' in o]
        for joint in to_make:
            self._make_joint(joint)
            
    def _make_joint(self, obj1):
        obj2 = next(o for o in self._all_objects if o.name == obj1['JointTarget'])
        
        id1 = obj1.getPhysicsId()
        id2 = obj2.getPhysicsId()

        obj1['joint'] = bge.constraints.createConstraint(id1, id2,
                                 bge.constraints.GENERIC_6DOF_CONSTRAINT,
                                 0,0,0,0,0,0)
                                 
        obj1['joint'].setParam(0, 0.0, 0.0) #Start off straight with no flex
        obj1['joint'].setParam(1, 0.0, 0.0) #First 3 contrain position
        obj1['joint'].setParam(2, 0.0, 0.0)                           
        obj1['joint'].setParam(3, 0, 0) #Next three constrain rotation
        obj1['joint'].setParam(4, 0, 0)
        if not obj1.get('ZFree', False):
            obj1['joint'].setParam(5, 0.0, 0.0) #No torsional bending

    def set_left_wheel_speed(self, value):
        self._all_objects['bottle_wheel'].setAngularVelocity([0,0,value/128], True)

    def get_left_wheel_rotation(self):
        return int((self._all_objects['bottle_wheel'].localOrientation.to_euler().y+math.pi) * 512 / math.pi)

    def set_right_wheel_speed(self, value):
        self._all_objects['bottle_wheel.001'].setAngularVelocity([0,0,-value/128], True)  # Not sure why this is negative.

    def get_right_wheel_rotation(self):
        return int((self._all_objects['bottle_wheel.001'].localOrientation.to_euler().y+math.pi)* 512 / math.pi)
