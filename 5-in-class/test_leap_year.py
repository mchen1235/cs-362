import leap_year as ly

def test_1():
    result = ly.leap_year(400)
    assert result == True

def test_2():
    result = ly.leap_year(401)
    assert result == False

def test_3():
    result = ly.leap_year(404)
    assert result == True

def test_4():
    result = ly.leap_year(500)
    assert result == False