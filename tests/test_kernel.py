from core import config
from core.kernel import Kernel, KernelState


def test_kernel_startup_and_shutdown(tmp_path, monkeypatch):
    monkeypatch.setitem(config.CONFIG, "database", str(tmp_path / "seos.db"))

    kernel = Kernel()
    kernel.start()

    diagnostics = kernel.diagnostics()

    assert kernel.state == KernelState.RUNNING
    assert diagnostics["loaded_modules"] == 8
    assert diagnostics["failed_modules"] == []
    assert diagnostics["missing_database_tables"] == []

    kernel.shutdown()

    assert kernel.state == KernelState.STOPPED
    assert kernel.database is None