from modules.engineering.bearings.bearing_database import BearingDatabase

db=BearingDatabase()

def test_6204():
    assert db.get("6204")["outer"]==47

def test_bore():
    assert len(db.search_bore(20))==1
