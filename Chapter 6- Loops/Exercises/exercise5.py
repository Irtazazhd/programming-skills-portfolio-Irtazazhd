# List of sandwich orders with 'pastrami' repeated at least three times
sandwich_orders = ['tuna', 'chicken', 'pastrami', 'egg salad', 'roast beef', 'pastrami', 'ham', 'pastrami']

# Empty list for finished sandwiches
finished_sandwiches = []

# Print a message indicating the deli has run out of pastrami
print("Sorry, the deli has run out of pastrami.")

# Remove all occurrences of 'pastrami' from sandwich_orders using a while loop
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Loop through the updated list of sandwich orders
for order in sandwich_orders:
    print(f"I made your {order} sandwich.")
    finished_sandwiches.append(order)

# Print a message listing each sandwich that was made
print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich} sandwich")
