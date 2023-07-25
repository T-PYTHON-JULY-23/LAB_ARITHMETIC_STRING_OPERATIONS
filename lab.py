#Define a variable named "price" and set its value to the cost of the item the customer is purchasing (e.g., $2.99).
price = 2.99
Quantity= 3
Tax_rate= 7.5

print(f"Price of item: ${price}")
print(f"Quantity: {Quantity}")
print(f"Tax rate: {Tax_rate}%")

subtotal = 2.99 * 3
print(f"Subtotal:  ${subtotal}")
Tax = subtotal * 0.075
print(f"Tax: ${Tax:.2f}")
print(f"Total: ${subtotal + Tax :.2f} ")