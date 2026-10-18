from functools import reduce

employees = [
    {"name": "Thanush", "department": "IT", "salary": 30000},
    {"name": "Nani", "department": "HR", "salary": 25000},
    {"name": "Kushal", "department": "IT", "salary": 40000}
]
# Select IT employees
it_employees = list(filter(
    lambda e: e["department"] == "IT", employees
))
# Increase salary by 10%
new_employees = list(map(
    lambda e: {
        "name": e["name"],
        "department": e["department"],
        "salary": e["salary"] * 1.10
    },
    it_employees
))
print("Employees after salary hike:")
for e in new_employees:
    print(e)

# Calculate total salary
total = reduce(
    lambda a, e: a + e["salary"],
    new_employees,
    0
)

print("Total salary:", total)

'''
Output:
Employees after salary hike:
{'name': 'Thanush', 'department': 'IT', 'salary': 33000.0}
{'name': 'Kushal', 'department': 'IT', 'salary': 44000.0}
Total salary: 77000.0
'''
