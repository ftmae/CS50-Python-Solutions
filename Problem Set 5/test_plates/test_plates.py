from plates import is_valid

def test_len():
    assert is_valid("ADALMUNDO") == False
    assert is_valid("A") == False

def test_alpha_num():
    assert is_valid("AAAA20") == True
    assert is_valid("01ADAL") == False
    assert is_valid("212323") == False
    assert is_valid("AA22AA") == False
    assert is_valid("AAA022") == False

def test_punct():
    assert is_valid("AAA!@") == False
