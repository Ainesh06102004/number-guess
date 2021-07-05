import random

print("Guessing Game ")
print("Guess A Number Between 1 To 9")

chances = 0

number = random.randint(1, 9)

while chances < 5:
    guess = int(input("Enter The Guessed Number : "))

    if guess == number:
        print("Congratulation You Won The Game :)")
        break

    elif guess < number:
        print("Your Guess Was Too Low. Guess A Number Higher Than", guess)

    else:
        print("Your Guess Was Too High. Guess A Number Lower Than", guess)

    chances += 1

    if not chances < 5:
        print("You Lose !!! The Number Is", number, "Try Again :)")
