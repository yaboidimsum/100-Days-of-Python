#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_words = pd.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter:row.code for (index, row) in nato_words.iterrows()}
# print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
output = [phonetic_dict[letter] for letter in word]

print(output)
