def my_function(s):
    return s[::-1]
s=input("enter the string:")
if s==my_function(s):
    print("palindrome")
else:
    print("not palindrome")