from core import config
from doctor import Doctor


def test_doctor_reports_healthy_core(tmp_path, monkeypatch):
    monkeypatch.setitem(config.CONFIG, "database", str(tmp_path / "seos.db"))

    doctor = Doctor()
    results = doctor.run()

    assert doctor.healthy()
    assert all(passed for passed, _name, _detail in results)
    assert {name for _passed, name, _detail in results} >= {
        "database_schema",
        "kernel_start",
        "module_load",
        "kernel_diagnostics",
    }