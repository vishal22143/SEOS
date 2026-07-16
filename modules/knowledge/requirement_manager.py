from core.database import Database
from modules.knowledge.requirement import Requirement


class RequirementManager:

    def __init__(self, database_path="database/seos.db"):
        self.database_path = database_path

    def initialize(self):
        database = Database(self.database_path)
        database.close()

    def add_requirement(self, requirement: Requirement):
        database = Database(self.database_path)

        try:
            database.execute(
                """
                INSERT OR REPLACE INTO requirements (
                    id,
                    title,
                    description,
                    priority,
                    status
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    requirement.id,
                    requirement.title,
                    requirement.description,
                    requirement.priority,
                    requirement.status,
                ),
            )
        finally:
            database.close()

    def get_requirement(self, requirement_id):
        database = Database(self.database_path)

        try:
            row = database.fetch_one(
                """
                SELECT id, title, description, priority, status
                FROM requirements
                WHERE id=?
                """,
                (requirement_id,),
            )
        finally:
            database.close()

        if row is None:
            return None

        return Requirement(
            row["id"],
            row["title"],
            row["description"],
            row["priority"],
            row["status"],
        )