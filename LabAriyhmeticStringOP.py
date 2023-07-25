
price = "$2.99"
quantity = 3
tax_rate = "7.5%"

# اقتطاع علامة $ من السعر وتحويله الى رقم 
price1 = price[1:]
price2 = float(price1)

# اقتطاع علامة % من القيمة المضافه وتحويله الى رقم 

tax_rate1 = tax_rate[:3]
tax_rate2 = float(tax_rate1)
tax_rate3 = tax_rate2 /100

subtotal = price2 * quantity
tax  = subtotal * tax_rate3
total  = subtotal + tax


print("Price of item:",price)
print("Quantity:",quantity)
print("Tax rate:",tax_rate)

print("Subtotal: $",subtotal)
print("Tax: $",round(tax , 2))
print("Total: $",round(total , 2))
