#Command to run: python lab1.py 
print("Palindrome Test")
print("Capitalization doesn't matter, spaces and punctuation does.")
word = input("Enter a word: ")
word = word.lower()
reverse = word[::-1]
if word == "":
    print("Nothing was entered.")
elif word == reverse:
    print(word + " is a palindrome.")
else:
    print(word + " is not a palindrome.")