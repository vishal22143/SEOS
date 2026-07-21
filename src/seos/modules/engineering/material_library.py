import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
DB=ROOT/"engineering"/"database"/"materials.json"

class MaterialLibrary:

    def __init__(self):
        if DB.exists():
            self.materials=json.loads(DB.read_text(encoding="utf-8"))
        else:
            self.materials=[]

    def get(self,name):
        for m in self.materials:
            if m["name"].lower()==name.lower():
                return m
        return None

    def all(self):
        return self.materials

if __name__=="__main__":
    lib=MaterialLibrary()
    print("Materials :",len(lib.all()))
