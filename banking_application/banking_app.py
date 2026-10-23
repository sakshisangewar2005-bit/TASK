# Task 03 - Banking Console Application (Python)
# Kiran Academy - Java & Python Programming Task

def fmt(n):
    # show 11500.0 as 11500, but keep 11500.5 as it is
    return str(int(n)) if n == int(n) else str(n)


balance = 10000  # fixed opening balance (in rupees)

print("Welcome to Kiran Bank")
print("Opening Balance: ₹" + fmt(balance))

while True:
    print()
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = input("Enter choice: ").strip()

    if choice == "1":
        print("Current Balance: ₹" + fmt(balance))

    elif choice == "2":
        try:
            amount = float(input("Enter deposit amount: "))
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue

        if amount <= 0:
            print("Invalid amount. Deposit must be greater than ₹0.")
        else:
            balance = balance + amount
            print("Deposit successful.")
            print("Updated Balance: ₹" + fmt(balance))

    elif choice == "3":
        try:
            amount = float(input("Enter withdrawal amount: "))
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue

        if amount <= 0:
            print("Invalid amount. Withdrawal must be greater than ₹0.")
        elif amount > balance:
            print("Transaction failed: Insufficient balance.")
            print("Current Balance: ₹" + fmt(balance))
        else:
            balance = balance - amount
            print("Withdrawal successful.")
            print("Updated Balance: ₹" + fmt(balance))

    elif choice == "4":
        print("Thank you for banking with us. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3 or 4.")
