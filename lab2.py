
#lab2 ARITHMETIC_STRING_OPERATIONS

price = 2.99
quantity = 3
tax_rate = 0.075

print("price of item: $", price)
print("quantity", quantity)
print("Tax rate:", tax_rate*100, "%")

subtotal = price * quantity
print("subtotal: $", subtotal)

tax = round(subtotal * tax_rate, 2)
print("Tax: $", tax)

total = subtotal + tax
print("total: $", total)
