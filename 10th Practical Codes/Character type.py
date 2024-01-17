character = input("Please enter a character to check: ")

if character.isupper():
    print("The character is uppercase")
elif character.islower():
    print("The character is lowercase")
elif character.isdigit():
    print("The character is a digit")
elif character.isspace():
    print("The character is a space")
else:
    print("The character is a special character")
