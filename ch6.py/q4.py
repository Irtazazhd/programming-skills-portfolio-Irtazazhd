# Create a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Initialize a variable to store the target number
target_number = 6

# Use a for loop to search for the target number
for number in numbers:
    if number == target_number:
        print(f"Target number {target_number} found!")
        break  # Exit the loop when the target number is found
    else:
        print(f"Checking {number}...")

# This code will continue here after the loop is exited
print("Loop finished.")
