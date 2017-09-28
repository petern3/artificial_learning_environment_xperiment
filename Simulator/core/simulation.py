

class Simulation:
    def __init__(self, scene, root_path):
        self.scene = scene
        self.root_path = root_path
        self.vehicles = list()

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def update(self):
        for vehicle in self.vehicles:
            vehicle.update()
        