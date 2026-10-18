def is_even(n):
        return n%2==0
n=5
list=list(map(int,input("enter list").split()))
for i in list:
    print(f"{i} is even: {is_even(i)}")

'''
Output:
enter list23 45 100 57 79
23 is even: False
45 is even: False
100 is even: True
57 is even: False
79 is even: False
'''
