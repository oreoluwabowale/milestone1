print("The Leap year program".center(30))
year = int(input("Please enter a year: "))

if year % 4 == 0 and year % 100 == 0 :
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
