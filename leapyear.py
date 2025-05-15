year=int(input("Enter a year to check if it a leap year or not: "))
if(year%4==0 and year%100!=0) or (year%400==0):
    print("It\'s a leap year")
else:
    print("It\'s Not a leap year")