# import os
# import matplotlib.pyplot as plt

# FILE_NAME = "data.csv"

# # Create file if not exists
# if not os.path.exists(FILE_NAME):
#     with open(FILE_NAME, "w") as f:
#         f.write("date,category,amount,description\n")

# # Category selection
# def get_category():
#     print("\nSelect Category:")
#     print("1. Food")
#     print("2. Travel")
#     print("3. Bills")
#     print("4. Others")

#     choice = input("Enter choice: ")

#     if choice == "1":
#         return "Food"
#     elif choice == "2":
#         return "Travel"
#     elif choice == "3":
#         return "Bills"
#     else:
#         return "Others"

# # Add Expense
# def add_expense():
#     date = input("📅 Enter date (YYYY-MM-DD): ")
#     category = get_category()
    
#     try:
#         amount = float(input("💰 Enter amount: "))
#     except:
#         print("❌ Invalid amount")
#         return

#     description = input("📝 Enter description: ")

#     with open(FILE_NAME, "a") as f:
#         f.write(f"{date},{category},{amount},{description}\n")

#     print("✅ Expense added successfully!")

# # View Expenses
# def view_expenses():
#     with open(FILE_NAME, "r") as f:
#         data = f.readlines()

#         if len(data) <= 1:
#             print("⚠ No expense data found.")
#             return

#         print("\n📄 All Expenses:\n")
#         for line in data:
#             print(line.strip())

# # Delete Expense
# def delete_expense():
#     with open(FILE_NAME, "r") as f:
#         lines = f.readlines()

#     if len(lines) <= 1:
#         print("⚠ No expenses to delete.")
#         return

#     print("\n🗑 Select Expense to Delete:\n")

#     for i in range(1, len(lines)):
#         print(f"{i}. {lines[i].strip()}")

#     try:
#         choice = int(input("\nEnter number to delete: "))
#     except:
#         print("❌ Invalid input.")
#         return

#     if choice < 1 or choice >= len(lines):
#         print("❌ Invalid choice.")
#         return

#     del lines[choice]

#     with open(FILE_NAME, "w") as f:
#         f.writelines(lines)

#     print("✅ Expense deleted successfully!")

# # Summary Logic
# def get_summary(filter_month=None):
#     total = 0
#     category_data = {}

#     with open(FILE_NAME, "r") as f:
#         lines = f.readlines()[1:]

#         if not lines:
#             return None, None

#         for line in lines:
#             parts = line.strip().split(",")
#             if len(parts) < 4:
#                 continue

#             date = parts[0]
#             category = parts[1]
#             amount = float(parts[2])

#             if filter_month and not date.startswith(filter_month):
#                 continue

#             total += amount

#             if category in category_data:
#                 category_data[category] += amount
#             else:
#                 category_data[category] = amount

#     return total, category_data

# # Monthly Summary
# def monthly_summary():
#     month = input("Enter month (YYYY-MM): ")
#     total, category_data = get_summary(month)

#     if not category_data:
#         print("⚠ No data for this month.")
#         return

#     print(f"\n📊 Monthly Summary ({month})")
#     print("Total Expense: ₹", total)

#     print("\n📂 Category Breakdown:")
#     for cat in category_data:
#         print(f"{cat} → ₹{category_data[cat]}")

#     show_insights(category_data)

# # Overall Summary
# def overall_summary():
#     total, category_data = get_summary()

#     if not category_data:
#         print("⚠ No data found.")
#         return

#     print("\n📊 Overall Summary")
#     print("Total Expense: ₹", total)

#     print("\n📂 Category Breakdown:")
#     for cat in category_data:
#         print(f"{cat} → ₹{category_data[cat]}")

#     show_insights(category_data)

# # Insights
# def show_insights(category_data):
#     max_category = max(category_data, key=category_data.get)
#     max_value = category_data[max_category]

#     print(f"\n🔥 Highest Spending Category: {max_category} (₹{max_value})")

#     print("\n💡 Insight:")
#     if max_category == "Food":
#         print("You are spending a lot on food. Try reducing dining out.")
#     elif max_category == "Travel":
#         print("Travel expenses are high. Consider optimizing routes.")
#     elif max_category == "Bills":
#         print("Bills are high. Monitor your usage.")
#     else:
#         print("Review your expenses to improve savings.")

# # Pie Chart
# def show_pie_chart():
#     _, category_data = get_summary()

#     if not category_data:
#         print("⚠ No data for chart.")
#         return

#     labels = list(category_data.keys())
#     sizes = list(category_data.values())

#     plt.pie(sizes, labels=labels, autopct='%1.1f%%')
#     plt.title("Expense Distribution")
#     plt.show()

# # Main Menu
# while True:
#     print("\n====== SMART EXPENSE TRACKER ======")
#     print("1. Add Expense")
#     print("2. View Expenses")
#     print("3. Monthly Summary")
#     print("4. Overall Summary")
#     print("5. Show Pie Chart")
#     print("6. Delete Expense")
#     print("7. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         add_expense()
#     elif choice == "2":
#         view_expenses()
#     elif choice == "3":
#         monthly_summary()
#     elif choice == "4":
#         overall_summary()
#     elif choice == "5":
#         show_pie_chart()
#     elif choice == "6":
#         delete_expense()
#     elif choice == "7":
#         print("👋 Exiting...")
#         break
#     else:
#         print("❌ Invalid choice. Try again.")
import os
import matplotlib.pyplot as plt

FILE_NAME = "data.csv"
budget = 0

# Create file if not exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        f.write("date,category,amount,description\n")

