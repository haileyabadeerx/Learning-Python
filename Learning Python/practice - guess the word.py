le_word = "Hu Tao"
guess = ""
guess_limit = 3
guess_count = 0

while guess != le_word:
    guess = input("Enter your guess: ")
    guess_lower = guess.lower()
    if guess != le_word:
        print("Oops, try again.")
        print(guess_limit - 1 + "attempts remaining.")


print("Congratulations! You know my favorite character.")
