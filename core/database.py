"""SEOS SQLite database manager."""

import sqlite3
from pathlib import Path


EXPECTED_TABLES = {"materials", "requirements"}

SCHEMA_STATEMENTS = [
    """
    CREATE TABLE IF NOT EXISTS materials (
        code TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        density REAL NOT NULL,
        yield_strength REAL NOT NULL,
        tensile_strength REAL NOT NULL,
        notes TEXT,
        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS requirements (
        id TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        priority TEXT,
        status TEXT,
        source TEXT,
        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
    """,
]


class Database:

    def __init__(self, path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.connection = sqlite3.connect(str(self.path))
        self.connection.row_factory = sqlite3.Row
        self.initialize_schema()

    def initialize_schema(self):
        with self.connection:
            for statement in SCHEMA_STATEMENTS:
                self.connection.execute(statement)

    def execute(self, statement, parameters=()):
        with self.connection:
            return self.connection.execute(statement, parameters)

    def fetch_one(self, statement, parameters=()):
        cursor = self.connection.execute(statement, parameters)
        return cursor.fetchone()

    def table_names(self):
        cursor = self.connection.execute(
            "SELECT name FROM sqlite_master WHERE type = 'table' ORDER BY name"
        )
        return [row["name"] for row in cursor.fetchall()]

    def missing_tables(self):
        return EXPECTED_TABLES - set(self.table_names())

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None