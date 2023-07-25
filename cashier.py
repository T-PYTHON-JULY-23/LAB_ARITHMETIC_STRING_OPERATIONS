price = 2.99
quantity = 3
tax_rate = 7.5

subTotal = price * quantity
tax = round(subTotal * tax_rate/100, 2)
total = subTotal + tax

print(f"Price ot item: ${price}")
print(f"Quantity: {quantity}")
print(f"Tax Rate: {tax_rate}%")
print()
print(f"Subtotal: ${subTotal}")
print(f"Tax: ${tax}")
print(f"Total: ${total}")