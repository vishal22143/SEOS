import json
from pathlib import Path

class HydraulicLibrary:

    def __init__(self, root):

        db = Path(root) / "engineering/database/hydraulic_cylinders.json"

        self.data = json.loads(db.read_text())

    def all(self):

        return self.data["cylinders"]
