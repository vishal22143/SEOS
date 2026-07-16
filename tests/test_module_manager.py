from core.module_manager import ModuleManager


def test_module_manager_loads_registered_modules():
    manager = ModuleManager()

    manager.load_all()

    assert manager.count() == 8
    assert manager.loaded_count() == 8
    assert manager.failed() == []


def test_module_manager_reports_failed_module():
    manager = ModuleManager(module_specs=(("missing", "modules.missing"),))

    manager.load_all()

    assert manager.count() == 1
    assert manager.loaded_count() == 0
    assert manager.failed()[0].name == "missing"