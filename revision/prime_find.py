def checker(num_in):
    if num_in>1:
        for i in range(2,int(num_in/2)):
            if (num_in % i)==0:
                return False
        else:
            return True
    return False

def main():
    loop1=True
    loop2=False

    while loop1==True:
        num_in=int(input('enter number above 0\n>'))
        if num_in<=0:
            print('number must be above 0')
        else:
            loop1=False
            loop2=True

        while loop2==True:
            returned=checker(num_in)
            if returned==True:
                print(num_in,'is prime')
            else:
                print(num_in,'is not prime')
            again=str(input('try another? y/n\n>'))
            if again=='y':
                loop2=False
                loop1=True
            elif again=='n':
                loop1=False
                loop2=False

main()