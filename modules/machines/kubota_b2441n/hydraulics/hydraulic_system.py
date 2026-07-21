import math

from modules.machines.kubota_b2441n.hydraulics.hydraulic_data import HYDRAULIC_SYSTEM

class HydraulicSystem:

    def __init__(self):
        self.data=HYDRAULIC_SYSTEM

    @property
    def flow(self):
        return self.data["pump_flow_lpm"]

    @property
    def pressure(self):
        return self.data["relief_pressure_bar"]

    def piston_area_mm2(self):
        d=self.data["cylinder_bore_mm"]
        return math.pi*d*d/4

    def lifting_force_newton(self):
        pressure=self.pressure*0.1
        area=self.piston_area_mm2()
        return pressure*area
