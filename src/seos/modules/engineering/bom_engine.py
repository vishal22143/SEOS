class BOM:

    def __init__(self,name):

        self.name=name
        self.items=[]

    def add(self,part,qty):

        self.items.append({

            "part":part,
            "qty":qty

        })

    def export(self):

        return self.items
