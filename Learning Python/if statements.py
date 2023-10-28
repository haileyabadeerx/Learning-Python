#simple if statements
is_single = True
is_broken = True

if is_single and is_broken:
    print("You are broken single")
elif not(is_single) and is_broken:
    print("Not single yet broken")
elif is_single and not(is_broken):
    print("Not broken yet single")
else:
    print("Woah, neither. Congrats!")

#with comparisons

def smallest(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c

print("Enter 3 numbers: ")
c = input()
a = input() 
b = input()
print("The smallest number is " + smallest(c, a, b))