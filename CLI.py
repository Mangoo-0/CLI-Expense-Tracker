import json
import os
if os.path.exists("expenses.json"):
    with open ("expenses.json","r") as file:
        expenses=json.load(file)
else:
    expenses=[]
while True:

    print("MY EXPENSE TRACKER")
    print("1. Add Expense.")
    print("2. View Expense.")
    print("3. Exit.")
    print("4. Total Expense.")
    try:
        action=int(input("Choose action to perform. 1,2,3,4. "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    print(" your selected action is ",action)

    if action==1:
        name=input("Enter expense name: ")
        while True:
        
            try:
                amount=float(input("Enter amount: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue
            
            if amount<=0:
                print("Amount must be greater than zero,please enter a valid positive number.")
                continue
            break

        category=input("Enter category: ")

        new_expenses={
            "name":name,"amount":amount, "category":category    }
        expenses.append(new_expenses)

        print("Expense added succesfully. ")
    elif action==2:
        if not expenses:
            print("Your expenses is none. ")
        else:
            for items in expenses:
                print("--- YOUR EXPENSES---")
                print("Name: ",items["name"])
                print("Amount: ",items["amount"])
                print("Category: ",items["category"])
                print("--------------------------")

        
    elif action==3:
        print("Existing Expense Tracker....")
        break
    elif action==4:
        if not expenses:
            print("your expenses is none. ")
        else:
            total_expenses=0
            for items in expenses:
                total_expenses=total_expenses+items["amount"]
            print("--- YOUR TOTAL EXPENSE ---")
            print(total_expenses)
    else:
        print("Option doesnt match")
with open ("expenses.json","w") as file:
    json.dump(expenses,file)


