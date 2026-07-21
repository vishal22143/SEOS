from modules.machines.kubota_b2441n.transmission.transmission import Transmission

t=Transmission()

def test_drive():
    assert t.drive=="4WD"

def test_forward_gears():
    assert t.forward_gears==9

def test_reverse_gears():
    assert t.reverse_gears==3

def test_pto_speed():
    assert t.pto_speed==540

def test_standard_pto():
    assert t.supports_standard_pto()
