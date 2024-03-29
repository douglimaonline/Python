# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#

# student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
# Access index and row
# Access row.student or row.score
# pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
letters_code = {row.letter: row.code for (index, row) in data.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def NATO_alphabet():
    try:
        word_list = list(input("Type a name: "))
        phonetic_list = [letters_code[letter.upper()] for letter in word_list]
        print(phonetic_list)
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        NATO_alphabet()


NATO_alphabet()
