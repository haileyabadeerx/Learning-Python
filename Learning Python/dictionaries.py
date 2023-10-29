
MidnightsTrack = {
    1: "Lavender Haze",
    2: "Maroon",
    3: "Anti-Hero",
    4: "Snow On The Beach (feat. Lana Del Rey) ",
    5: "You're On Your Own, Kid",
    6: "Midnight Rain",
    7: "Question...?",
    8: "Vigilante Shit",
    9: "Bejeweled",
    10: "Labyrinth",
    11: "Karma",
    12: "Sweet Nothing",
    13: "Mastermind",
}

print("This is a Midnights Album Tracker")
print("Press a number from 1-13 for your track.")

track = input("Enter here: ")

if track in MidnightsTrack:
    print(MidnightsTrack[track])
else:
    print("Track Number not in the album")