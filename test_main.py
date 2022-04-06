import main
import pytest

@pytest.fixture
def input():
    a=25
    return a
def test_divisible5_1(input):
    #a=10

    result=main.divisible5(input)
    assert result==True
def test_divisible5_2(input):
    #a=11
    result=main.divisible5(input)
    assert result==False
def test_divisible7_1(input):
    #a=7
    result=main.divisible7(input)
    assert result==True

def test_divisible7_2(input):
    #a=8
    result=main.divisible7(input)
    assert result==False

def test_divisible9_1(input):
    #a=9
    result=main.divisible9(input)
    assert result==True
def test_divisible9_2(input):
    #a=11
    result=main.divisible9(input)
    assert result==False
def test_divisible11_1(input):
    #a=11
    result=main.divisible11(input)
    assert result==True
def test_divisible11_2(input):
    #a=12
    result=main.divisible11(input)
    assert result==False


if __name__=="__main__":
    main()