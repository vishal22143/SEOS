import json
from pathlib import Path

class BearingLibrary:

    def __init__(self, root):

        db = Path(root) / "engineering/database/bearings.json"

        self.data = json.loads(db.read_text())

    def all(self):

        return self.data["series"]
