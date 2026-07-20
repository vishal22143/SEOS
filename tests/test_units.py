from modules.engineering.units import *


def test_mm():
    assert mm_to_m(1000) == 1


def test_bar():
    assert mpa_to_bar(20) == 200
