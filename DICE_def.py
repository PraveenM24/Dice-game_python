#This contains the functions for the Main game
s= "+- - - -+"
m1="| o   o |"
m2="| o     |"
m3="|   o   |"
m4="|     o |"
m5="|       |"

#This function is used to determine the dice phase based on the random value
def dice(choice):
    if choice == 1:
        print(s + "\n" + m5 + "\n" + m3 + "\n" + m5 + "\n" + s)
    elif choice == 2:
        print(s + "\n" + m5 + "\n" + m1 + "\n" + m5 + "\n" + s)
    elif choice == 3:
        print(s + "\n" + m2 + "\n" + m3 + "\n" + m4 + "\n" + s)
    elif choice == 4:
        print(s + "\n" + m1 + "\n" + m5 + "\n" + m1 + "\n" + s)
    elif choice == 5:
        print(s + "\n" + m1 + "\n" + m3 + "\n" + m1 + "\n" + s)
    elif choice == 6:
        print(s + "\n" + m1 + "\n" + m1 + "\n" + m1 + "\n" + s)

#This function is used to check whether the user's account balance is sufficient to get the Bounty tries        
def validate(d_amount,count):
    c_amount=50*count
    if d_amount<c_amount:
        return False
    else:
        return True
