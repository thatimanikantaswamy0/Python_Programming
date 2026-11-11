n1=int(input("enter base value:"))
n2=int(input("enter exponent value:"))
power=1
for i in range(n2):
    power*=n1
print("power number =",power)