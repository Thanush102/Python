grade = lambda marks: "Pass" if marks >= 40 else "Fail"

marks_list = [85, 35, 60, 25, 40, 90]

for marks in marks_list:
    print(marks, "-", grade(marks))

'''
Output:
85 - Pass
35 - Fail
60 - Pass
25 - Fail
40 - Pass
90 - Pass
'''
