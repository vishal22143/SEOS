from modules.machines.kubota_b2441n.hydraulics.hydraulic_system import HydraulicSystem

h=HydraulicSystem()

def test_flow():
    assert h.flow==23.5

def test_pressure():
    assert h.pressure==170

def test_area():
    assert h.piston_area_mm2()>3000

def test_force():
    assert h.lifting_force_newton()>50000
