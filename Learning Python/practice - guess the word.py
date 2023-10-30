le_word = "Hu Tao"

def ask_input():
    guess = input("Enter your guess: ")
    guess_lower = guess.lower()

guess = ""
guess_lower = ""
guess_limit = 3
guess_count = 0

while guess != guess_lower:
    print("Oops, try again.")
    print(str(guess_limit - 1) + "attempts remaining.")
    guess_limit -= 1
    ask_input()

print("Congratulations! You know my favorite character.")
