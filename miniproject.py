# KAYISE IT - Python Programming Mini Project: Simple ATM Menu System

def main():
    # Predefined account details
    correct_pin = "4321"
    balance = 2000.00

    print("=== Welcome to KAYISE IT ATM ===")
    entered_pin = input("Please enter your ATM PIN: ").strip()

    # Task 1: PIN Authentication
    if entered_pin != correct_pin:
        print("Incorrect PIN. Access denied.")
        return

    print("\nPIN verified. Access granted.\n")

    # Task 2 & Task 3: Display Menu and Handle Selections
    while True:
        print("--- ATM Main Menu ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            # Option 1: Check Balance
            print(f"\nYour current balance is: R{balance:.2f}\n")

        elif choice == "2":
            # Option 2: Deposit Money
            raw_amount = input("Enter amount to deposit: R").strip()
            try:
                deposit_amount = float(raw_amount)
                if deposit_amount <= 0:
                    print("Invalid deposit amount. Please enter an amount greater than R0.00.\n")
                else:
                    balance = balance + deposit_amount
                    print(f"Deposit successful! Updated balance: R{balance:.2f}\n")
            except ValueError:
                print("Invalid input. Please enter a valid number.\n")

        elif choice == "3":
            # Option 3: Withdraw Money
            raw_amount = input("Enter amount to withdraw: R").strip()
            try:
                withdraw_amount = float(raw_amount)
                if withdraw_amount <= 0:
                    print("Invalid withdrawal amount. Please enter an amount greater than R0.00.\n")
                elif withdraw_amount > balance:
                    print(f"Insufficient funds. Available balance: R{balance:.2f}\n")
                else:
                    balance = balance - withdraw_amount
                    print(f"Withdrawal successful! Updated balance: R{balance:.2f}\n")
            except ValueError:
                print("Invalid input. Please enter a valid number.\n")

        elif choice == "4":
            print("\nThank you for using KAYISE IT ATM. Have a great day!")
            break

        else:
            # Invalid Option
            print("Invalid option. Please select a valid menu number (1-4).\n")


if __name__ == "__main__":
    main()
