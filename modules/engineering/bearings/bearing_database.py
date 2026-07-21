from modules.engineering.bearings.data.bearing_data import BEARING_DATABASE

class BearingDatabase:

    def __init__(self):
        self.data=BEARING_DATABASE

    def get(self,number):
        return self.data.get(str(number))

    def all(self):
        return self.data

    def search_bore(self,bore):
        return [
            b for b in self.data.values()
            if b["bore"]==bore
        ]
