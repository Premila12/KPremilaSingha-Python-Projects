import os

# ---------------------------------------------
#  Expense Tracker With Input/Output File System
# ---------------------------------------------

def initialize_expenses():
    """Returns an empty expenses dictionary."""
    return {}


def add_expense(expenses, category, amount):
    """Adds or updates expense for a category."""
    if category in expenses:
        expenses[category] += amount
        print(f"✓ Updated {category}: ₹{expenses[category]} (added ₹{amount})")
    else:
        expenses[category] = amount
        print(f"✓ Added {category}: ₹{amount}")


def display_expenses(expenses):
    """Displays all expenses in a formatted way."""
    print("\n" + "="*60)
    print("Expense Summary")
    print("="*60)

    if not expenses:
        print("No expenses recorded yet!")
    else:
        for category, amount in sorted(expenses.items()):
            print(f"{category:20} : ₹{amount:>10.2f}")

    print("-"*60)
    total = sum(expenses.values())
    print(f"{'TOTAL SPENT':20} : ₹{total:>10.2f}")
    print("="*60)


def save_expenses_to_file(expenses, filename):
    """Saves expenses to a file."""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("Expense Tracker Report\n")
        file.write("Author: K Premila Singha\n")
        file.write("="*60 + "\n\n")

        file.write(f"{'Category':<20} {'Amount (₹)':>15}\n")
        file.write("-"*60 + "\n")

        for category, amount in sorted(expenses.items()):
            file.write(f"{category:<20} {amount:>15.2f}\n")

        file.write("-"*60 + "\n")
        total = sum(expenses.values())
        file.write(f"{'TOTAL SPENT':<20} {total:>15.2f}\n")
        file.write("="*60 + "\n")

    print(f"\n✓ Expenses saved to '{filename}'")


def load_expenses_from_file(filename):
    """Loads expenses from input file (if exists)."""
    expenses = {}

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            print(f"✓ Reading expenses from '{filename}'")

            for line in file:
                line = line.strip()
                if not line:
                    continue

                parts = line.split("|")
                if len(parts) != 2:
                    print(f"Skipping invalid line: {line}")
                    continue

                category, amount = parts[0].strip(), parts[1].strip()

                try:
                    expenses[category] = float(amount)
                except ValueError:
                    print(f"Invalid amount in line: {line}")

    except FileNotFoundError:
        print(f"❌ Input file '{filename}' not found! Starting with empty expenses.")

    return expenses


def main():
    """Main function to manage expenses."""
    print("\n💰 Expense Tracker")
    print("Author: K Premila Singha\n")

    # Input & output file paths
    input_file = "input_files/expenses.txt"
    output_file = "output_files/expenses.txt"

    # Load from input file
    expenses = load_expenses_from_file(input_file)

    # Add sample data
    print("\nRecording sample expenses...\n")
    add_expense(expenses, "Food", 500)
    add_expense(expenses, "Transport", 200)
    add_expense(expenses, "Entertainment", 800)
    add_expense(expenses, "Food", 300)
    add_expense(expenses, "Shopping", 1500)
    add_expense(expenses, "Bills", 2000)
    add_expense(expenses, "Transport", 150)

    # Display expenses
    display_expenses(expenses)

    # Highest expense
    highest = max(expenses, key=expenses.get)
    print(f"\n🔝 Highest Expense: {highest} - ₹{expenses[highest]:.2f}")

    # Save to output file
    save_expenses_to_file(expenses, output_file)

    print("\n" + "="*60)
    print("💡 Tip: Add your own entries inside input_files/expenses.txt!")
    print("="*60)


if __name__ == "__main__":
    main()