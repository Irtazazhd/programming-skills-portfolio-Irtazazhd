while True:
    age = input("Enter your age to determine the ticket price (or 'quit' to exit): ")
    
    if age.lower() == 'quit':
        break

    try:
        age = int(age)
    except ValueError:
        print("Please enter a valid age or 'quit'.")
        continue

    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    
    if price == 0:
        print("The ticket is free for you!")
    else:
        print(f"Your movie ticket costs ${price}.")
