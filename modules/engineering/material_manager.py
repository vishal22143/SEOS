from core.database import Database
from modules.engineering.material import Material


class MaterialManager:

    def __init__(self, database_path="database/seos.db"):
        self.database_path = database_path

    def initialize(self):
        database = Database(self.database_path)
        database.close()

    def add_material(self, material: Material):
        database = Database(self.database_path)

        try:
            database.execute(
                """
                INSERT OR REPLACE INTO materials (
                    code,
                    name,
                    density,
                    yield_strength,
                    tensile_strength
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    material.code,
                    material.name,
                    material.density,
                    material.yield_strength,
                    material.tensile_strength,
                ),
            )
        finally:
            database.close()

    def get_material(self, code):
        database = Database(self.database_path)

        try:
            row = database.fetch_one(
                """
                SELECT code, name, density, yield_strength, tensile_strength
                FROM materials
                WHERE code=?
                """,
                (code,),
            )
        finally:
            database.close()

        if row is None:
            return None

        return Material(
            row["code"],
            row["name"],
            row["density"],
            row["yield_strength"],
            row["tensile_strength"],
        )