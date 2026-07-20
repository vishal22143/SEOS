from modules.engineering.force import *


def test_piston_area():
    assert piston_area(100) > 7800


def test_extension_force():
    assert cylinder_extension_force(100,180) > 100000


def test_retraction_force():
    assert cylinder_retraction_force(100,56,180) > 60000


def test_weight_force():
    assert weight_force(100) == 981.0


def test_resultant_force():
    assert resultant_force(10,20,30) == 60
