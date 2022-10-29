from build_word_grid import build_word_grid

def test_cat():
    result = build_word_grid("cat")
    assert result[0] == "Cat"
    assert result[1] == "cAt"
    assert result[2] == "caT"
