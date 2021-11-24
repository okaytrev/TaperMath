import time

print ("---------------------------------------------")
print ("------      THE TAPER CALCULATOR       ------")
print ("---------------------------------------------")
print (" ")
print (" ")
weeks = int(input("How many weeks have you trained?:"))
print (" ")
print ("---------------------------------------------")
print (" ")
miles = int(input("How many miles have you ran?: "))
print (" ")
print ("---------------------------------------------")
print (" ")
difficulty = input("How difficult was your training (Easy, Med, Hard)?: ")
print (" ")
print ("---------------------------------------------")
print (" ")

if difficulty.lower() == "easy":
    percent = .6
elif difficulty.lower() == "med":
    percent = .50
elif difficulty.lower() == "hard":
    percent = .40

twoweek = ((miles / weeks) * 2) * percent

x=0
while x<50:
   print ("Calculating...") 
   x=x+1   
   time.sleep(.02)

print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print ("You ran " + str(miles) + " miles over the last " + str(weeks) + " weeks!")
print (" ")
print (" ")
print ("You should run " + str(twoweek) + " miles over the next 14 days of your training.")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")

x = 10
if (x > 1):
    print ("you are great")