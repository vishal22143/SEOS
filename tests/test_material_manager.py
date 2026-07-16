from modules.engineering.material import Material
from modules.engineering.material_manager import MaterialManager


def test_material_database(tmp_path):
    manager = MaterialManager(tmp_path / "seos.db")

    manager.initialize()

    steel = Material(
        "IS2062",
        "Structural Steel",
        7850,
        250,
        410,
    )

    manager.add_material(steel)

    result = manager.get_material("IS2062")

    assert result is not None
    assert result.name == "Structural Steel"