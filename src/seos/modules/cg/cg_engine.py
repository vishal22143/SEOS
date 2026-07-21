"""
SEOS Center of Gravity Engine
Version 1.0
"""

from dataclasses import dataclass

@dataclass
class MassPoint:

    name:str
    mass:float
    x:float
    y:float
    z:float


class CGEngine:

    def __init__(self):

        self.points=[]

    def add(self,name,mass,x,y,z):

        self.points.append(
            MassPoint(name,mass,x,y,z)
        )

    def total_mass(self):

        return sum(p.mass for p in self.points)

    def cg_x(self):

        m=self.total_mass()

        if m==0:
            return 0

        return sum(p.mass*p.x for p in self.points)/m

    def cg_y(self):

        m=self.total_mass()

        if m==0:
            return 0

        return sum(p.mass*p.y for p in self.points)/m

    def cg_z(self):

        m=self.total_mass()

        if m==0:
            return 0

        return sum(p.mass*p.z for p in self.points)/m

    def center_of_gravity(self):

        return (
            self.cg_x(),
            self.cg_y(),
            self.cg_z()
        )

    def axle_loads(self,wheelbase):

        total=self.total_mass()

        if wheelbase<=0:
            raise ValueError("Wheelbase must be greater than zero")

        cg=self.cg_x()

        front=(total*cg)/wheelbase

        rear=total-front

        return {
            "front_axle":front,
            "rear_axle":rear
        }

    def stability_factor(self,track_width):

        if track_width<=0:
            return 0

        return (track_width/2)/max(self.cg_z(),0.001)

if __name__=="__main__":

    engine=CGEngine()

    engine.add("Tractor",650,0.95,0,0.60)

    engine.add("Backhoe",420,-0.80,0,1.10)

    print("--------------------------------")
    print("Total Mass :",engine.total_mass())
    print("CG :",engine.center_of_gravity())
    print(engine.axle_loads(1.56))
