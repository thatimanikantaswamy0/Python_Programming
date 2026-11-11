n=int(input("enter the number:"))
add=0
while n>0:
    digit=n%10
    add+=digit
    n//=10
print("sum number =",add)