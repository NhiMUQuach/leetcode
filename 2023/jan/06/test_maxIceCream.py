from solution import maxIceCream


def test_1():
    assert 4 == maxIceCream([1,3,2,4,1], 7)

def test_2():
    assert 0 == maxIceCream([10,6,8,7,7,8], 5)

def test_3():
    assert 6 == maxIceCream([1,6,3,1,2,5], 20)



