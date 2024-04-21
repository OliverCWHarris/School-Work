#valid = 2 caps, 2 lower, 3 numbers, no special symbols

def caps_check(string):
    str_list=list(string)
    caps_total=0

    for i in range(0,len(str_list)):
        upper=str_list[i].upper()
        if str_list[i]==upper:
            caps_total+=1
    
    if caps_total<=0:
        return False
    elif caps_total>=2:
        return True
    else:
        return False

def lower_check(string):
    str_list=list(string)
    lower_total=0

    for i in range(0,len(str_list)):
        lower=str_list[i].lower()
        if str_list[i]==lower:
            lower_total+=1
    
    if lower_total<=0:
        return False
    elif lower_total>=2:
        return True
    else:
        return False

def num_check(string):
    str_list=list(string)
    nums_total=0
    nums=[0,1,2,3,4,5,6,7,8,9]

    for i in range(0,len(str_list)):
        if str_list[i] in nums:
            nums_total+=1
    
    if nums_total<=0:
        return False
    elif nums_total>=3:
        return True
    else:
        return False

def special_check(string):
    str_list=list(string)
    symbol_total=0
    symbols=['!','"','£','$','%','^','&','*','(',')','-','_','+','=','[',']','{','}',':',';','@',"'",'~','#','<','>',',','.','?','/','|','`','¬','¦']

    for i in range(0,len(str_list)):
        if str_list[i] in symbols:
            symbol_total+=1
    
    if symbol_total<=0:
        return True
    elif symbol_total>=1:
        return False
    else:
        return False

completed=False
while completed==False:
    print('requirements for password \n -2 or more capitals \n -2 or more lower case \n -3 or more numbers \n -no special characters')
    string=str(input('enter a password\n>'))
    check_results=0
    
    if caps_check(string) == True:
        check_results+=1
    if lower_check(string) == True:
        check_results+=1
    if num_check(string) == True:
        check_results+=1
    if special_check(string) == True:
        check_results+=1
    
    if check_results==4:
        print(string, 'is a good password')
    else:
        print(string, 'is a bad password')