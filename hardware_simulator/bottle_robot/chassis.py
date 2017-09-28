import bge
import math

import pio


def make_joints():
    to_make = [o for o in bge.logic.getCurrentScene().objects if 'JointTarget' in o]
    for joint in to_make:
        make_joint(joint)
        
def make_joint(obj1):
    obj2 = obj1.scene.objects[obj1['JointTarget']]
    
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
        
make_joints()



def set_left_wheel_speed(value):
    bge.logic.getCurrentScene().objects['bottle_wheel'].setAngularVelocity([0,0,value/128], True)

def get_left_wheel_rotation():
    return int((bge.logic.getCurrentScene().objects['bottle_wheel'].localOrientation.to_euler().y+math.pi) * 512 / math.pi)

def set_right_wheel_speed(value):
    bge.logic.getCurrentScene().objects['bottle_wheel.001'].setAngularVelocity([0,0,-value/128], True)  # Not sure why this is negative.

def get_right_wheel_rotation():
    return int((bge.logic.getCurrentScene().objects['bottle_wheel.001'].localOrientation.to_euler().y+math.pi)* 512 / math.pi)


class Chassis(object):
    def __init__(self):
        self.left_wheel_actuator = pio.Output(set_left_wheel_speed)
        self.left_wheel_sensor = pio.Input(get_left_wheel_rotation)
        self.right_wheel_actuator = pio.Output(set_right_wheel_speed)
        self.right_wheel_sensor = pio.Input(get_right_wheel_rotation)


