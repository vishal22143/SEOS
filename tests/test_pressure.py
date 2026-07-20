from modules.engineering.pressure import *


def test_bar_to_mpa():
    assert bar_to_mpa(200) == 20


def test_mpa_to_bar():
    assert mpa_to_bar(20) == 200


def test_force():
    assert force(1000,200) == 20000
