import pytest
from fuel import convert,gauge

def test_exception():
    with pytest.raises(ValueError):
        convert("100/10")
    with pytest.raises(ValueError):
        convert("7/5.3")
    with pytest.raises(ValueError):
        convert("one/two")
    with pytest.raises(ValueError):
        convert("72-5")
    with pytest.raises(ZeroDivisionError):
        convert("100/0")


def test_convert():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("1/100") == 1

def test_gauge():
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(0.53) == "E"
    assert gauge(75) == "75%"
    assert gauge(53) == "53%"



