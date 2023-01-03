from solution import detectCapitalUse



def test_1():
    assert detectCapitalUse('USA') == True


def test_2():
    assert detectCapitalUse('FlaG') == False

def test_3():
    assert detectCapitalUse('usa') == True

def test_4():
    """
    Test when the input length is 100 chars.
    """
    assert detectCapitalUse('Accccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc') == True
    
def test_5():
    """
    Test when the input length is 1 char.
    """
    assert detectCapitalUse('A') == True
    assert detectCapitalUse('a') == True
