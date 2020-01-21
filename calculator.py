# calculator.py
def add(a,b):
    c = a + b
    return c, "+"

def subtract(a,b):
    c = a - b
    return c, "-"

def multiply(a,b):
    c = a * b
    return c, "*"
    
def divide(a,b):
    c = a / b
    return c, "/"

if __name__ == "__main__":
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    x = float(a)    
    y = float(b)
    answer, symbol = add(x,y)
    print("{} {} {} = {}".format(a,symbol,b,answer))
    answer, symbol = subtract(x,y)
    print("{} {} {} = {}".format(a,symbol,b,answer))
    answer, symbol = multiply(x,y)
    print("{} {} {} = {}".format(a,symbol,b,answer))
    answer, symbol = divide(x,y)
    print("{} {} {} = {}".format(a,symbol,b,answer))