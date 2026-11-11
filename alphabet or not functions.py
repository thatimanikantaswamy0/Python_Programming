def my_function(c):
    if c>='A'and c<='Z' or c>='a'and c<='z':
        return "alphabet"
    else:
        return "not alphabet"
c=input("enter the character:")
print(my_function(c))