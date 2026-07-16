import sqlite3
from pathlib import Path

from modules.engineering.material import Material


class MaterialManager:

    def __init__(self, database_path="database/seos.db"):
        self.database_path = Path(database_path)

    def initialize(self):
        self.database_path.parent.mkdir(parents=True, exist_ok=True)

        conn = sqlite3.connect(self.database_path)
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS materials (
                code TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                density REAL NOT NULL,
                yield_strength REAL NOT NULL,
                tensile_strength REAL NOT NULL
            )
        """)

        conn.commit()
        conn.close()

    def add_material(self, material: Material):
        conn = sqlite3.connect(self.database_path)
        cur = conn.cursor()

        cur.execute("""
            INSERT OR REPLACE INTO materials
            VALUES (?, ?, ?, ?, ?)
        """, (
            material.code,
            material.name,
            material.density,
            material.yield_strength,
            material.tensile_strength,
        ))

        conn.commit()
        conn.close()

    def get_material(self, code):
        conn = sqlite3.connect(self.database_path)
        cur = conn.cursor()

        cur.execute(
            "SELECT code, name, density, yield_strength, tensile_strength FROM materials WHERE code=?",
            (code,),
        )

        row = cur.fetchone()

        conn.close()

        if row is None:
            return None

        return Material(*row)
