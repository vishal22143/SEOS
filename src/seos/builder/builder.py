from pathlib import Path
from .package_engine import PackageEngine
from .git_engine import GitEngine

class SEOSBuilder:

    def __init__(self, root):
        self.root = Path(root)
        self.package = PackageEngine(self.root)
        self.git = GitEngine(self.root)

    def execute(self, package_file, message):
        self.package.install(package_file)
        self.git.commit(message)
        self.git.push()
