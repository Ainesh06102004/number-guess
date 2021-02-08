import random


compnumber = random.randint(0,9)

print("Guess a number between 0 and 9, Good luck :)")

usernumber = int(input("Enter your number: "))

if(usernumber > 9 or usernumber < 0):
    print("Enter a number between 0 and 9")

if(usernumber >= 0 and usernumber <= 9):
    if (compnumber == usernumber):
        print("Congratulations! You've Won")    
    else:
        print("Oops! Try again")