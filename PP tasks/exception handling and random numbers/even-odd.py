import random                                                       #import random function for the dice

def roll():                                                         #create function to roll dice and return the total

    roll1=random.randint(1,6)
    roll2=random.randint(1,6)

    total=int(roll1+roll2)

    return total

def even_odd_roll(total):                                           #create function to check if the total from dice rolls is odd or even

    if (total%2==0):
        return 'even'

    elif (total%2!=0):
        return 'odd'

while True:                                                         #begin infinite loop for the try/except statement (this is where most things happen)

    try:

        bet=int(input('Enter your bet\n>'))                         #user inputs their bet amount
        choice=str(input('Enter even or odd\n>'))                   #user inputs their choice of even or odd
    
        if (even_odd_roll(roll())=='even') and (choice=='even'):    #if roll total is even and user chose even they win
            print('Congratulations! You bet',bet,'and won',bet*2)
            break
        elif (even_odd_roll(roll())=='even') and (choice=='odd'):   #if roll total is even and user chose odd they lose
            print('You bet',bet,'and lost! You get no money!')
            break
        elif (even_odd_roll(roll())=='odd') and (choice=='odd'):    #if roll total is odd and user chose odd they win
            print('Congratulations! You bet',bet,'and won',bet*2)
            break
        elif (even_odd_roll(roll())=='odd') and (choice=='even'):   #if roll total is odd and user chose even they lose
            print('You bet',bet,'and lost! You get no money!')
            break

    except ValueError:                                              #if user doesnt enter a number for the bet they are told and asked to enter again
        print('Please enter a valid number')

    except NameError:                                               #if user doesnt enter 'even' or 'odd' as their choice they are told and asked to enter again
        print('Please enter even or odd')