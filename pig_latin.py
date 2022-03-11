# Task 4
"""" Sets 'ay' to a empty array and asks the user for a input. It then sets the input to lowercase and spits it. It
     spits them in to a list. Then it selects the first letter from the word and puts it on the end of the word
     e.g 'hello' to 'elloh' and then adds 'ay' to the end e.g 'ellohay' and appends it to the array 'ay' then joins the
     words in 'ay' together with a single space """
def pig_latin():
    ay = []
    user_input = str(input("Please enter you sentence: "))

    user_input = user_input.lower().split()

    for words in user_input:
        piglatin = words[1:] + words[0]
        piglatin += "ay"
        ay.append(piglatin)

    answer = " ".join(ay)

    print(answer)


pig_latin()

# Stops the window from closing upon finishing
print("")
input("Press any button to exit!")
