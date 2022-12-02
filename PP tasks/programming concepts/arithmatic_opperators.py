#this first section is for inputting the users numbers and their choice of opperator
import time
opperator=int(input("""1:Add
2:Subtract
3:Multiply
4:Divide
5:Modulus
6:Exponentiation
7:Floor division
Enter number for opperator: """))

time.sleep(1)
number1=int(input("Enter first number: "))
time.sleep(1)
number2=int(input("Enter second number: "))

#declaring the variable "output" as an integer
output=int

#every section here is for a different opperator, they all follow the same format of check opperator, perform opperator, set value "output" as the answer, then print that value
if opperator==1:
    output=number1+number2
    print(output)

elif opperator==2:
    output=number1-number2
    print(output)

elif opperator==3:
    output=number1*number2
    print(output)

elif opperator==4:
    output=number1/number2
    print(output)

elif opperator==5:
    output=number1%number2
    print(output)

elif opperator==6:
    output=number1**number2
    print(output)

elif opperator==7:
    output=number1//number2
    print(output)