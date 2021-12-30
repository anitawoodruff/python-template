from app.foo import Foo

def test_initialise():
    Foo()
    assert True

def test_fail():
    assert 1 == 2