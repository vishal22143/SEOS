from modules.engineering.fasteners.fastener_database import FastenerDatabase

db=FastenerDatabase()

def test_m10():
    assert db.get("M10-8.8")["diameter"]==10

def test_grade():
    assert len(db.search_grade("8.8"))>=5
