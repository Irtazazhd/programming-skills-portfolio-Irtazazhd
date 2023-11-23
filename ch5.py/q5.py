# Define two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

# Merge dict2 into dict1 using dictionary unpacking
merged_dict = {**dict1, **dict2}

# Print the merged dictionary
print(merged_dict)
