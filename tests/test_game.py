from app.game import Game

def test_initialise():
    Game()
    assert True

def test_fail():
    assert 1 == 2