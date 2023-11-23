# Assuming numbers1 has 100 elements and numbers2 is an empty list
numbers1 = [i for i in range(100)]  # Example data for numbers1
numbers2 = []

# Copying the values from numbers1 to numbers2
for number in numbers1:
    numbers2.append(number)

# Now numbers2 contains all elements from numbers1
print("Contents of numbers2:", numbers2)
