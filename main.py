import random
import sys
from colorama import Fore, Style, init
from word_list import word_options
from json_modification import cleanup_data, track_word

#Here is where it initializes the terminal for colorama to work cross-OS
init()

#Here is where it will check that the user wants to play
def intro():
    first_response = input("\nWould you like to play Wordle: ").lower()
    
    if first_response in ["not now", "no", "n"]:
        print("\nAlright, maybe later\n")
        intro()
    elif first_response in ["yes", "yeah", "y"]:
        print("\nAlright, let's play!")
    else:
        print("\nThat is not one of the options, please choose yes or no\n")
        intro()

#Here is where the computer chooses its word
def computer(word_options):
    computer_choice = random.choice(word_options)
    return list(computer_choice)

#Here is where I create the string of the word for the user
def user(word_options):
    user_choice = input("\nTry a word: ").lower()
    if user_choice not in word_options:
        print("That is not a valid word")
        return user(word_options)
    else:
        return list(user_choice)

#Here is the list of the alphabet that will be motified by the available function
unused_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l","m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

#Here is where it will show the user what letters are still available to use
def available(user_choice):

    global unused_letters

    for a in user_choice:
        if a in unused_letters:
            unused_letters.remove(a)
    print("\nThese are the letters that you have not used:\n", unused_letters)

#Here is where we check if the user actually wins or loses
def check_win(computer_choice, user_choice):
    if user_choice == computer_choice:
        sys.exit(Fore.GREEN + "".join(user_choice) + Style.RESET_ALL + "\nYou have found the wordle!")
    else:
        letter_counts = {}
        for letter in computer_choice:
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
        
        result = [''] * len(user_choice)
        for i in range(len(user_choice)):
            if user_choice[i] == computer_choice[i]:
                result[i] = Fore.GREEN + user_choice[i] + Style.RESET_ALL
                letter_counts[user_choice[i]] -= 1
        
        for i in range(len(user_choice)):
            if result[i] == '': 
                if user_choice[i] in letter_counts and letter_counts[user_choice[i]] > 0:
                    result[i] = Fore.YELLOW + user_choice[i] + Style.RESET_ALL
                    letter_counts[user_choice[i]] -= 1
                else:
                    result[i] = user_choice[i]
        
        print(''.join(result))
    
    available(user_choice)

#Here is where they can try again
def guess_word(word_options, computer_choice):
    for attempt in range(6):
        user_choice = user(word_options)
        check_win(computer_choice, user_choice)
    sys.exit("\nUnfortunately, you have not gotten it. Thanks for playing!\nThe correct word was: " + "".join(computer_choice))

#Here is where I call the functions to actually happen
intro()
most_recent_words = cleanup_data()
computer_choice = computer(word_options)
if "".join(computer_choice) in most_recent_words:
    computer_choice = computer(word_options)
track_word(computer_choice)
guess_word(word_options, computer_choice)