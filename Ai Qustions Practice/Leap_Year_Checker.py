# Check Whether a Year is Leap or Not
# CODE BY LUCKY

year = int(input("Enter Year : "))

if year % 400 == 0:
    print(year, "is a Leap year!")
elif year % 100 == 0:
    print(year, "is not a Leap year")
elif year % 4 == 0:
    print(year, "is a Leap year!")
else:
    print(year, "is not a Leap year")
