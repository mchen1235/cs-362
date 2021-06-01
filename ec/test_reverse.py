import reverse as r

def test_1():
    assert r.reverse("Hello World.") == "World Hello."

def test_2():
    assert r.reverse("") == ""

def test_3():
    assert r.reverse("There is no period") == "period no is There"

def test_4():
    assert r.reverse("Double  space single") == "single space  Double"