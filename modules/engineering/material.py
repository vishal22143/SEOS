from dataclasses import dataclass


@dataclass
class Material:
    code: str
    name: str
    density: float
    yield_strength: float
    tensile_strength: float

    def to_dict(self):
        return {
            "code": self.code,
            "name": self.name,
            "density": self.density,
            "yield_strength": self.yield_strength,
            "tensile_strength": self.tensile_strength,
        }
