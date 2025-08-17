class Coffee:
    # initialize coffee with name and price

    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    # initialize order with empty list

    def __init__(self):
        self.items = []

    # add the coffee to order

    def add_item(self, coffee):
        self.items.append(coffee)
        print(f"Added {coffee.name} to your order.")

    # calculate total price

    def total(self):
        return sum(item.price for item in self.items)
    
    # print order details

    def print_order(self):
        if not self.items:
            print("No items in your order list.")
            return 
        
        print("\n Your Order:")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name} - ₹{item.price:.2f}")

        print(f"Total: ₹{self.total():.2f}\n")

    # handle checkout process
    
    def checkout(self):
        if not self.items:
            print("Your cart is empty. Pleas add items to your order.")
            return 
        
        self.print_order()

        confirm = input("Proceed to checkout? (yes/no): ").strip().lower()
        
        if confirm == 'yes':
            print("Order Placed Successfully! Thank you.")

            self.items.clear() # Clear the order after checkout
        else:
            print("Checkout cancelled. Your order is still in the cart.")

# display menu and handle user input

class main():
    menu = [
        Coffee("Espresso", 50),
        Coffee("Cappuccino", 70),
        Coffee("Latte", 80),
        Coffee("Mocha", 90),
        Coffee("Americano", 60),
        Coffee("Macchiato", 75),
        Coffee("Irish Coffee", 100),
        Coffee("Turkish Coffee", 65),
        Coffee("Iced Latte", 60),
        Coffee("Coffee with Milk", 50),
        Coffee("Coffee with Cream", 55)
    ]

    order = Order()
    #User interface for coffee shop

    while True:
        print("\n--- Coffee Shop Menu ---")

        for i, coffee in enumerate(menu, 1):
            print(f"{i}. {coffee.name} - ₹{coffee.price:.2f}")

        print("12. View Order")
        print("13. Checkout")
        print("14. Exit")

        choice = input("Choose an option (1-14): ").strip()

        if choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']:
            coffee = menu[int(choice) - 1]
            order.add_item(coffee)

        elif choice == '12':
            order.print_order()

        elif choice == '13':
            order.checkout()

        elif choice == '14':
            print("Thankyou for visiting our Coffee Shop! Good bye.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()