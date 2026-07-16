from dataclasses import dataclass


@dataclass
class HydraulicCylinder:
    name: str
    bore_mm: float
    rod_mm: float
    stroke_mm: float
    pressure_bar: float

    @property
    def piston_area_mm2(self):
        return 3.14159265359 * (self.bore_mm ** 2) / 4

    @property
    def push_force_newton(self):
        return self.piston_area_mm2 * self.pressure_bar * 0.1

    @property
    def push_force_kN(self):
        return self.push_force_newton / 1000
