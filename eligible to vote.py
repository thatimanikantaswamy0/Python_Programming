age=int(input("enter the age:"))
if age>=18:
    print("person eligible to vote")
else:
    print(f"person not eligible to vote he needs {18-age} more years to vote")