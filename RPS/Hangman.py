def hangman():
    import random
    import time
    print("Welcome to Hangman!")
    print("loading...")
    print("IMPORTANT: Always enter lowercase letters.")
    time.sleep(1.5)
    word_choices=["february","wednesday","rhythm","happened","babies","eighteen","promise","rhyme","destruction","tornado"]
    word=random.choice(word_choices)
    word_choices=list(word)
    user_input_list=[]
    for i in range(len(word)):
        user_input_list.append(" ")
    length=len(word)*"_ "
    print(length)
    lives=5
    user_list=[]
    while lives > 0:
        print()
        user_input=input("Guess a letter:")
        print()
        user_list.append(user_input)
        if user_input in word:
            print("You guessed a letter!")
            for i in range(len(word)):
                if user_input==word_choices[i]:
                    user_input_list[i] = user_input
                else:
                    if user_input_list[i]=="a" or user_input_list[i]=="b" or user_input_list[i]=="c" or user_input_list[i]=="d" or user_input_list[i]=="e" or user_input_list[i]=="f" or user_input_list[i]=="g" or user_input_list[i]=="h" or user_input_list[i]=="i" or user_input_list[i]=="j" or user_input_list[i]=="k" or user_input_list[i]=="l" or user_input_list[i]=="m" or user_input_list[i]=="n" or user_input_list[i]=="o" or user_input_list[i]=="p" or user_input_list[i]=="q" or user_input_list[i]=="r" or user_input_list[i]=="s" or user_input_list[i]=="t" or user_input_list[i]=="u" or user_input_list[i]=="v" or user_input_list[i]=="w" or user_input_list[i]=="x" or user_input_list[i]=="y" or user_input_list[i]=="z":
                        user_input_list[i]=user_input_list[i]
                    else:
                        user_input_list[i] = "_"
        if len(user_input) >= 2:
            print()
            print(f"You have entered 2 or more characters.")
        if len(user_input) <= 0:
            print()
            print(f"You have entered nothing.")
        if len(user_list) != len(set(user_list)):
            print()
            print("You have entered some number of charecters twice. Please try again.")
            user_list=[]
        if user_input.isalpha() == False and len(user_input)!=0:
            print()
            print("You have entered a character that is not a letter. Please try again.")
        if user_input not in word and len(user_input)==1 and user_input.isalpha()==True:
            lives=lives-1
            print()
            print(f"Sorry, the letter you have entered is not in the word.\nYou now have {lives} lives left.")
        print()
        print("This is your progress so far!")
        for k in range(len(user_input_list)):
            print(user_input_list[k], end=" ")
        if user_input_list==word_choices:
            print()
            print("Congrats! You win!")
            print()
            play_again=input("Would you like to play again? y/n")
            if play_again != "y":
                exit()
            else:
                hangman()  
    print("Sorry! You lost. :(")  
hangman()