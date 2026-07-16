"""SEOS module registry and lifecycle manager."""

from dataclasses import dataclass
from importlib import import_module


DEFAULT_MODULES = (
    ("ai", "modules.ai"),
    ("cad", "modules.cad"),
    ("digital_twin", "modules.digital_twin"),
    ("engineering", "modules.engineering"),
    ("hydraulics", "modules.hydraulics"),
    ("knowledge", "modules.knowledge"),
    ("manufacturing", "modules.manufacturing"),
    ("simulation", "modules.simulation"),
)


@dataclass
class ModuleRecord:
    name: str
    package: str
    status: str = "registered"
    error: str | None = None

    def to_dict(self):
        return {
            "name": self.name,
            "package": self.package,
            "status": self.status,
            "error": self.error,
        }


class ModuleManager:

    def __init__(self, module_specs=None):
        self.module_specs = tuple(module_specs or DEFAULT_MODULES)
        self.modules = []

    def load_all(self):
        self.modules = []

        for name, package in self.module_specs:
            record = ModuleRecord(name=name, package=package)

            try:
                import_module(package)
                record.status = "loaded"
            except Exception as error:
                record.status = "failed"
                record.error = str(error)

            self.modules.append(record)

    def shutdown_all(self):
        for record in self.modules:
            if record.status == "loaded":
                record.status = "stopped"

    def count(self):
        return len(self.modules)

    def loaded_count(self):
        return len([record for record in self.modules if record.status == "loaded"])

    def failed(self):
        return [record for record in self.modules if record.status == "failed"]

    def diagnostics(self):
        return [record.to_dict() for record in self.modules]