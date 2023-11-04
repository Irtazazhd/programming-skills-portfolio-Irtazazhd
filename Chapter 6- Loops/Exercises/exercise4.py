# List of sandwich orders
sandwich_orders = ['tuna', 'chicken', 'egg salad', 'roast beef', 'ham']

# Empty list for finished sandwiches
finished_sandwiches = []

# Loop through the list of sandwich orders
for order in sandwich_orders:
    print(f"I made your {order} sandwich.")
    finished_sandwiches.append(order)

# Print a message listing each sandwich that was made
print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich} sandwich")
