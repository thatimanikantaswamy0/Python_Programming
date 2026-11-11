def my_function(year):
    if year%4==0 and year%100!=0 or year%400==0:
        return "leap year"
    else:
        return "not leap year"
year=int(input("enter the year:"))
print(my_function(year))