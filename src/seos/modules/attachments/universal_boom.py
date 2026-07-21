import json
from pathlib import Path

class UniversalBoom:

    def __init__(self,root):

        db=Path(root)/"engineering/attachments/SUB001/specification.json"

        self.data=json.loads(db.read_text())

    @property
    def model(self):

        return self.data["model"]

    def compatible(self):

        return self.data["compatible_with"]

    def configuration(self):

        return self.data["configuration"]
