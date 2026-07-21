from modules.machines.kubota_b2441n.systems.front_axle import FrontAxle

axle=FrontAxle()

def test_load():
    assert axle.max_load==900

def test_angle():
    assert axle.steering_angle==55

def test_drive():
    assert axle.drive=="Front"

def test_diff():
    assert axle.differential=="Bevel Gear"
