#this is how to declare basic for loop
#dito niloloop lang letters nung string dito
for  letter in "Honkai Star Rail":
    print(letter)

#for arrays
trailblazers = ["March 7th", "Dan Heng", "Stelle"]
for member in trailblazers:
    print(member)

#for numbers exclusive 10
for number in range(10):
        print(number)
#laging di kasama yung last number sa range
for number in range(2,15):
        print(number)

#can use range for arrays too
for member in range(len(trailblazers)): #<-- kinukuha length nung array
      print(trailblazers[member])