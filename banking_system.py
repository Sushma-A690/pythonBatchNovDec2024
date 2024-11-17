account_holder_name = input("Enter account holder's name: ")
holder_email = (input("Enter your email:"))
opening_balance = float(input("Add the amount:"))
print(f"Your account has been created successfully! Welcome to Boffa, {account_holder_name}!")
deposit_amount = float(input("Enter the deposit amout:"))
availble_balance = opening_balance+deposit_amount
print( availble_balance)
withdraw_amount = float(input(" Enter the withdraw amount:"))
Final_availble_balance = (opening_balance + deposit_amount) - withdraw_amount
print("Available_balance: " + str(Final_availble_balance))
