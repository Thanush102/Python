#Square function
square=lambda n:n*n
print("Square of 5 is",square(5))  

print()
#Positive number check
is_even=lambda n:n%2==0;
print("14 is Even:",is_even(14))   

#Larger of two nums
print()
larger=lambda a,b:b if a<b else a;
print("Largest number in 15,49 is",larger(15,49)) 

"""
Output:
Square of 5 is 25

14 is Even: True

Largest number in 15,49 is 49
"""
