price = 5.99
quantity = 4
tax_rate = 15
subtotal = price * quantity
tax = subtotal * (tax_rate / 100)
total = subtotal + tax
print(f'Price of item: ${price}')
print(f'Quantity:: {quantity}')
print(f'Tax rate: {tax_rate}%')
print("")
print(f'Subtotal: ${round(subtotal,2)}')
print(f'Tax:: ${round(tax,2)}')
print(f'Total: ${round(total,2)}')