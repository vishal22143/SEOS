"""
SEOS Engineering Stress Library
"""


def tensile_stress(force_n, area_mm2):

    return force_n / area_mm2


def compressive_stress(force_n, area_mm2):

    return force_n / area_mm2


def shear_stress(force_n, area_mm2):

    return force_n / area_mm2


def bearing_stress(force_n, projected_area_mm2):

    return force_n / projected_area_mm2


def safety_factor(failure, working):

    return failure / working
