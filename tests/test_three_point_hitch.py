from modules.machines.kubota_b2441n.hitch.three_point_hitch import ThreePointHitch

h=ThreePointHitch()

def test_category():
    assert h.category=="Category I"

def test_capacity():
    assert h.lift_capacity==750

def test_height():
    assert h.lift_height==820

def test_can_lift():
    assert h.can_lift(500)

def test_cannot_lift():
    assert not h.can_lift(900)
