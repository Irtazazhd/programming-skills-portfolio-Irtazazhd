# Given list
list1 = [5, 10, 15, 20, 25, 50, 20]

# Find the value 20 and replace it with 200 (only the first occurrence)
if 20 in list1:
    index = list1.index(20)
    list1[index] = 200

# Printing the updated list
print("Updated list:", list1)
