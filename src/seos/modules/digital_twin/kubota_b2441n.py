import json
from pathlib import Path


class KubotaB2441N:

    def __init__(self,root):

        db=Path(root)/"engineering/machines/kubota_b2441n.json"

        self.machine=json.loads(db.read_text())

    @property
    def name(self):
        return self.machine["machine"]

    def assemblies(self):

        return self.machine["assemblies"]

    def total_assemblies(self):

        return len(self.machine["assemblies"])

    def summary(self):

        return {

            "machine":self.name,

            "hp":self.machine["power_hp"],

            "assemblies":self.total_assemblies()

        }
