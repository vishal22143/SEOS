"""
SEOS Engineering Calculation Engine
Version 1.0
"""

from math import pi

GRAVITY = 9.81

class EngineeringCalculator:

    def cylinder_force(self, pressure_bar, bore_mm):

        pressure = pressure_bar * 100000

        bore = bore_mm / 1000

        area = pi * (bore ** 2) / 4

        return pressure * area

    def cylinder_area(self, bore_mm):

        bore = bore_mm / 1000

        return pi * (bore ** 2) / 4

    def oil_volume(self, bore_mm, stroke_mm):

        area = self.cylinder_area(bore_mm)

        stroke = stroke_mm / 1000

        return area * stroke

    def steel_weight(self,length,width,height,density=7850):

        volume=length*width*height

        return volume*density

    def round_bar_weight(self,diameter,length,density=7850):

        dia=diameter/1000

        area=pi*(dia**2)/4

        volume=area*length

        return volume*density

    def plate_weight(self,length,width,thickness,density=7850):

        t=thickness/1000

        return length*width*t*density

    def hydraulic_power(self,pressure_bar,flow_lpm):

        return (pressure_bar*flow_lpm)/600

    def bucket_capacity(self,width,height,depth,fill_factor=0.9):

        return width*height*depth*fill_factor

    def lifting_moment(self,force,distance):

        return force*distance

    def safety_factor(self,yield_strength,working_stress):

        return yield_strength/working_stress

if __name__=="__main__":

    calc=EngineeringCalculator()

    print("--------------------------------")

    print("Cylinder Force")

    print(calc.cylinder_force(180,63))

    print("--------------------------------")
