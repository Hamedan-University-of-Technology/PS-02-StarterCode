from math import log , pow

def check(x,y):
    if x.isnumeric() and y.isnumeric():
        return float(x),float(y)
    
    else :
        raise ValueError("invalid input")

def my_log (x):
    if x > 0 :
        return log(x,2)
    raise ValueError("invalid input")

def my_pow(x,y):
    return pow(x,y)

x = input("Enter number x: ")
y = input("Enter number y: ")

x , y = check(x,y)

print(f"X**y = {my_pow(x,y)}")
print(f"log(x) = {my_log(x)}")