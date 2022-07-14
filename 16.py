#leap year
year=(input("enter the year\t"))
if (year%400) :
    print("year is leap year")
elif(year%100) :
    print("year is not leap year")
elif(year%4) :
    print("year is leap year")
else :
    print("year is not leap year")