"""
SEOS Database Manager
"""

import sqlite3
from pathlib import Path


SCHEMA_STATEMENTS = [
    """
    CREATE TABLE IF NOT EXISTS materials (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        grade TEXT,
        density REAL,
        yield_strength REAL,
        tensile_strength REAL,
        notes TEXT,
        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS requirements (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        category TEXT,
        priority TEXT NOT NULL DEFAULT 'medium',
        status TEXT NOT NULL DEFAULT 'open',
        description TEXT,
        source TEXT,
        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
    """,
]


class Database:

    def __init__(self, path):

        self.path = Path(path)

        # Create parent directory automatically
        self.path.parent.mkdir(parents=True, exist_ok=True)

        self.connection = sqlite3.connect(str(self.path))
        self.connection.row_factory = sqlite3.Row
        self.initialize_schema()

    def initialize_schema(self):

        with self.connection:

            for statement in SCHEMA_STATEMENTS:

                self.connection.execute(statement)

    def table_names(self):

        cursor = self.connection.execute(
            "SELECT name FROM sqlite_master WHERE type = 'table' ORDER BY name"
        )

        return [row["name"] for row in cursor.fetchall()]

    def close(self):

        if self.connection:

            self.connection.close()
            self.connection = None
