biglist=[[],[]]
run=True
i=0
def entervalues():
    entername=str(input('enter a name\n>'))
    entersalary=int(input('enter a salary\n>'))
    biglist[0].append(entername)
    biglist[1].append(entersalary)

    choice=str(input('enter another? y/n\n>'))
    global lowerchoice
    lowerchoice=choice.lower

while run==True:
    entervalues()
    if lowerchoice=='y':
        i+=1
        entervalues()
    elif lowerchoice=='n':
        run=False
        print(biglist)
    else:
        print('error, invalid input')