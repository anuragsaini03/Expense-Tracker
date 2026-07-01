#expence tracker 
expenses = []

print(".....Welcome to Expense traker.....")
print("Karcha kam kiya karo!")

while True:
    print("====Menu====")
    print("1. Add Expenses")
    print("2. View all Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

    choice = input("Please Enter your Choice: ")

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

        