import words

def test_1():
    result = words.words("Hello There")
    assert result == 2

def test_2():
    result = words.words(" Hello   There ")
    assert result == 2

def test_3():
    result = words.words("")
    assert result == 0

def test_4():
    result = words.words("  Hello  ")
    assert result == 1

def test_5():
    result = words.words("Hello")
    assert result == 2
