userInput1 = input("Please input first name: ")
userInput2 = input("Please input last name: ")
print(f"Your full name is {userInput1} {userInput2}")

# Refactoring
fullName = f"{userInput1} {userInput2}".upper()
print(f"Your full name is {fullName}")

# Alternative f'notion'
print("Your full name is {}".format(fullName))