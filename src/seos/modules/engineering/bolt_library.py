import json
from pathlib import Path

class BoltLibrary:

    def __init__(self, root):

        db = Path(root) / "engineering/database/bolts.json"

        self.data = json.loads(db.read_text())

    def all(self):

        return self.data["metric"]
