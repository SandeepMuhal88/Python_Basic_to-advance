def Divide(a,b):
    if b==0:
        raise ValueError("Demoninator cannot be zero")
    return a//b

try:
    a,b=map(int,input("Enter two value:-").split(','))
    print(Divide(a,b))
except ValueError as e:
    print(e)