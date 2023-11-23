largest = None

while True:
    user_input = input("Enter a number (or '0' to exit): ")
    
    if user_input == '0':
        break
    
    try:
        number = int(user_input)
        largest = max(largest, number) if largest is not None else number
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if largest is not None:
    print("The largest number entered is:", largest)
else:
    print("No valid numbers were entered.")

