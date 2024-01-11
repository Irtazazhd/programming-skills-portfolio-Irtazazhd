class VendingMachine:
    def __init__(self):
        # Define products with their codes, names, prices, and stock
        self.products = {
            'A1': {'tapper': 'Water', 'price': 1.50, 'stock': 10},
            'A2': {'irti': 'Soda', 'price': 2.00, 'stock': 10},
            'B1': {'': 'Chips', 'price': 1.75, 'stock': 10},
            'B2': {'abdu': 'Chocolate Bar', 'price': 1.25, 'stock': 10}
        }

    def display_products(self):
        # Display available products
        print("Available Products:")
        for code, item in self.products.items():
            print(f"{code}: {item['name']} - ${item['price']} (Stock: {item['stock']})")

    def select_product(self, code):
        # Return the selected product or None if invalid
        return self.products.get(code)

    def vend(self, code, money_inserted):
        product = self.select_product(code)
        if not product:
            return "Invalid selection", money_inserted

        if product['stock'] <= 0:
            return "Out of stock", money_inserted

        if money_inserted < product['price']:
            return "Insufficient funds", money_inserted

        product['stock'] -= 1
        change = money_inserted - product['price']
        return f"Dispensed {product['name']}. Change: ${change:.2f}", change

def main():
    machine = VendingMachine()
    while True:
        # Show products
        machine.display_products()

        # Get user input
        choice = input("Enter product code or 'quit' to exit: ").strip()
        if choice.lower() == 'quit':
            break

        try:
            money = float(input("Insert money ($): "))
        except ValueError:
            print("Please enter a valid amount.")
            continue

        # Vend item and return change
        message, change = machine.vend(choice, money)
        print(message)

if __name__ == "__main__":
    main()
    