from core import control

import bge
keyboard = bge.logic.keyboard
JUST_ACTIVATED = bge.logic.KX_INPUT_JUST_ACTIVATED
ACTIVE = bge.logic.KX_SENSOR_ACTIVE

WHEEL_SPEED = 1023


class User(control.Controller):
    def update(self):
        left_wheel = 0
        right_wheel = 0
        
        if keyboard.events[bge.events.WKEY] == ACTIVE:
            left_wheel += WHEEL_SPEED
        if keyboard.events[bge.events.SKEY] == ACTIVE:
            left_wheel -= WHEEL_SPEED
            
        if keyboard.events[bge.events.EKEY] == ACTIVE:
            right_wheel += WHEEL_SPEED
        if keyboard.events[bge.events.DKEY] == ACTIVE:
            right_wheel -= WHEEL_SPEED
            
        self._outputs['left_wheel'].write(left_wheel)
        self._outputs['right_wheel'].write(right_wheel)
        
        if keyboard.events[bge.events.XKEY] == JUST_ACTIVATED:
            print(self._inputs['left_wheel'].read())
        if keyboard.events[bge.events.CKEY] == JUST_ACTIVATED:
            print(self._inputs['right_wheel'].read())

