price = 2.99
print(f"price of item : ${price}")

Quantity= 3
print(f"Quantity : {Quantity}")

tax_rate = 7.5
print(f"Tax rate : {tax_rate}%")
tax_rate = tax_rate /100
print(" ")

Subtotal = price * Quantity
print(f"Subtotal : %{Subtotal}")

tax = tax_rate * Subtotal
tax_element = str(tax)

print(f"Tax : $", tax_element[:4])


total = tax + Subtotal
total_element = str(total)
print(f"Total : $", total_element[:4])
