from time import sleep
nums=[[3,7,1],[6,9,2],[5,0,1],[4,2,9],[0,2,5]]
total=0
print('list has 3 columns and 5 rows')
sleep(0.5)
col=int(input('enter column number\n>'))
col-=1
for i in nums:
    total+=i[col]
print(total)