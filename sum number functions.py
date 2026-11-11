def my_function(n,add):
    while n>0:
        digit=n%10
        add+=digit
        n//=10
    return add
n=int(input("enter the number:"))
add=0
print("sum number =",my_function(n,add))