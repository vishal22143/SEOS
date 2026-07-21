from modules.engineering.fasteners.data.fastener_data import FASTENER_DATABASE

class FastenerDatabase:

    def __init__(self):
        self.data = FASTENER_DATABASE

    def get(self,size):
        return self.data.get(size.upper())

    def all(self):
        return self.data

    def search_grade(self,grade):
        return [
            b for b in self.data.values()
            if b["grade"]==grade
        ]
