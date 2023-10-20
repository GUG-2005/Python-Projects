# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
letters = data["letter"].to_list()
code = data["code"].to_list()

dict = {n:"" for n in letters}
n = 0
for i in dict:
    dict[i] = code[n]
    n += 1
inp = input("Enter a name to explore? ").upper()
result = []
try:
    letters = []
    for i in inp:
        letters.append(i)

    for i in letters:
        for j in dict:
            if i == j:
                result.append(dict[j])
except KeyError:
    print("Please enter text to move forward")
else:
    print(f"The Phonetic code for your name would be {result}")
