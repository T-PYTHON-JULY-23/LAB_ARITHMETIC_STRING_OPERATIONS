#Define a string variable containing a sentence with at least 10 words.
name = "I am Sarah Alhamad, 20 years old, majoring in programming"

#Define a string variable containing a word that appears in the sentence.
firstName= "Sarah"

#Print the length of the sentence.
print(len(name))

#Print the index of the first occurrence of the word in the sentence.
print(name.index("I"))

#Print the number of times the word appears in the sentence.
print(name.count("a"))

#Print the sentence in all uppercase letters.
print(name.upper())

#Print the sentence in all lowercase letters.
print(name.lower())

#Replace the word in the sentence with a new word of your choice.
print(name.replace("Alhamad" , "Majed"))

#Print the last character of the sentence.
print(name[-1])