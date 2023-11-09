le_word = "Hu Tao"

guess_limit = 3

print("Can you guess my FAVORITE GENSHIN IMPACT CHARACTER?")

while guess_limit >= 0:
    guess = input("Enter your guess: ")

    if guess.lower() != le_word.lower() and guess_limit != 0:
        print("Oops, try again.")
        print(str(guess_limit) + " attempts remaining.")
        guess_limit -= 1
    else:
        break
    
if guess_limit == 0 and guess.lower() != le_word.lower():
    print("Sorry, you ran out of attempts.")   
else:
    print("Congratulations! You know my favorite character.")