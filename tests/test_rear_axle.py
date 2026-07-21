from modules.machines.kubota_b2441n.systems.rear_axle import RearAxle

axle=RearAxle()

def test_drive():
    assert axle.drive=="Rear"

def test_differential():
    assert axle.differential=="Spiral Bevel"

def test_final_drive():
    assert axle.final_drive=="Bull Gear"

def test_max_load():
    assert axle.max_load==1600

def test_pto():
    assert axle.pto_supported is True
