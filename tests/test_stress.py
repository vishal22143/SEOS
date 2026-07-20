from modules.engineering.stress import *


def test_tensile():
    assert tensile_stress(1000,100) == 10


def test_sf():
    assert safety_factor(250,100) == 2.5
