def my_function(c):
    if c.isupper():
        return "uppercase alphabet"
    elif c.islower():
        return "lowercase alphabet"
    else:
        return "not an alphabet"
c=input("enter the character:")
print(my_function(c))