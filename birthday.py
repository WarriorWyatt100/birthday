from datetime import date
import time


months = ["January","Febuarary","March","April","May","June","July","August","September","October","November","December"]
day = input("Enter your birth day: ")
month = input("Enter your birth month: ")
year = input("Enter your birth year: ")

for i in range(12):
    num = str(i+1)
    if (month == num):
        month = months[i]

print("You were born on: ", month, day, year)
print("THATS CRAZY!")

age = input("What's your age????: ")
print("Oh wow....")
time.sleep(1)
print("You're old")
time.sleep(1)
quiery = input("You wanna know the date?! ")
if(quiery == "yes") or (quiery == "sure") or (quiery == "Yes") or (quiery == "Sure"):
    print("Today's date is!")
    for i in range(4):
        print("...")
        if(i==3):
            print("the anticipation...")
        time.sleep(1)
    today = date.today()
    print(today)
else:
    print("oh..... ok.... goodbye then :L")