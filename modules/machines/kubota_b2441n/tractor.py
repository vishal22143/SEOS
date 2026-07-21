from modules.machines.kubota_b2441n.tractor_data import TRACTOR

class KubotaB2441N:

    def __init__(self):
        self.spec = TRACTOR

    @property
    def engine_hp(self):
        return self.spec["engine"]["power_hp"]

    @property
    def lift_capacity(self):
        return self.spec["hydraulics"]["lift_capacity_kg"]

    @property
    def pto_speed(self):
        return self.spec["pto"]["rpm"]

    @property
    def weight(self):
        return self.spec["dimensions"]["weight_kg"]
