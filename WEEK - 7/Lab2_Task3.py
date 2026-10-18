def  total_marks(*marks):
    print(marks)
    total=sum(marks)
    average=total/len(marks)
    print("Total:",total)
    print("Average:",average)
total_marks(40,20,16)
total_marks(40,20,16,89,90)
total_marks(40)

'''
Output:
(40, 20, 16)
Total: 76
Average: 25.333333333333332
(40, 20, 16, 89, 90)
Total: 255
Average: 51.0
(40,)
Total: 40
Average: 40.0
'''
