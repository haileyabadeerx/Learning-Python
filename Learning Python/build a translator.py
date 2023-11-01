def translate(phrase):
    translation = ""

    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "meow"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter something to translate: ")))