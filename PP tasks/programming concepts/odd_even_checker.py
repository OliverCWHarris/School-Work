#first 3 lines declare the lists of numbers, even numbers, and odd numbers
numbers=[1,2,3,4,5,6,7,8,9,10]
numbers_odd=[]
numbers_even=[]

#declares the counting variable
count=0

#simple while loop to continue sorting numbers until the count reaches 10 (max number of numbers in the numbers[] list)
while count!=10:
    if numbers[count]%2==0:
        numbers_even.insert(count, numbers[count])
        count+=1
    else:
        numbers_odd.insert(count, numbers[count])
        count+=1
    
    if count==10:
        print("odd numbers:",numbers_odd)
        print("even numbers:",numbers_even)