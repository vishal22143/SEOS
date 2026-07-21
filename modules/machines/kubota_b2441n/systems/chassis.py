from modules.machines.kubota_b2441n.systems.chassis_data import CHASSIS

class Chassis:

    def __init__(self):
        self.data=CHASSIS

    @property
    def material(self):
        return self.data["material"]

    @property
    def wheelbase(self):
        return self.data["wheelbase_mm"]

    @property
    def clearance(self):
        return self.data["ground_clearance_mm"]

    @property
    def weight(self):
        return self.data["weight_kg"]

    @property
    def mounting_points(self):
        return self.data["mounting_points"]
