import random


def multi_finder(recuring):
    if recuring==3:
        return 4
    elif recuring==2:
        return 3
    elif recuring==1:
        return 2
    else:
        return 0

dice1=random.randint(1,6)
dice2=random.randint(1,6)
dice3=random.randint(1,6)
#print('dices are',dice1,dice2,dice3)

dice_list=list((dice1,dice2,dice3))
#print('dice_list is',dice_list)

bet=int(input('Enter bet ammount\n>'))
#print('bet is',bet)

while True:
    try:
        plr_vlu=int(input('Enter your number (1-6)\n>'))
        #print('plr_vlu is',plr_vlu)

        if plr_vlu>=1 and plr_vlu<=6:
            number_shows=dice_list.count(plr_vlu)
            #print('number_shows is',number_shows)

            payout=bet*multi_finder(number_shows)
            #print('payout is',payout)

            if payout==0:
                print("Bad luck! You didn't win anything!")
            else:
                print('Congratulations! Your bet of',bet,'turned into',payout,'!')

            break
    except:
        print('Not between 1 anad 6!')









