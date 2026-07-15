"""
SEOS Database Manager
"""

import sqlite3
from pathlib import Path


class Database:

    def __init__(self, path):

        self.path = Path(path)

        # Create parent directory automatically
        self.path.parent.mkdir(parents=True, exist_ok=True)

        self.connection = sqlite3.connect(str(self.path))

    def close(self):

        if self.connection:

            self.connection.close()
