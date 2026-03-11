word1 = str(input("Enter text with atleast 2 h's: "))
h1 = word1.find("h")
h2 = word1.rfind("h")
word2 = word1[h1+1:h2]
word3 = word2.replace("h","H")
word4 = word1[:h1+1]
word5 = word1[h2:]
print(word4+word3+word5)
