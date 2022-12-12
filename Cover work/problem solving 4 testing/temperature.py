temperature=int(input('please enter temperature in celsius\n>'))
if temperature>=-273 and temperature <=-7:
    print('solid')
else:
    if temperature>=-6 and temperature<=59:
        print('liquid')
    else:
        if temperature>=59:
            print('gas')
        else:
            print('not found')