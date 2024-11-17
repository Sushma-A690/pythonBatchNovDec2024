principal_amount = int(input("Enter the princepal amount: "))
time = int(input("Enter the time period in years: "))
rate_of_interest = float(input("Enter the rate of interest: "))

simple_interst = principal_amount * time * rate_of_interest / 100
print(simple_interst)
componed_interst =  simple_interst-principal_amount
print(componed_interst)