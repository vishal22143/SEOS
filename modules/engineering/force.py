"""
SEOS Engineering Force Library
"""

from math import pi

GRAVITY = 9.81


def piston_area(diameter_mm):

    return (pi * diameter_mm ** 2) / 4


def rod_area(rod_mm):

    return (pi * rod_mm ** 2) / 4


def annulus_area(bore_mm,rod_mm):

    return piston_area(bore_mm)-rod_area(rod_mm)


def hydraulic_force(area_mm2,pressure_bar):

    return area_mm2*pressure_bar*0.1


def cylinder_extension_force(
        bore_mm,
        pressure_bar):

    return hydraulic_force(
        piston_area(bore_mm),
        pressure_bar
    )


def cylinder_retraction_force(
        bore_mm,
        rod_mm,
        pressure_bar):

    return hydraulic_force(
        annulus_area(
            bore_mm,
            rod_mm),
        pressure_bar
    )


def weight_force(mass_kg):

    return mass_kg*GRAVITY


def resultant_force(*forces):

    return sum(forces)
