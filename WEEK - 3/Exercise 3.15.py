str = input("Enter a sentende: ")
arr=str.lower()
vowels=0
consonents = 0
digits=0
spaces=0
n=len(str)
for i in range(n):
    if arr[i].isalpha():
        if arr[i] in {'a','e','o','i','u'}:
            vowels+=1
        else:
            consonents+=1
    elif arr[i].isdigit():
        digits+=1
    elif arr[i] in {' '}:
        spaces+=1
print("No. of Vowels =",vowels)
print("No. of Consonentss =",consonents)
print("No. of Digits =",digits)
print("No. of Spaces =",spaces)


#output
#Enter a sentende: grzjtxkyulil;iou;ytc
#No. of Vowels = 5
#No. of Consonentss = 13
#No. of Digits = 0
#No. of Spaces = 0
