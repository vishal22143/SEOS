import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

sys.path.insert(0,str(ROOT))

from src.seos.modules.cg.cg_engine import CGEngine

cg=CGEngine()

cg.add("Tractor",650,0.95,0,0.60)
cg.add("Operator",75,0.90,0,1.10)
cg.add("Fuel",25,0.80,0,0.70)
cg.add("Backhoe",420,-0.80,0,1.10)

print("--------------------------------")
print("CENTER OF GRAVITY TEST")
print("--------------------------------")

print("Total Mass")
print(cg.total_mass())

print("--------------------------------")

print("CG")
print(cg.center_of_gravity())

print("--------------------------------")

print("Axle Loads")
print(cg.axle_loads(1.56))

print("--------------------------------")

print("Stability Factor")
print(cg.stability_factor(1.18))

print("--------------------------------")
print("CG ENGINE VERIFIED")
