def hash(string):
    string_list=list(string)
    ascii_list=[]
    big_num=0

    list_len=len(string_list)

    for i in range(0,list_len):
        ascii_num=ord(string_list[i])
        ascii_list.append(ascii_num)
    
    for i in range(0,list_len):
        big_num+=ascii_list[i]
    
    modded=big_num%11
    return modded

def collision_check(hashed):
    with open('hashlist.txt','r') as f:
        lines=len(f.readlines())

    for i in range(0,lines):
        with open('hashlist.txt','r') as f:
            line=f.readline
        if line==hashed:
            hashed+=1
            collision_check(hashed)
        elif line!=hashed:
            with open('hashlist.txt','a') as f:
                f.write(hashed)
            return hashed
        else:
            return 'error'

string=str(input('enter string: '))
hashed=hash(string)
collision=collision_check(hashed)
if collision!='error':
    print('success! your hash of',string,'is',hashed)
else:
    print('error')