import os
while True:
    print("Welcome to the expense tracker what do you like to do?")
    print("1.Add expenses\n2.View expenses\n3.Clear expenses\n4.Exit")
    choice=input("Enter your choice (1-4) :").strip()
    valid_choice=["1","2","3","4"]
    while choice not in valid_choice:
        print("You can only enter (1-4)")
        choice=input("Enter your choice (1-4) :").strip()
    if choice=="1":
        name,price=input("Enter the expense name seperated by commas :").strip(),input("Enter the amount seperated by commas :").strip()
        name=name.split(",")
        price=price.split(",")
        price=[int(i) for i in price]    
        expense_dict=dict(zip(name,price))
        expense=[]
        total=0
        for x,y in expense_dict.items():
            expense.append(f"Expense names are : {x} | prices are : {y}\n")
        with open("expenses.txt","at") as f:
            f.writelines(expense)            
            print("The data has been saved")
            for i in price:
                total+=i
            print(f"The total expense amount is : {total}")            
    if choice=="2":
        if os.path.exists("expenses.txt"):
            with open("expenses.txt","rt") as f:
                        for i in f:
                            print(i,end="")
        else:
            print("oops there is no data!")
    if choice=="3":
        if os.path.exists("expenses.txt"):
            os.remove("expenses.txt")
            print("Data has been deleted")
        else:
            print("oops there is no data!")    
    if choice=="4":
        print("Goodbye see you later")        
        break