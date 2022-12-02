#this first section is for inputting the userss numbers and their choice of opperator
import time
opperator=int(input("""1:Equal too,
2:Not equal too
3:Greater than
4:Less than
5:Greater than or equal too
6:Less than or equal too
Enter number for opperator: """))

time.sleep(1)
number1=int(input("Enter first number: "))
time.sleep(1)
number2=int(input("Enter second number: "))

#declaring the variable "output" as a boolean value
output=bool

#every section here is for a different opperator, they all follow the same format of check opperator, perform opperator, set value "output" as true or flase, then print that value
if opperator==1:
    if number1==number2:
        output=True
        print(output)
    else:
        output=False
        print(output)

elif opperator==2:
    if number1!=number2:
        output=True
        print(output)
    else:
        output=False
        print(output)

elif opperator==3:
    if number1>number2:
        output=True
        print("is",number1,"greater than",number2,"?",output)
    else:
        output=False
        print(output)

elif opperator==4:
    if number1<number2:
        output=True
        print(output)
    else:
        output=False
        print(output)

elif opperator==5:
    if number1>=number2:
        output=True
        print(output)
    else:
        output=False
        print(output)

elif opperator==6:
    if number1<=number2:
        output=True
        print(output)
    else:
        output=False
        print(output)