from hashlib import sha256

'''
input_ = input('Enter something: ')
print(sha256(input_.encode('utf-8')).hexdigest())

f=open('password.txt','a')
f.write(sha256(input_.encode('utf-8')).hexdigest())
'''

quit_=False

def setup():
    input_ = input('Enter something: ')
    f=open('password.txt','a')
    hashed=sha256(input_.encode('utf-8')).hexdigest()
    f.write(hashed)
    f.write('\n')
    f.close()
    quit()

def login():
    input_=input('Enter password: ')
    hashed=sha256(input_.encode('utf-8')).hexdigest()
    f=open('password.txt','r')
    if hashed in f:
        f.close()
        print('Welcome!')
        global quit_
        quit_=True
        quit()

while True:
    try:
        choice=int(input('1 for setup, 2 for login\n>'))
        if choice==1:
            setup()
        elif choice==2:
            login()
            if quit==True:
                break
    
    except ValueError:
        print('Please enter 1 or 2')