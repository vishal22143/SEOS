from modules.machines.kubota_b2441n.transmission.transmission_data import TRANSMISSION

class Transmission:

    def __init__(self):
        self.data=TRANSMISSION

    @property
    def type(self):
        return self.data["type"]

    @property
    def drive(self):
        return self.data["drive"]

    @property
    def forward_gears(self):
        return self.data["forward_gears"]

    @property
    def reverse_gears(self):
        return self.data["reverse_gears"]

    @property
    def pto_speed(self):
        return self.data["pto_speed_rpm"]

    @property
    def pto_power(self):
        return self.data["pto_power_hp"]

    def supports_standard_pto(self):
        return self.pto_speed==540
