word=input("    Enter a word  ")
s = ''
length = len(word) - 1

while length>=0:
    s = s + word[length]
    length = length - 1

print("  The reverse of the entered word is: ",s)    