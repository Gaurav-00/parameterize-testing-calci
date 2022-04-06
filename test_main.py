import main
def test_divisible5_1():
    a=10
    result=main.divisible5(a)
    assert result==True
def test_divisible5_2():
    a=11
    result=main.divisible5(a)
    assert result==False
def test_divisible7_1():
    a=7
    result=main.divisible7(a)
    assert result==True

def test_divisible7_2():
    a=8
    result=main.divisible7(a)
    assert result==False

def test_divisible9_1():
    a=9
    result=main.divisible9(a)
    assert result==True
def test_divisible9_2():
    a=11
    result=main.divisible9(a)
    assert result==False
def test_divisible11_1():
    a=11
    result=main.divisible11(a)
    assert result==True
def test_divisible11_2():
    a=12
    result=main.divisible11(a)
    assert result==False


if __name__=="__main__":
    main()