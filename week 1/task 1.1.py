""""task 1:
Write a Python program that helps a user summarize their monthly budget.
The program should ask for several inputs, perform calculations, and display results neatly."""

print("Welcome to the Personal Finance Assistant!")
#get user details

name=input("Enter your name: ")
age=int(input("Enter your age: "))

#get monthly income of the user

monthly_income=float(input("Enter your monthly income: "))

#get monthly expenses of the user

food_expenses=float(input("Enter your food expenses: "))
transtport_expenses=float(input("Enter your transtport expenses: "))
entertainment_expenses=float(input("Enter your entertainment expenses: "))


total_expenses=food_expenses+transtport_expenses+entertainment_expenses #calculate total expense of the month
remaining_balance=monthly_income-total_expenses #calculate balance income of the month

#display budget details of the user
print("\n-----Monthly Budget Summary-----")
print(f"Name: {name} (Age: {age})")
print(f"Income: {monthly_income:.2f}")
print(f"Total Expenses: {total_expenses:.2f}")
print(f"Remaining Balance: {remaining_balance:.2f}")
print(f"Recommended Savings (10%): {(10*monthly_income)/100:.2f}")
