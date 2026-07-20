"""
SEOS Engineering Pressure Library
"""

BAR_TO_PA = 100000
MPA_TO_PA = 1000000


def pressure(force_n, area_mm2):

    return force_n / area_mm2


def pressure_bar(force_n, area_mm2):

    return pressure(force_n, area_mm2) * 10


def pressure_mpa(force_n, area_mm2):

    return pressure(force_n, area_mm2)


def force(area_mm2, pressure_bar):

    return area_mm2 * pressure_bar * 0.1


def bar_to_mpa(bar):

    return bar / 10.0


def mpa_to_bar(mpa):

    return mpa * 10.0


def bar_to_pa(bar):

    return bar * BAR_TO_PA


def pa_to_bar(pa):

    return pa / BAR_TO_PA
