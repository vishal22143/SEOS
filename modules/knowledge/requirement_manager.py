import sqlite3
from pathlib import Path
from modules.knowledge.requirement import Requirement


class RequirementManager:

    def __init__(self, database_path="database/seos.db"):
        self.database_path = Path(database_path)

    def initialize(self):
        self.database_path.parent.mkdir(parents=True, exist_ok=True)

        conn = sqlite3.connect(self.database_path)
        cur = conn.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS requirements (
            id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            priority TEXT,
            status TEXT
        )
        """)

        conn.commit()
        conn.close()

    def add_requirement(self, requirement: Requirement):
        conn = sqlite3.connect(self.database_path)
        cur = conn.cursor()

        cur.execute("""
        INSERT OR REPLACE INTO requirements
        VALUES (?, ?, ?, ?, ?)
        """, (
            requirement.id,
            requirement.title,
            requirement.description,
            requirement.priority,
            requirement.status
        ))

        conn.commit()
        conn.close()

    def get_requirement(self, requirement_id):
        conn = sqlite3.connect(self.database_path)
        cur = conn.cursor()

        cur.execute(
            "SELECT id, title, description, priority, status FROM requirements WHERE id=?",
            (requirement_id,)
        )

        row = cur.fetchone()
        conn.close()

        if row is None:
            return None

        return Requirement(*row)
