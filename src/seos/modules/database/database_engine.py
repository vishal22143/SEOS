"""
SEOS Engineering Database Engine
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

class EngineeringDatabase:

    def __init__(self):
        self.database_path = ROOT / "engineering" / "database"

    def load(self,name):

        file=self.database_path / f"{name}.json"

        if not file.exists():
            return {}

        with open(file,"r",encoding="utf-8") as f:
            return json.load(f)

    def save(self,name,data):

        file=self.database_path / f"{name}.json"

        with open(file,"w",encoding="utf-8") as f:
            json.dump(data,f,indent=4)

if __name__=="__main__":

    db=EngineeringDatabase()

    print("Available Database Folder")
    print(db.database_path)
