import random
lives = 3
words = ["wonderful","cry","fly","chacteristic","consequence", "extreme","query","marvalous"]
compword = random.choice(words)
cCompwWord = compword.upper()
guessedletters = set()
while (lives > 0):
    userInput1 = input("What letter do you guess?")
    guessedletters.add(userInput1)
    print(guessedletters)
    print(cCompwWord)
    lives = lives - 1
if guessedletters == cCompwWord:
    print("Yay, you guessed a letter correctly!")