import bge
from .simulation import Simulation

def start(cont):
    cont.owner["Simulation"] = Simulation(cont.owner.scene, bge.logic.expandPath('//'))
    cont.script = __name__ + '.update'

def update(cont):
    cont.owner['Simulation'].update()