def my_function(age):
    if age>=18:
        return "person eligible to vote"
    else:
        return f"person not eligible to vote he needs {18-age} more years to vote"
age=int(input("enter the age:"))
print(my_function(age))