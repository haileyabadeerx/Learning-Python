le_word = "Hu Tao"

def ask_input():
    guess = input("Enter your guess: ")

ask_input()

guess = ""
guess_limit = 3
guess_count = 0

while guess.lower() != le_word.lower() and guess_limit != 0 :
    print("Oops, try again.")
    print(str(guess_limit) + " attempts remaining.")
    guess_limit -= 1
    got_it = False
    ask_input()
    
if got_it == False:
    print("Sorry, you ran out of attempts.")
else:
    print("Congratulations! You know my favorite character.")
