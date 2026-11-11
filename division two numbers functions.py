def my_function(n1,n2):
    if n2==0:
        return "error! division not possible"
    else:
        div=n1/n2
        return f"division two numbers ={div}"
n1=int(input("enter the first number:"))
n2=int(input("enter the second number:"))
print(my_function(n1,n2))