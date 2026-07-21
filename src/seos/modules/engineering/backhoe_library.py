import json
from pathlib import Path

class BackhoeLibrary:

    def __init__(self, root):

        db = Path(root) / "engineering/database/backhoe.json"

        self.data = json.loads(db.read_text())

    def assemblies(self):

        return self.data["assemblies"]
