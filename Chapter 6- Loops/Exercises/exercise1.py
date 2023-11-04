# Start with an empty list to store the pizza toppings
pizza_toppings = []

# Prompt the user for pizza toppings
print("Enter a series of pizza toppings (type 'quit' when you are finished):")

while True:
    topping = input("Add a topping: ")
    
    if topping.lower() == 'quit':
        break
    else:
        pizza_toppings.append(topping)
        print(f"We'll add {topping} to your pizza!")

# After the loop, you could also list all the toppings the user chose
print("\nWe're preparing your pizza with the following toppings:")
for topping in pizza_toppings:
    print(f"- {topping}")
