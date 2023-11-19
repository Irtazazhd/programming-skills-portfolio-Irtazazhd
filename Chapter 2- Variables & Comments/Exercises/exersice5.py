# Define the total amount of money the girl has
total_money = 50

# Define the price of one USB stick
usb_price = 6

# Calculate how many USB sticks she can buy
usb_count = total_money // usb_price  # Using integer division

# Calculate how much money she will have left
money_left = total_money % usb_price  # Using the modulus operator

# Print the results
print("The girl can buy", usb_count, "USB sticks.")
print("She will have £", money_left, "left.")