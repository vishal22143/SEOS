import subprocess

class GitEngine:

    def __init__(self, root):
        self.root = root

    def commit(self, message):
        subprocess.run(["git","add","."],cwd=self.root)
        subprocess.run(["git","commit","-m",message],cwd=self.root)

    def push(self):
        subprocess.run(["git","push"],cwd=self.root)
