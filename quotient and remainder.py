n1=int(input("enter the dividend value:"))
n2=int(input("enter the divisor value:"))
if n2==0:
    print("error! quotient and remainder not possible")
else:
    quo=n1/n2
    rem=n1%n2
    print("quotient =",quo)
    print("remainder =",rem)