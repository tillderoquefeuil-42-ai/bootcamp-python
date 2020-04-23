import sys
import random

nbr_try = 1
nbr = random.randint(1, 99)

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number. Type 'exit' to end the game.")
print("Good luck!\n")

user_try = input("What's your guess between 1 and 99?\n")
if user_try.isdigit():
    user_try = int(user_try)

while user_try != nbr:
    if user_try == "exit":
        print("Goodbye!")
        sys.exit(0)
    elif not type(user_try) is int:
        print("That's not a number.")
    else:
        if user_try > nbr:
            print('Too high!')
        if user_try < nbr:
            print('Too low!')

    nbr_try = nbr_try + 1
    user_try = input("What's your guess between 1 and 99?\n")
    if user_try.isdigit():
        user_try = int(user_try)


if nbr == 42:
    print("The answer to the ultimate question of life, the universe and everything is 42.")

if nbr_try == 1:
    print("Congratulations! You got it on your first try!")
else:
    print("Congratulations, you've got it!\nYou won in %d attempts!" % nbr_try)
