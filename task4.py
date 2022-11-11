import math

print("sales report")
year = int(input("Input the year the sales report is for:"))
january = float(input("Input January's sales amount: £"))
february = float(input("Input February's sales amount: £"))
march = float(input("Input March's sales amount: £"))
april = float(input("Input April's sales amount: £"))
may = float(input("Input May's sales amount: £"))
june = float(input("Input June's sales amount: £"))
july = float(input("Input July's sales amount: £"))
august = float(input("Input August's sales amount: £"))
september = float(input("Input September's sales amount: £"))
october = float(input("Input October's sales amount: £"))
november = float(input("Input November's sales amount: £"))
december = float(input("Input December's sales amount: £"))


total_sales = (january + february + march +april + may + june + july + august + september +october + november + december)

print(math.ceil,"The total sales for", year ,"are £",(str(total_sales)))

average_sales = (total_sales/12)

print(math.ceil,"The average sales for", year ,"are £",(str(average_sales)))

min_month = min([january,february,march,april,may,june,july,august,september,october,november,december])
min([january,february,march,april,may,june,july,august,september,october,november,december])
print(min_month)