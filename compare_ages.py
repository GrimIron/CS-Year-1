# Task 2
""" Sets my_age to a value and asks the user to input there age, if there is no error, it will check there answer verses
    my_age if its the same it will print out that it is the same, if not will state how many years older/ younger they
    are """
def compare_ages():
    my_age = 24
    while True:
        try:
            user_age = int(input("What is your age? : "))
        except ValueError:
            print("Try again, but enter a whole number")
            print()
        else:
            if user_age == my_age:
                print("You are my age! ")
            elif user_age < my_age:
                user_age1 = str(my_age - user_age)
                print("You are younger than me by " + user_age1 + " year(s)")
            elif user_age > my_age:
                user_age2 = str(user_age - my_age)
                print("You are older than me by " + user_age2 + " year(s)")
            print()


compare_ages()

# Stops the window from closing upon finishing
print("")
input("Press any button to exit!")
