from exercises.is_vowel import is_vowel

def test_chars():
    for ch in 'aeiouAEIOU':
        assert is_vowel(ch) is True
    for ch in 'bcdfgBCDFGxYz':
        assert is_vowel(ch) is False
