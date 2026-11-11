def my_function(n,reverse):
    while n>0:
        digit=n%10
        reverse=reverse*10+digit
        n//=10
    return reverse
n=int(input("enter the number:"))
reverse=0
original=n
if my_function(n,reverse)==original:
    print("palindrome")
else:
    print("not palindrome")