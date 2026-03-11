word = str(input("Enter a word of even length: "))
wordd = len(word)//2
wordf = word[:wordd]
wordg = word[wordd:]
print(wordg+wordf)
