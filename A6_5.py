word = str(input("Enter input with atleast two H's: "))
splice1 = word.find("h")
splice2 = word.rfind("h")+1
splice3 = word[:splice1]
splice4 = word[splice2:]
print(splice3+splice4)

