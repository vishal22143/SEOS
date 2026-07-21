class AssemblyTree:

    def __init__(self):

        self.tree={}

    def add(self,parent,child):

        self.tree.setdefault(parent,[]).append(child)

    def children(self,parent):

        return self.tree.get(parent,[])

    def export(self):

        return self.tree
