# Task 6
# asks the user to input a number
def user_num():
    while True:
        try:
            z = int(input("Enter a number :"))
        except ValueError:
            print("Enter a whole number!")
            print()
            continue
        else:
            return z


""""sees if "n" is a multiple of 3 - if it is, it will run to see if it is 21, 24 or 27 and if it is will keep the 
    value the same, but if any other multiple of 3 will set the value to 0 """
def fix_three(n):
    if n % 3 == 0:
        if n < 20 or n > 29:
            n = 0
    return n


# runs a, b, c through the helper function fix_three() and then add them together
def no_three_sum(a, b, c):
    a = fix_three(a)
    b = fix_three(b)
    c = fix_three(c)
    sum1 = str(a + b + c)
    print()
    print("Sum of a, b, c is " + sum1)


# Uses the user_num function the set the arguments in no_three_sum a, b, c
no_three_sum(user_num(), user_num(),user_num())

# Stops the window from closing upon finishing
print("")
input("Press any button to exit!")



