print("Welcome to palindrome checker!")
# input
string1 = input("Enter your word: ")
# variables
stringList = []
string = ""

# appends each letter in the string to a list
for letters in string1:
    stringList.append(letters)
# reverses list so it is backwards
stringList.reverse()

# adds each letter to a string
for letters in stringList:
    string += letters

# if the word backwards is the same as it is in normal form:
if string == string1:
    print("Yor word is a palindrome!")
else:
    print(string1 + " is not a palindrome.")

print(string)
