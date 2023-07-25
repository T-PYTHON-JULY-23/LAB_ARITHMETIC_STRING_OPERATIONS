#1-Define a variable named "price" and set its value to the cost of the item the customer is purchasing (e.g., $2.99).
price = 2.99

#2-Define a variable named "quantity" and set its value to the number of items the customer is purchasing (e.g., 3).
quantity = 3

#3-Define a variable named "tax_rate" and set its value to the tax rate in your area (e.g., 7.5%).
tax_rate = 7.5

#4-Calculate the subtotal by multiplying the price by the quantity and store the result in a variable named "subtotal

subtotal = price * quantity

#5-Calculate the tax by multiplying the subtotal by the tax rate (in decimal form, e.g., 0.075) and store the result in a variable named "tax".
tax = round(subtotal * tax_rate/100, 2)

#6-Calculate the total cost by adding the subtotal and the tax, and store the result in a variable named "total".
total = subtotal + tax

#7-Print the subtotal, tax, and total costs, formatted as currency (e.g., $8.97 for the total cost).
print(f"Price ot item: ${price}")
print(f"Quantity: {quantity}")
print(f"Tax Rate: {tax_rate}%")
print("---------------------")
print(f"Subtotal: ${subtotal}")
print(f"Tax: ${tax}")
print(f"Total: ${total}")



