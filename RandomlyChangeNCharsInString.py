import random
import string

# Method to change N characters from a string with random characters.
def randomly_change_n_char(word, value):
    length = len(word)
    word = list(word)
    # This will select the two distinct index for us to replace
    k = random.sample(range(0,length),value)
    for index in k:
        # This will replace the characters at the specified index with
        # the generated characters
        word[index] = random.choice(string.ascii_lowercase)
    # Finally print the string in the modified format.
    print("" . join(word))

# Get the string to be modified
string_to_modify = raw_input("Enter the string to be replaced...\n")

# get the number of places that needed to be randomly replaced
total_places = input("Enter the total places that needs to be modified...\n")

# Function to replace 'n' characters at random
randomly_change_n_char(string_to_modify, total_places)