import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

def generate_phonetic():
    user_word = input("Please enter a word: ").upper()
    try:
        result = [phonetic_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters A-Z are allowed. Try again.")
        generate_phonetic()
    else:
        print(result)

generate_phonetic()