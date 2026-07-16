from pathlib import Path
import sqlite3
import sys

ROOT = Path(__file__).resolve().parent.parent


def check(name, ok):
    print(f"[{'OK' if ok else 'FAIL'}] {name}")


print("=" * 50)
print("SEOS Doctor")
print("=" * 50)

check("Python >= 3.12", sys.version_info >= (3, 12))

check("core/", (ROOT / "core").exists())
check("modules/", (ROOT / "modules").exists())
check("tests/", (ROOT / "tests").exists())
check("database/", (ROOT / "database").exists())

db = ROOT / "database" / "seos.db"

if db.exists():
    try:
        sqlite3.connect(db).close()
        check("SQLite Database", True)
    except Exception:
        check("SQLite Database", False)
else:
    check("SQLite Database", False)

print()
print("Repository Root:", ROOT)
print("=" * 50)
