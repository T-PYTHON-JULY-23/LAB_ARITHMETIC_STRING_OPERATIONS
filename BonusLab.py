
ten_fruits = "AppleOrangeKiwiBananaPeachPapayaStrawberrieWatermelonLemonMango"

fruit = "Mango"
newWord = "Hi"
 
ten_fruitsLen = len(ten_fruits)
print("The length of the sentence:",ten_fruitsLen)

mango_apear = ten_fruits.index(fruit)
print("The index of the first occurrence of the word in the sentence:",mango_apear)

time_apear = ten_fruits.count(fruit)
print("The number of times the word appears in the sentence:",time_apear)

print("The sentence all lowerupper:",ten_fruits.upper())

print("The sentence all lowercase:",ten_fruits.lower())

cutWord = ten_fruits[:58]
reword = f"{cutWord}{newWord}"
print("The sentence after replacing the word with new one:",reword)

print("Last character of the sentence after replacement:",reword[-1])