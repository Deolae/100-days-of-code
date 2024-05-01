#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# Import libraries
import pandas as pd

# Read the csv of NATO code words
nato_df = pd.read_csv("nato_phonetic_alphabet.csv")

# Make dictionary for NATO code words
nato_dict = {row.letter:row.code for (index, row) in nato_df.iterrows()}

# Take word from user
user_word = input("Enter a word: ").upper()

# Compare to the letters in the dict and get the corresponding code
nato_list_user = [nato_dict[letter] for letter in user_word]

# Print the phonetic alphabet list for the word
print(nato_list_user)
