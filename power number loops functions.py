def my_function(n1,n2,power):
    for i in range(n2):
        power*=n1
    return power
n1=int(input("enter base value:"))
n2=int(input("enter exponent value:"))
power=1
print("power number =",my_function(n1,n2,power))