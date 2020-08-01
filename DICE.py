import random
import DICE_def

default_amount = 500
Bounty_count = 0
print("\t\t\tWELCOME!!")
print('\n\nYou have '+str(default_amount)+'$ in your account')
trial = str(input('Do you want a trial game? (y-Yes/n=No):\n'))
if trial == 'y':
    print('\t\t\tTRIAL GAME\n')
    roll_t = str(input("Press r-roll :\n"))
    if (roll_t == "r"):
        print("Choose the sum:\n1.(2-6)\n2.(7)\n3.(8-12)\n")
        option = int(input('Place your bet!!:'))
        value1 = random.randint(1, 6)
        value2 = random.randint(1, 6)
        DICE_def.dice(value1)
        DICE_def.dice(value2)
        win_sum = value1 + value2
        if option == 1:
            if win_sum >= 2 and win_sum <= 6:
                print('You won\nTrial is over!!')
            else:
                print('You lost\nTrial is over!!')
        elif option == 2:
            if win_sum == 7:
                print("You won\nTrial is over!!")
            else:
                print('You lost\nTrial is over!!')
        elif option == 3:
            if win_sum >= 8 and win_sum <= 12:
                print("You won\nTrial is over!!")
            else:
                print('You lost\nTrial is over!!')
Bounty = str(input('Would you like to get Bounty tries for 50$ ? (y-Yes/n-No)y'))
if Bounty == 'y':
    Bounty_count = int(input('Enter the number of bounty tries you want (Your balance:'+str(default_amount)+'$) :'))
    DICE_def.validate(default_amount, Bounty_count)
    if DICE_def.validate:
        default_amount -= (Bounty_count*50)
        while Bounty_count != 0:
            roll = str(input("Press r-roll q-quit:\n"))
            if roll == "r":
                bet_amt = int(input('How much would you like to bet?'))
                if bet_amt > default_amount:
                    print("You don't have enough money")
                    continue
                print("Choose the sum:\n1.(2-6)\n2.(7)\n3.(8-12)\n")
                option = int(input('Place your bet!!:'))
                value1 = random.randint(1, 6)
                value2 = random.randint(1, 6)
                DICE_def.dice(value1)
                DICE_def.dice(value2)
                win_sum = value1 + value2
                if option == 1:
                    if win_sum >= 2 and win_sum <= 6:
                        print("You won " + str(2 * bet_amt) + '$ !!')
                        default_amount += (2 * bet_amt)
                    else:
                        print("You lost :(")
                elif option == 2:
                    if win_sum == 7:
                        print("You won " + str(2 * bet_amt) + '$ !!')
                        default_amount += (2 * bet_amt)
                    else:
                        print("You lost :(")
                elif option == 3:
                    if win_sum >= 8 and win_sum <= 12:
                        print("You won " + str(2 * bet_amt) + '$ !!')
                        default_amount += (2 * bet_amt)
                    else:
                        print("You lost :(")
                print("\nAccount Balance:" + str(default_amount) + "$\n\n")
                Bounty_count-=1
                print('Bounty tries remaining:'+str(Bounty_count))
            elif (roll == "q"):
                break
            else:
                print('Enter valid input')

    else:
        print("Not enough dollars")

while 1 and Bounty_count == 0:
    roll = str(input("Press r-roll q-quit:\n"))
    if roll == "r":
            bet_amt = int(input('How much would you like to bet?'))
            if bet_amt>default_amount:
               print("You don't have enough money")
               continue
            print("Choose the sum:\n1.(2-6)\n2.(7)\n3.(8-12)\n")
            option = int(input('Place your bet!!:'))
            value1 = random.randint(1, 6)
            value2 = random.randint(1, 6)
            DICE_def.dice(value1)
            DICE_def.dice(value2)
            win_sum=value1+value2
            if option==1:
                if win_sum>=2 and win_sum<=6:
                    print("You won "+str(2*bet_amt)+'$ !!')
                    default_amount += (2*bet_amt)
                else:
                    print("You lost "+str(bet_amt)+"$ :(")
                    default_amount -= bet_amt
            elif option==2:
                if win_sum==7:
                    print("You won " + str(2 * bet_amt) + '$ !!')
                    default_amount += (2 * bet_amt)
                else:
                    print("You lost " + str(bet_amt) + "$ :(")
                    default_amount -= bet_amt
            elif option==3:
                if win_sum>=8 and win_sum<=12:
                    print("You won " + str(2 * bet_amt) + '$ !!')
                    default_amount += (2 * bet_amt)
                else:
                    print("You lost " + str(bet_amt) + "$ :(")
                    default_amount -= bet_amt
            print("Account Balance:"+str(default_amount)+"$\n\n")
            if default_amount == 0:
                print('You have no money left!!')
                break
    elif(roll=="q"):
        break
    else:
        print('Enter valid input')


