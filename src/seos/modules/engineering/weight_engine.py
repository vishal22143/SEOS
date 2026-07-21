class WeightEngine:

    def total(self,parts):

        total=0

        for p in parts:

            total+=p.weight*p.quantity

        return total
