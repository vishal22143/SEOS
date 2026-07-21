from datetime import datetime

class PartNumberEngine:

    def __init__(self):

        self.prefix = {
            "assembly":"ASM",
            "part":"PRT",
            "weldment":"WLD",
            "sheetmetal":"SHT",
            "shaft":"SHF",
            "gear":"GER",
            "bearing":"BRG",
            "bolt":"BLT",
            "pin":"PIN",
            "bushing":"BSH",
            "hydraulic":"HYD"
        }

    def generate(self,
                 category,
                 machine,
                 serial):

        code=self.prefix.get(category.upper().lower(),"GEN")

        return f"{machine}-{code}-{int(serial):05d}"

    def revision(self,part,rev):

        return f"{part}-R{int(rev):02d}"

    def drawing(self,part):

        return f"DWG-{part}"

    def bom(self,part):

        return f"BOM-{part}"

    def timestamp(self):

        return datetime.now().isoformat()
