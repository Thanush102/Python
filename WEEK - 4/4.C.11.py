String=input("Enter a string:")
char_counts = {}

for char in String:
    char_counts[char] = char_counts.get(char, 0) + 1

print("Original String:", String)
print("Character Frequencies:", char_counts)

#output
#Enter a string:thanush==7
#Original String: thanush==7
#Character Frequencies: {'t': 1, 'h': 2, 'a': 1, 'n': 1, 'u': 1, 's': 1, '=': 2, '7': 1}
