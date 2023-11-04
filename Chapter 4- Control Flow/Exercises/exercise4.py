# Set the age of the person
age = 25  # You can change this value to test different outcomes

# If-elif-else chain to determine the stage of life
if age < 2:
    print("This person is a baby.")
elif age < 4:
    print("This person is a toddler.")
elif age < 13:
    print("This person is a kid.")
elif age < 20:
    print("This person is a teenager.")
elif age < 65:
    print("This person is an adult.")
else:
    print("This person is an elder.")

age = 1
# Corresponding if-elif-else chain
# Output: "This person is a baby."

age = 3
# Corresponding if-elif-else chain
# Output: "This person is a toddler."

age = 10
# Corresponding if-elif-else chain
# Output: "This person is a kid."

age = 15
# Corresponding if-elif-else chain
# Output: "This person is a teenager."

age = 30
# Corresponding if-elif-else chain
# Output: "This person is an adult."

age = 70
# Corresponding if-elif-else chain
# Output: "This person is an elder."
