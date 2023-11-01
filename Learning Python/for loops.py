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

#tweakings with for loops
for index in range(5):
      if index == 0:
            print("The first iteration is 0")
      elif index == 1:
            print("The second iteration is 1.")
      elif index == 2:
            print("The third iteration is 2.")
      elif index == 3:
            print("The fourth iteration is 3")
      elif index == 4:
            print("The fifth iteration is 4.")
print("Even if the range is 5, it won't be printed")


