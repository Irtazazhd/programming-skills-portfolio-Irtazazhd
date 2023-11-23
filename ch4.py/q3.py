# Take input for amount1 and amount2
amount1 = float(input("Enter the value for amount1: "))
amount2 = float(input("Enter the value for amount2: "))

# Check the conditions and display the result
if amount1 > 10 and amount2 < 100:
    if amount1 > amount2:
        print("The greater of amount1 and amount2 is:", amount1)
    else:
        print("The greater of amount1 and amount2 is:", amount2)
else:
    print("The conditions for displaying the greater value are not met.")

