"""
==========================================================
SEOS Kernel
==========================================================
"""

from enum import Enum, auto

from core.config import CONFIG
from core.database import Database
from core.logger import logger
from core.module_manager import ModuleManager


class KernelState(Enum):
    STOPPED = auto()
    STARTING = auto()
    RUNNING = auto()
    STOPPING = auto()


class Kernel:

    def __init__(self):
        self.state = KernelState.STOPPED
        self.database = None
        self.module_manager = ModuleManager()

    def start(self):
        if self.state != KernelState.STOPPED:
            logger.warning("Kernel already running.")
            return

        self.state = KernelState.STARTING
        logger.info("Starting SEOS...")

        self.database = Database(CONFIG["database"])
        self.module_manager.load_all()

        self.state = KernelState.RUNNING
        logger.info("SEOS Started.")

    def shutdown(self):
        if self.state == KernelState.STOPPED:
            return

        self.state = KernelState.STOPPING
        self.module_manager.shutdown_all()

        if self.database:
            self.database.close()
            self.database = None

        self.state = KernelState.STOPPED
        logger.info("SEOS Stopped.")

    def diagnostics(self):
        tables = []
        missing_tables = []

        if self.database:
            tables = self.database.table_names()
            missing_tables = sorted(self.database.missing_tables())

        return {
            "state": self.state.name,
            "modules": self.module_manager.count(),
            "loaded_modules": self.module_manager.loaded_count(),
            "failed_modules": [record.name for record in self.module_manager.failed()],
            "database_tables": tables,
            "missing_database_tables": missing_tables,
        }