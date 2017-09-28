from chassis import bottle_robot
from controllers import control_user

class Simulation:
    def __init__(self, scene, root_path):
        self.scene = scene
        self.root_path = root_path
        self.vehicles = list()

        test_vehicle = bottle_robot.BottleRobot()
        test_vehicle.controller = control_user.User()
        self.add_vehicle(test_vehicle)

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def update(self):
        for vehicle in self.vehicles:
            vehicle.update()
        