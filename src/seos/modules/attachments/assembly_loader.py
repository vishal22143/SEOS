import json
from pathlib import Path

class AssemblyLoader:

    def __init__(self,root):

        db=Path(root)/"engineering/attachments/SUB001/assemblies.json"

        self.data=json.loads(db.read_text())

    def assemblies(self):

        return self.data["assemblies"]
