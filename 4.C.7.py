student_marks = {
    "Thanush": 85,
    "Nani": 92,
    "Kushal": 78,
    "Sahith": 90
}

print("Original Dictionary:", student_marks)

removed_val = student_marks.pop("Sahith")
print(f"\nRemoved 'Charan' with score: {removed_val}")
print("Dictionary after pop():", student_marks)

missing_key = "Charan"
safe_value = student_marks.get(missing_key,"Not Found")

print(f"\nAttempted to access '{missing_key}': {safe_value}")
print("Dictionary remains unchanged:", student_marks)

#OUTPUT
#Original Dictionary: {'Thanush': 85, 'Nani': 92, 'Kushal': 78, 'Sahith': 90}

#Removed 'Charan' with score: 90
#Dictionary after pop(): {'Thanush': 85, 'Nani': 92, 'Kushal': 78}

#Attempted to access 'Charan': Not Found
#Dictionary remains unchanged: {'Thanush': 85, 'Nani': 92, 'Kushal': 78}
