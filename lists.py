albums = ["Lover", "Reputation", "1989", "Red", "Speak Now", "Fearless"]

#pwede rin mixed var types in one like
#albums = ["Red", 5, True] (string, int, and bool in one list)

print(albums[0])

#to access index from the last element
print(albums[-1])

#to exclude certain elements kunwari ayaw ipakita ang 1st element us2 yung the rest 
print(albums[1:])

#choosing range of elements
print(albums[1:5])

#to change values of list 
albums[2] = "1989 TV"
print(albums[0:6])