class RevisionEngine:

    def __init__(self):

        self.current={}

    def next(self,part):

        if part not in self.current:

            self.current[part]=0

        self.current[part]+=1

        return self.current[part]
