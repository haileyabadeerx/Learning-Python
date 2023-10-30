le_word = "Hu Tao"
guess = ""
guess_limit = 3
guess_count = 0

while guess != guess_lower:
    guess = input("Enter your guess: ")
    guess_lower = guess.lower()
    if guess != guess_lower:
        print("Oops, try again.")
        print(str(guess_limit - 1) + "attempts remaining.")
        guess_limit -= 1


print("Congratulations! You know my favorite character.")
