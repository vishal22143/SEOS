import json
from pathlib import Path

class TractorLibrary:

    def __init__(self, root):

        db = Path(root) / "engineering/database/tractor.json"

        self.data = json.loads(db.read_text())

    def machine(self):

        return self.data
