employees = {
    "employee01": {
        "name": "Thanush",
        "department": "Engineering",
        "salary": 85000
    },
    "employee02": {
        "name": "Nani",
        "department": "Marketing",
        "salary": 75000
    },
    "employee03": {
        "name": "Kushal",
        "department": "Finance",
        "salary": 80000
    }
}
for emp_id, info in employees.items():
    print(f"ID: {emp_id}")
    print(f"  Name: {info['name']}")
    print(f"  Department: {info['department']}")
    print(f"  Salary: ${info['salary']:,}")
    print("-" * 25)

#output
#    ID: employee01
#  Name: Thanush
#  Department: Engineering
#  Salary: $85,000

#ID: employee02
#  Name: Nani
#  Department: Marketing
#  Salary: $75,000

#ID: employee03
#  Name: Kushal
#  Department: Finance
#  Salary: $80,000
-------------------------

