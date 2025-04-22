class ATM:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.transaction_history = []

    def check_balance(self):
        print(f"\n✅ Your current balance is: ₹{self.balance}")
        self.transaction_history.append("Checked balance")

    def deposit(self, amount):
        if amount <= 0:
            print("\n❌ Invalid deposit amount.")
            return
        self.balance += amount
        print(f"\n💰 ₹{amount} deposited successfully.")
        self.transaction_history.append(f"Deposited ₹{amount}")

    def withdraw(self, amount):
        if amount <= 0:
            print("\n❌ Invalid withdrawal amount.")
        elif amount > self.balance:
            print("\n❌ Insufficient balance.")
        else:
            self.balance -= amount
            print(f"\n💸 ₹{amount} withdrawn successfully.")
            self.transaction_history.append(f"Withdrew ₹{amount}")

    def show_transactions(self):
        print("\n📜 Transaction History:")
        if not self.transaction_history:
            print("No transactions yet.")
        else:
            for i, txn in enumerate(self.transaction_history, 1):
                print(f"{i}. {txn}")

# Menu for user interaction
def main():
    atm = ATM(10000)  # Set initial balance here

    while True:
        print("\n--- ATM Management System ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            atm.check_balance()
        elif choice == "2":
            amount = float(input("Enter deposit amount: ₹"))
            atm.deposit(amount)
        elif choice == "3":
            amount = float(input("Enter withdrawal amount: ₹"))
            atm.withdraw(amount)
        elif choice == "4":
            atm.show_transactions()
        elif choice == "5":
            print("👋 Thank you for using the ATM. Goodbye!")
            break
        else:
            print("❌ Invalid option. Please try again.")

if __name__ == "__main__":
    main()
