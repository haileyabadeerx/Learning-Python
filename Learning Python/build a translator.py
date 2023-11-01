def translate(phrase):
    translation = ""

    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "Meow"
            else:
                translation = translation + "meow"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter something to translate: ")))