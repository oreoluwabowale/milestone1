import math

print("Sales Report")
print()

year =  int(input("Please input the year the sales report is for: "))
print()

months = 0
salesTotal = 0
list1= []

for i in range(12):
    months+=1
    sales = float(input("Please enter the sales for month " +str(months)+ ": £"))
    salesTotal += sales
    list1.append(sales)
print()

#print("The total sales for", year ,"are £",(str(salesTotal)))
print(f"The total sales for the year is £{salesTotal:.1f}")

average_sales = (salesTotal/12)

#print("The average sales for", year ,"are £",(str(average_sales)))
print(f"The average sale for the year is £ {average_sales:.1f}")


min_month = min(list1)

max_month = max(list1)

print("The month with the minimum sales is month", months ,"£",(str(min_month)))
print("The month with the maxmimum sales is month", months ,"£",(str(max_month)))
