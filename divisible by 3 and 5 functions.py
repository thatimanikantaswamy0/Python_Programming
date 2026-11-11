def my_function(n):
    if n%3==0 and n%5==0:
        return "divisible by both 3 and 5"
    elif n%3==0:
        return "divisible by only 3"
    elif n%5==0:
        return "divisible by only 5"
    else:
        return "not divisible by both 3 and 5"
n=int(input("enter the number:"))
print(my_function(n))