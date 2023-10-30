le_word = "Hu Tao"

def ask_input():
    guess = input("Enter your guess: ")

guess_limit = 3
got_it = False

while guess_limit != 0:
    guess = input("Enter your guess: ")

    if guess.lower() != le_word.lower():
        print("Oops, try again.")
        print(str(guess_limit) + " attempts remaining.")
        guess_limit -= 1
        ask_input()
    
if got_it:
    print("Sorry, you ran out of attempts.")
else:
    print("Congratulations! You know my favorite character.")
