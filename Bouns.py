
## Bonus (Not required), create a new python file and do the following:

#- Define a string variable containing a sentence with at least 10 words.
string_ten_words="First 2nd 3rd 4rd 5th 6th 7th 8th 9th 10th"

#- Define a string variable containing a word that appears in the sentence.
search_word="5th"

#- Print the length of the sentence.
print(len(string_ten_words))

#- Print the index of the first occurrence of the word in the sentence.
print(string_ten_words.index(search_word))

#- Print the number of times the word appears in the sentence.
print(string_ten_words.count(search_word))

#- Print the sentence in all uppercase letters.
print(string_ten_words.upper())

#- Print the sentence in all lowercase letters.
print(string_ten_words.lower())

#- Replace the word in the sentence with a new word of your choice.

string_ten_words=string_ten_words.replace(search_word,"NewWord")
#- Print the last character of the sentence.

print(string_ten_words[-1])