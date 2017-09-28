import bge
from .simulation import Simulation

from chassis import bottle_robot
from controllers import control_user

def start(cont):
    cont.owner["Simulation"] = Simulation(cont.owner.scene, bge.logic.expandPath('//'))
    
    test_vehicle = bottle_robot.BottleRobot()
    test_vehicle.controller = control_user.User()
    cont.owner["Simulation"].add_vehicle(test_vehicle)
    
    cont.script = __name__ + '.update'

def update(cont):
    cont.owner['Simulation'].update()