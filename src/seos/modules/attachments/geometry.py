from dataclasses import dataclass
from math import cos,sin,radians


@dataclass
class Point:

    x:float
    y:float
    z:float=0.0


class BoomGeometry:

    def __init__(self):

        self.boom_length=1800.0
        self.dipper_length=1200.0
        self.bucket_length=550.0

        self.boom_angle=0.0
        self.dipper_angle=0.0
        self.bucket_angle=0.0


    def boom_tip(self):

        a=radians(self.boom_angle)

        return Point(

            self.boom_length*cos(a),

            self.boom_length*sin(a)

        )


    def dipper_tip(self):

        b=self.boom_tip()

        a=radians(

            self.boom_angle+
            self.dipper_angle

        )

        return Point(

            b.x+self.dipper_length*cos(a),

            b.y+self.dipper_length*sin(a)

        )


    def bucket_tip(self):

        d=self.dipper_tip()

        a=radians(

            self.boom_angle+
            self.dipper_angle+
            self.bucket_angle

        )

        return Point(

            d.x+self.bucket_length*cos(a),

            d.y+self.bucket_length*sin(a)

        )
