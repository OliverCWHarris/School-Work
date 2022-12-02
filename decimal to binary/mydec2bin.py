def dec2bin(number,places=3):
    
    whole,dec=str(number).split('.')

    whole=int(whole)
    dec=int(dec)

    res = bin(whole).lstrip("0b") + "."

    for i in range (places):

        whole,dec=str((dec_conv(dec))*2).split('.')

        dec=int(dec)

        res=res+whole
    return res

def dec_conv(num):
    while num>1:
        num=num/10
    return num

n=input('Enter your decimal value in denary\n>')

p=int(input('Enter number of decimal places in answer\n>'))

print(dec2bin(n,places=p))