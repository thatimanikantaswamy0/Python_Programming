def my_function(n1,n2,n3):
    if n1<=n2 and n1<=n3:
        return n1
    elif n2<=n1 and n2<=n3:
        return n2
    else:
        return n3
n1=int(input("enter the first number:"))
n2=int(input("enter the second number:"))
n3=int(input("enter the third number:"))
print("smallest number =",my_function(n1,n2,n3))