word = str(input("Enter text with at least 2 H's: "))
h1 = word.find("h")
h2 = word.rfind("h")
word2 = word[h1:h2]
word3 = word2[::-1]
word4 = word[:h1+1]
word5 = word[h2-1:]
print(word4+word3+word5)
