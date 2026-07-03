#expence tracker 
expenses = []

print(".....Welcome to Expense traker.....")
print("Karcha kam kiya karo!")

# choice = int(input("Please enter your Choice: "))

while True:
    print("====Menu====")
    print("1. Add Expenses")
    print("2. View all Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

    choice = int(input("Please Enter your Choice: "))

# 1. Add Expenses
    if(choice == 1):
        date = input("Enter the date: ")
        category = input("Enter Category of Item, (Food, Travel, Shoping, Stationary, any Other: ")
        description = input("Any other Details about Product: ")
        amount = input("Enter amount of Item: ")

        expense = {
            "date" : date,
            "category" : category,
            "description" : description,
            "amount" : amount
        }

        expenses.append(expense)
        print(" \n Your Expenses added Succesfully!")

# 2. View all expenses
    elif (choice == 2):
        if( len(expenses) == 0):
            print("No expense added, Go and add Expense")
        else:
            print("==== Here is your all expenses =====")
            count = 1
            for each_expense in expenses:
                print(f"Expense no. {count} -> {each_expense ["date"]}, {each_expense ["category"]}, {each_expense ["description"]}, {each_expense ["amount"]} ")
                count += 1

# 3. View total spending
    elif (choice == 3):
        total = 0
        for each_expense in expenses:
            total = total + int(each_expense["amount"])

        print("\n Total expense = ", total)

#4. Exit
    elif (choice == 4):
        print("Thanks for using our Program!")
        break

# For wrong input
    else:
        print("____Wrong Input____")
