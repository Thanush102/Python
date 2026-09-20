import re

sentence = "1024 requests were served in 3 seconds"

result = re.match(r"\d", sentence)
print("Starts with digit:", bool(result))

result = re.search(r"served", sentence)
print("Position of served:", result.span())

result = re.fullmatch(r"\d+", "12345")
print("12345 contains only digits:", bool(result))

result = re.fullmatch(r"\d+", "123a5")
print("123a5 contains only digits:", bool(result))

#output:
#Starts with digit: True
#Position of served: (19, 25)
#12345 contains only digits: True
#123a5 contains only digits: False  '''
