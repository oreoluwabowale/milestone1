import math

print("Sales Report")
print()

year =  float(input("Please input the year the sales report is for: "))
print()

months = 0
salesTotal = 0
list1= []

for i in range(12):
    months+=1
    sales = int(input("Please enter the sales for month " +str(months)+ ": "))
    salesTotal += sales
    list1.append(sales)
print()

print(f"The total sales for", year ,"are £ {salesTotal:.1f}")


average_sales = (salesTotal/12)

print(f"The average sales for", year ,"are £ {average_sales:.1f}")

min_month = min(list1)

max_month = max(list1)

print("The month with the minimum sales is", months ,"is",(str(min_month)))
print("The month with the maxmimum sales is", months ,"is",(str(max_month)))
