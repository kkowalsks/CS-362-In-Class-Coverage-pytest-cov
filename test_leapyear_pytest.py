import leapyear

def test_true():
    assert leapyear.leapCheck(2008) == True

def test_false():
    assert leapyear.leapCheck(2100) == False

def test_failed():
    assert leapyear.leapCheck(2000) == False