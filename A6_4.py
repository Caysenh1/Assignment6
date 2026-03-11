words = str(input("Enter two words: "))
wordn = words.index(" ")
worda = words[:wordn]
wordb = words[wordn:]
print(wordb,worda)
