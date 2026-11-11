def my_function(n1,n2):
    temp=n1
    n1=n2
    n2=temp
    print("after swapping first number =",n1)
    print("after swapping second number=",n2)
n1=int(input("enter the first number:"))
n2=int(input("enter the second number:"))
print("before swapping first number =",n1)
print("before swapping second number =",n2)
my_function(n1,n2)