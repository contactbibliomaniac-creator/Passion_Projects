def name():
    userInput = input("What's your name?")
    return userInput.upper()
def age():
    return input("What is your age?")
names = name()
ages = age()
print (f"Hello {names} You are {ages} years old")