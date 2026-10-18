def  student_info(name, roll_no, branch):
    print("Name:",name)
    print("Roll No:",roll_no)
    print("Branch:",branch)
print("Positional Argument")    
student_info("Thanush","11111","CSE")
print()

print("Keyword Argument")
student_info(name="Thanush",roll_no="11111",branch="CSE")

'''
Output:
Positional Argument
Name: Thanush
Roll No: 11111
Branch: CSE

Keyword Argument
Name: Thanush
Roll No: 11111
Branch: CSE
'''
