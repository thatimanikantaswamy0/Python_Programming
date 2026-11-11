def my_function(c):
    if c.isalpha():
        return "alphabet"
    else:
        return "not alphabet"
c=input("enter the character:")
print(my_function(c))