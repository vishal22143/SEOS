class CenterOfGravity:

    def calculate(self,points):

        if len(points)==0:
            return (0,0,0)

        x=y=z=0

        for p in points:

            x+=p[0]
            y+=p[1]
            z+=p[2]

        n=len(points)

        return (

            x/n,
            y/n,
            z/n

        )
