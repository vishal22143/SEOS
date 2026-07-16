"""SEOS Doctor Tool."""

from core.config import CONFIG
from core.database import Database, EXPECTED_TABLES
from core.kernel import Kernel, KernelState


class Doctor:

    def __init__(self):
        self.results = []

    def pass_check(self, name, detail):
        self.results.append((True, name, detail))

    def fail_check(self, name, detail):
        self.results.append((False, name, detail))

    def check_database(self):
        database = None

        try:
            database = Database(CONFIG["database"])
            missing = EXPECTED_TABLES - set(database.table_names())

            if missing:
                self.fail_check(
                    "database_schema",
                    "Missing tables: " + ", ".join(sorted(missing)),
                )
            else:
                self.pass_check(
                    "database_schema",
                    "Required tables are present.",
                )

        except Exception as error:
            self.fail_check("database", str(error))

        finally:
            if database:
                database.close()

    def check_kernel(self):
        kernel = Kernel()

        try:
            kernel.start()

            if kernel.state == KernelState.RUNNING:
                self.pass_check("kernel_start", "Kernel reached RUNNING state.")
            else:
                self.fail_check("kernel_start", "Kernel did not reach RUNNING state.")

            diagnostics = kernel.diagnostics()

            if diagnostics["failed_modules"]:
                self.fail_check(
                    "module_load",
                    "Failed modules: " + ", ".join(diagnostics["failed_modules"]),
                )
            else:
                self.pass_check("module_load", "All registered modules loaded.")

            self.pass_check("kernel_diagnostics", str(diagnostics))

        except Exception as error:
            self.fail_check("kernel", str(error))

        finally:
            kernel.shutdown()

    def run(self):
        self.results = []
        self.check_database()
        self.check_kernel()
        return self.results

    def healthy(self):
        return all(result[0] for result in self.results)


def main():
    doctor = Doctor()
    results = doctor.run()

    print("SEOS Doctor")
    print("===========")

    for passed, name, detail in results:
        status = "PASS" if passed else "FAIL"
        print(f"[{status}] {name}: {detail}")

    return 0 if doctor.healthy() else 1


if __name__ == "__main__":
    raise SystemExit(main())