le_word = "Hu Tao"

def ask_input():
    guess = input("Enter your guess: ")
    guess_lower = guess.lower()

ask_input()

guess = ""
guess_lower = ""
guess_limit = 3
guess_count = 0

while le_word.lower() != guess_lower and guess_count < 3 and guess_limit != 0 :
    print("Oops, try again.")
    print(str(guess_limit) + " attempts remaining.")
    guess_limit -= 1
    guess_count += 1
    got_it = False
    ask_input()
    
if got_it == False:
    print("Sorry, you ran out of attempts.")
else:
    print("Congratulations! You know my favorite character.")
