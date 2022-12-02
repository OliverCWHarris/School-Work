number1=int(input("Enter a whole number: "))
number2=int(input("Enter another whole number: "))

TempNum1=number1
TempNum2=number2

while TempNum1!=TempNum2:
    if TempNum1>TempNum2:
        TempNum1-=TempNum2
    else:
        TempNum2-=TempNum1
Result=TempNum1
print(Result,"is the GCF of", number1,"and",number2)