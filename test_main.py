import main
import pytest

@pytest.mark.parametrize("num,output",[(5,True),(2,False),(10,True),(7,False)])

#@pytest.fixture
#def input():
    #a=25
    #return a
#def test_divisible5_1(input):
    #a=10
def test_divisible5_1(num,output):
    result=main.divisible5(num)
    assert result == output

#def test_divisible7_1(input):
    #a=7
@pytest.mark.parametrize("num1,output1",[(5,True),(14,False),(10,True),(7,False)])
def test_divisible7_1(num1,output1):
    result=main.divisible7(num1)
    assert result==output1
@pytest.mark.parametrize("num2,output2",[(5,True),(2,False),(10,True),(9,False)])
def test_divisible9_1(num2,output2):
    #a=9
    result=main.divisible9(num2)
    assert result==output2
@pytest.mark.parametrize("num3,output3",[(5,True),(7,False),(11,True),(10,False)])
def test_divisible11_1(num3,output3):
    #a=11
    result=main.divisible11(num3)
    assert result==output3



if __name__=="__main__":
    pass