# Category selection
def get_category():
    print("\nSelect Category:")
    print("1. Food\n2. Travel\n3. Bills\n4. Others")
    choice = input("Enter choice: ")
    return ["Food", "Travel", "Bills", "Others"][int(choice)-1] if choice in ["1","2","3","4"] else "Others"

# Add Expense
def add_expense():
    global budget
    date = input("📅 Enter date (YYYY-MM-DD): ")
    category = get_category()
    
    try:
        amount = float(input("💰 Enter amount: "))
    except:
        print("❌ Invalid amount")
        return

    description = input("📝 Enter description: ")

    with open(FILE_NAME, "a") as f:
        f.write(f"{date},{category},{amount},{description}\n")

    print("✅ Expense added successfully!")

    if budget > 0:
        total, _ = get_summary()
        if total > budget:
            print(f"⚠ Budget exceeded! Budget: ₹{budget}, Spent: ₹{total}")
        else:
            print(f"💰 Remaining Budget: ₹{budget - total}")

# View Expenses
def view_expenses():
    with open(FILE_NAME, "r") as f:
        lines = f.readlines()
        if len(lines) <= 1:
            print("⚠ No data found.")
            return

        print("\n📄 Expense List:")
        for i in range(1, len(lines)):
            print(f"{i}. {lines[i].strip()}")

# Delete Expense
def delete_expense():
    with open(FILE_NAME, "r") as f:
        lines = f.readlines()

    if len(lines) <= 1:
        print("⚠ No expenses to delete.")
        return

    print("\n🗑 Select Expense to Delete:")
    for i in range(1, len(lines)):
        print(f"{i}. {lines[i].strip()}")

    try:
        choice = int(input("Enter number: "))
    except:
        print("❌ Invalid input")
        return

    if choice < 1 or choice >= len(lines):
        print("❌ Invalid choice")
        return

    confirm = input("Are you sure? (y/n): ")
    if confirm.lower() != "y":
        print("Cancelled.")
        return

    del lines[choice]

    with open(FILE_NAME, "w") as f:
        f.writelines(lines)

    print("✅ Expense deleted!")

# Summary Logic
def get_summary(filter_value=None, by_date=False):
    total = 0
    category_data = {}

    with open(FILE_NAME, "r") as f:
        lines = f.readlines()[1:]

        for line in lines:
            parts = line.strip().split(",")
            if len(parts) < 4:
                continue

            date, category, amount = parts[0], parts[1], float(parts[2])

            if filter_value:
                if by_date and date != filter_value:
                    continue
                elif not by_date and not date.startswith(filter_value):
                    continue

            total += amount
            category_data[category] = category_data.get(category, 0) + amount

    return total, category_data

# Monthly Summary
def monthly_summary():
    month = input("Enter month (YYYY-MM): ")
    total, data = get_summary(month)

    if not data:
        print("⚠ No data found.")
        return

    print(f"\n📊 Monthly Summary ({month})")
    print(f"Total: ₹{total}")
    for k, v in data.items():
        print(f"{k} → ₹{v}")
    show_insights(data)

# Overall Summary
def overall_summary():
    total, data = get_summary()

    if not data:
        print("⚠ No data.")
        return

    print("\n📊 Overall Summary")
    print(f"Total: ₹{total}")
    for k, v in data.items():
        print(f"{k} → ₹{v}")
    show_insights(data)

# Search by Category
def search_category():
    cat = input("Enter category (Food/Travel/Bills/Others): ")
    _, data = get_summary()

    print(f"\n🔍 Results for {cat}:")
    with open(FILE_NAME, "r") as f:
        lines = f.readlines()[1:]
        for line in lines:
            if cat.lower() in line.lower():
                print(line.strip())

# Search by Date
def search_date():
    date = input("Enter date (YYYY-MM-DD): ")
    print(f"\n🔍 Expenses on {date}:")
    with open(FILE_NAME, "r") as f:
        lines = f.readlines()[1:]
        for line in lines:
            if line.startswith(date):
                print(line.strip())

# Insights
def show_insights(data):
    max_cat = max(data, key=data.get)
    print(f"\n🔥 Highest: {max_cat} (₹{data[max_cat]})")

    if max_cat == "Food":
        print("💡 Reduce food spending.")
    elif max_cat == "Travel":
        print("💡 Optimize travel.")
    else:
        print("💡 Monitor expenses.")

# Pie Chart
def show_chart():
    _, data = get_summary()
    if not data:
        print("⚠ No data.")
        return

    plt.pie(data.values(), labels=data.keys(), autopct='%1.1f%%')
    plt.title("Expense Distribution")
    plt.show()

# Set Budget
def set_budget():
    global budget
    try:
        budget = float(input("Enter monthly budget: "))
        print(f"✅ Budget set: ₹{budget}")
    except:
        print("❌ Invalid input")

# Main Menu
while True:
    print("\n========== SMART EXPENSE TRACKER ==========")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Monthly Summary")
    print("4. Overall Summary")
    print("5. Pie Chart")
    print("6. Delete Expense")
    print("7. Search by Category")
    print("8. Search by Date")
    print("9. Set Budget")
    print("10. Exit")

    choice = input("👉 Enter choice: ")

    if choice == "1": add_expense()
    elif choice == "2": view_expenses()
    elif choice == "3": monthly_summary()
    elif choice == "4": overall_summary()
    elif choice == "5": show_chart()
    elif choice == "6": delete_expense()
    elif choice == "7": search_category()
    elif choice == "8": search_date()
    elif choice == "9": set_budget()
    elif choice == "10":
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid choice")