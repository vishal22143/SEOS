"""
SEOS Configuration
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CONFIG = {
    "database": str(ROOT / "database" / "seos.db"),
    "version": "0.2.0-alpha"
}
