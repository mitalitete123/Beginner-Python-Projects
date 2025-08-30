class User:
    # Initiialize user with name and balance

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    # Show user's balance

    def show_balance(self):
        print(f"Current balance of {self.name}: ₹{self.balance:.2f}")

    # Add money to user's balance

    def add_money(self, amount):
        if amount <= 0:
            print("Please enter a valid amount to add.")

        else:
            self.balance += amount
            print(f"₹{amount:.2f} added to your balance. \nNew balance: ₹{self.balance:.2f}")

    # Send money to another user

    def send_money(self, recipient, amount):
        if amount <= 0:
            print("Please enter a valid amount to send.")

        elif amount > self.balance:
            print("Insufficient balance to send this amount.")

        else:
            self.balance -= amount
            recipient.balance += amount
            print(f"₹{amount:.2f} sent to {recipient.name}. \nNew balance: ₹{self.balance:.2f}")

# Show menu and handle user input

class main():
    # Create two users for demonstration

    user1 = User("Mitali", 957.50)
    user2 = User("Rahul", 1683.75)

    while True:
        print("\n---Payment App---")
        print("1. Show Balance")
        print("2. Add Money")
        print("3. Send Money")
        print("4. Exit")

        choice = float(input("Enter your choice: "))

        if choice == 1:
            user1.show_balance()

        elif choice == 2:
            amt = float(input("Enter amount to add: "))
            user1.add_money(amt)

        elif choice == 3:
            amt = float(input("Enter amount to send: "))
            user1.send_money(user2, amt)

        elif choice == 4:
            print("Exiting the app... \nThank you!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the App
if __name__ == "__main__":
    main()
