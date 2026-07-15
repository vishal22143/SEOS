"""
SEOS Module Manager
"""

class ModuleManager:

    def __init__(self):
        self.modules = []

    def load_all(self):
        self.modules = []

    def shutdown_all(self):
        self.modules.clear()

    def count(self):
        return len(self.modules)
