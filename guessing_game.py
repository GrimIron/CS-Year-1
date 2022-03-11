# Task 3
""" Sets a random number between 1 - 100 and sets guesses to 1, then asks the user to input a number guess between 1 -
    100. If the guess is the same it will return that it is correct and how many guesses they took. If not correct it
    will print whether the answer is to big or small adding 1 to the guesses each time they take a guess"""
def guessing_game():
    import random
    ans = random.randint(1, 100)
    guesses = 1
    print("Welcome to the Guessing Game!\n")

    while True:
        try:
            guess = int(input("Please enter a number between 1 and 100 : "))
        except ValueError:
            print("Try again, but enter a whole number!\n")
        else:
            if guess > 100:
                print("The number is between 1 - 100\n")
            else:
                if ans < guess:
                    print("That's not right " + str(guess) + " is too big!\n")
                    print()

                elif ans > guess:
                    print("That's not right " + str(guess) + " is too small!\n")
                    print()

                elif ans == guess:
                    print("That's right!\n" + "\n" + "You took " + str(guesses) + " guess(es)!\n")
                    return

                guesses += 1


guessing_game()

# Stops the window from closing upon finishing
print("")
input("Press any button to exit!")
