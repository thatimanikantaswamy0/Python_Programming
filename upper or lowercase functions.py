def my_function(c):
    if c>='A'and c<='Z':
        return "uppercase alphabet"
    elif c>='a'and c<='z':
        return "lowercase alphabet"
    else:
        return "not an alphabet"
c=input("enter the character:")
print(my_function(c))