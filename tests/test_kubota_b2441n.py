from modules.machines.kubota_b2441n.tractor import KubotaB2441N

tractor=KubotaB2441N()

def test_engine():
    assert tractor.engine_hp==24

def test_lift():
    assert tractor.lift_capacity==750

def test_pto():
    assert tractor.pto_speed==540

def test_weight():
    assert tractor.weight==760
