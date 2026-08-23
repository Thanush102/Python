c = input("enter the character:")
if c.isalpha():
    c_lower = c.lower()
    if c_lower in {'a','e','i','o','u'}:
        print(c,"is a vowel")
    else:
        print(c,"is a consonant")
elif c.isdigit():
    print(c,"is a digit")
else:
    print(c,"is a special character")

#output
#enter the character:e
#e is a vowel
