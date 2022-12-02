import math

def sqr(tosqr):
    print(tosqr,'squared is',tosqr**2)

def sqrt(tosqrt):
    return math.sqrt(tosqrt)

while True:
    choice=int(input('1 for sqared, 2 for square root, 3 for exit\n>'))
    
    if choice==1:
        num=int(input('Enter a number\n>'))
        sqr(num)
    elif choice==2:
        num=int(input('Enter a number\n>'))
        print(sqrt(num))
    elif choice==3:
        break
    else:
        print('invalid choice')