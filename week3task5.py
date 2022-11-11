print("Account Interest Calculator")
print("---------------------------")
print()

starting_balance = float(input("Please enter the starting balance: £"))
final_balance = float(input("Please enter the final balance: £"))
interest_rate = float(input("Please enter the interest rate: "))

current_balance = starting_balance
month = 0

print("Month\tBalance (£)")

while current_balance < final_balance:
    month+=1



    current_balance = current_balance *(1 + (interest_rate / 100))
    
    print(str(month) + "\t" + "{:.2f}".format(current_balance))
        
print()
print("It will take " + str(month) + " months to achieve the balance £" + "{:.2f}".format(final_balance))
