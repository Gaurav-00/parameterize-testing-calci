def divisible9(x):
    if x%9==0:
        return True
    else:
        return False
def divisible5(x):
    if x%5==0:
        return True
    else:
        return False

def divisible7(x):
    if x%7==0:
        return True
    else:
        return False


def divisible11(x):
    if x % 11 == 0:
        return True
    else:
        return False
if __name__=="__main__":
    n1=int(input("Enter the number-:"))
    print(divisible5(n1))
    print(divisible7(n1))
    print(divisible9(n1))
    print(divisible11(n1))