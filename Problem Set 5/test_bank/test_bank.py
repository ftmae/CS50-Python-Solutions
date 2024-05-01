from bank import value
def text_hello():
    assert value("Hello") == 0
    assert value("Hello Elaine.") == 0

def test_h():
    assert value("Hey There!") == 20
    assert value("Hi") == 20

def test_greeting():
    assert value("What's Up?") == 100
    assert value("AMENA!") == 100
