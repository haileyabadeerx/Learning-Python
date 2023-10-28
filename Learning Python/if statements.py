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