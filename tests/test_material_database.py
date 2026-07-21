from modules.engineering.material_database import MaterialDatabase

db = MaterialDatabase()

def test_material_exists():
    assert db.get("EN8")["code"]=="EN8"

def test_search_category():
    assert len(db.search_category("Steel"))>=1

def test_density():
    assert len(db.density_between(7800,7900))>=1

def test_strength():
    assert len(db.yield_strength_above(500))>=1
