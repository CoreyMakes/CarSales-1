def Models():
    print("What kind of car are you looking for? ")
    Type = input()
    print("Let's take a look at some models that match  " + Type)
    


class Car:
     def __init__(self, year, make, model):
         self.year = year
         self.make = make
         self.model = model

year = int(input("What year is your car?  "))
make = input("What make is it?  ")
model = input("What model?  ")

print("Are you happy with your " + str(year) + " " + make + " " + model + "?")
answer = input()
if answer == "no":
    print("It might be time for a new one. Would you like to look at some new models?")
YesNo = input()
if YesNo == "no":
	Models()  
else:
if YesNo == "yes":
	Models()
    
    
if answer == "no":
    print("That's too bad. We would love to help you.")
