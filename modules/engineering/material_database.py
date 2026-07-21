from modules.engineering.data.material_data import MATERIAL_DATABASE

class MaterialDatabase:
    def __init__(self):
        self.materials = MATERIAL_DATABASE

    def all(self):
        return self.materials

    def get(self, code):
        return self.materials.get(code.upper())

    def search_name(self, text):
        text = text.lower()
        return [
            m for m in self.materials.values()
            if text in m["name"].lower()
        ]

    def search_category(self, category):
        category = category.lower()
        return [
            m for m in self.materials.values()
            if m["category"].lower() == category
        ]

    def density_between(self, minimum, maximum):
        return [
            m for m in self.materials.values()
            if minimum <= m["density"] <= maximum
        ]

    def yield_strength_above(self, value):
        return [
            m for m in self.materials.values()
            if m["yield_strength"] >= value
        ]
