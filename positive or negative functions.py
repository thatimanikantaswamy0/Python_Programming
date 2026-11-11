def my_function(n):
    if n>0:
        return "positive number"
    elif n<0:
        return "negative number"
    else:
        return "equal to zero"
n=int(input("enter the number:"))
print(my_function(n))