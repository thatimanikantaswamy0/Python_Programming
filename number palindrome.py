n=int(input("enter the number:"))
reverse=0
original=n
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n//=10
if reverse==original:
    print("palindrome")
else:
    print("not palindrome")