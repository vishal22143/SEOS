import json
from pathlib import Path

class MaterialLibrary:

    def __init__(self, root):

        db = Path(root) / "engineering/database/materials.json"

        self.data = json.loads(db.read_text(encoding="utf-8"))

    def all(self):

        return self.data["materials"]

    def find(self, code):

        for m in self.data["materials"]:

            if m["code"] == code:
                return m

        return None
