import random

rolls=[]

x=range(3)

def gamble(number):
    for i in x:
        try:
            roll=str(input('Press enter to roll a dice'))
            if roll=='':
                dice=random.randint(1,6)
                print(dice)
                rolls.append(dice)
            else:
                print("Don't type anything just press enter")
        except:
            print("No seriously just press enter")
    if rolls.count(choice)==3:
        print('You rolled',rolls)
        print('Congrats! You won',bet*3)
    else:
        print("Bad luck! You didn't win anything!")



while True:
    try:
        bet=int(input('Enter your bet\n>'))
        choice=int(input('Enter your number\n>'))
        gamble(choice)
        break
    except ValueError:
        print('Not a number!')