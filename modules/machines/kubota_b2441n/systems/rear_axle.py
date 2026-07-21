from modules.machines.kubota_b2441n.systems.rear_axle_data import REAR_AXLE

class RearAxle:

    def __init__(self):
        self.data=REAR_AXLE

    @property
    def drive(self):
        return self.data["drive"]

    @property
    def differential(self):
        return self.data["differential"]

    @property
    def final_drive(self):
        return self.data["final_drive"]

    @property
    def max_load(self):
        return self.data["max_load_kg"]

    @property
    def pto_supported(self):
        return self.data["pto_supported"]
