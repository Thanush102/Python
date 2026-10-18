def power(base, exp):
    if exp==0:
        return 1
    elif exp>0:
        return base*power(base, exp-1)
    elif exp<0:
        exp*=-1
        return 1/(base*power(base, exp-1))
print("100 power 1 is",power(100,1))

"""
Output:
100 power 1 is 100
"""
