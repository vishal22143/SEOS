import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.seos.modules.calculations.calculation_engine import EngineeringCalculator

calc=EngineeringCalculator()

print("--------------------------------")
print("SEOS BUILD-035 TESTS")
print("--------------------------------")

print("Cylinder Force")
print(calc.cylinder_force(180,63))

print("--------------------------------")
print("Cylinder Area")
print(calc.cylinder_area(63))

print("--------------------------------")
print("Oil Volume")
print(calc.oil_volume(63,500))

print("--------------------------------")
print("Plate Weight")
print(calc.plate_weight(1.2,0.5,10))

print("--------------------------------")
print("Round Bar Weight")
print(calc.round_bar_weight(40,1.0))

print("--------------------------------")
print("Hydraulic Power")
print(calc.hydraulic_power(180,28))

print("--------------------------------")
print("Bucket Capacity")
print(calc.bucket_capacity(0.30,0.45,0.40))

print("--------------------------------")
print("Moment")
print(calc.lifting_moment(25000,1.5))

print("--------------------------------")
print("Safety Factor")
print(calc.safety_factor(250,125))

print("--------------------------------")
print("ALL TESTS PASSED")
