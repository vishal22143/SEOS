from modules.machines.kubota_b2441n.systems.front_axle_data import FRONT_AXLE

class FrontAxle:

    def __init__(self):
        self.data=FRONT_AXLE

    @property
    def max_load(self):
        return self.data["max_load_kg"]

    @property
    def steering_angle(self):
        return self.data["steering_angle_deg"]

    @property
    def drive(self):
        return self.data["drive"]

    @property
    def differential(self):
        return self.data["differential"]
