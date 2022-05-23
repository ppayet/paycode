from mlproject.distance import haversine

def test_haversine():
    assert type(haversine(0,0,0,0)) == float
