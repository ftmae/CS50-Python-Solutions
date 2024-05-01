from twttr import shorten

def test_shorten_only_vowels():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""
def test_shorten_vowels_number_consonant():
    assert shorten("12AEIOUDF")=="12DF"
def test_shorten_vowels_punct():
    assert shorten("aeiou!!")=="!!"
def test_shorten_print_uppercase():
    assert shorten("VowelsAEIOU") == "Vwls"
