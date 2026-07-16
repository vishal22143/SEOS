from core.database import Database, EXPECTED_TABLES


def test_database_initializes_required_tables(tmp_path):
    database = Database(tmp_path / "seos.db")

    try:
        assert EXPECTED_TABLES.issubset(set(database.table_names()))
        assert database.missing_tables() == set()
    finally:
        database.close()