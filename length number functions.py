def my_function(n,count):
    while n>0:
        digit=n%10
        count+=1
        n//=10
    return count
n=int(input("enter the number:"))
count=0
print("length number =",my_function(n,count))