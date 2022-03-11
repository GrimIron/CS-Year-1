import string
from collections import Counter
cf = open("guessing_game.py")

"""Creates a new empty value, the separates the program chosen into words then letters. From there is separates the
   a - z letters from the file and sets them to lowercase then adds it to the new value as a string. Then runs through
   the Counter collection and prints"""
def cal_frequency(file):
    new_string = []
    for word in file:
        for letter in word:
            if letter in string.ascii_letters:
                letter_lower = letter.lower()
                new_string += letter_lower
    frequency = Counter(new_string)
    frequency = dict(frequency)
    print(frequency)


(cal_frequency(cf))

# Stops the window from closing upon finishing
print("")
input("Press any button to exit!")