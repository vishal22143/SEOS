from modules.machines.kubota_b2441n.systems.chassis import Chassis

c=Chassis()

def test_material():
    assert c.material=="IS2062-E250"

def test_wheelbase():
    assert c.wheelbase==1560

def test_clearance():
    assert c.clearance==325

def test_mounting_points():
    assert len(c.mounting_points)==6
