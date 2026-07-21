import json
from pathlib import Path

class PackageEngine:

    def __init__(self, root):
        self.root = Path(root)

    def install(self, package_file):

        data = json.loads(Path(package_file).read_text())

        for f in data["files"]:

            p = self.root / f["path"]
            p.parent.mkdir(parents=True,exist_ok=True)
            p.write_text(f["content"],encoding="utf-8")

        print("BUILD INSTALLED")
