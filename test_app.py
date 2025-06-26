from app import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


from app import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0.0) == 0

def test_add_large_numbers():
    assert add(1000, 2000) == 3000

def test_add_negative_numbers():
    assert add(-5, -5) == -10


