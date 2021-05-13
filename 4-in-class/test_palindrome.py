import palindrome

def test_1():
    result = palindrome.palindrome("abba")
    assert result == True

def test_2():
    result = palindrome.palindrome("ababa")
    assert result == True

def test_3():
    result = palindrome.palindrome("")
    assert result == True

def test_4():
    result = palindrome.palindrome("abbbaaaaaa")
    assert result == False

def test_5():
    result = palindrome.palindrome(" b a b ")
    assert result == False
