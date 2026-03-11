word = str(input("Enter your  name: "))
wordsp = word.find(" ")
word2 = word[wordsp+1:]
wordluke = word[:wordsp] 
wordC = wordluke.capitalize()
word2C = word2.capitalize()
print(wordC)
print(word2C)
print(f"My first name is {wordC} and my last name is {word2C}.")
