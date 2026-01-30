import pandas

#TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data.to_dict())
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Please enter a word: ").upper()
result = [phonetic_dict[letter] for letter in user_word]
# user_letters = list(user_word)

# user_letter_code = {}
# for (index, row) in data.iterrows():
#     if row.letter in user_letters:
#         user_letter_code[row.letter] = row.code

# user_letter_code = {row.letter: row.code for (index, row) in data.iterrows() if row.letter in user_letters}
print(result)