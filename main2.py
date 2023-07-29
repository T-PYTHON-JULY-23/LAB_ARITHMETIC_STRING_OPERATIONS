
# Define the price of the item the customer is purchasing
price = 2.99

# Define the quantity of the item the customer is purchasing
quantity = 3

# Define the tax rate in decimal form
tax_rate = 7.5

# Calculate the subtotal
subtotal = price * quantity

# Calculate the tax
tax = subtotal * tax_rate/100

# Calculate the total cost, including tax
total_cost = subtotal + tax

# Print the subtotal, tax, and total costs formatted as currency
print("Price of item: $", price)
print("quantity ", quantity)
print ("Tax rate: " , tax_rate)

print("Subtotal: $", subtotal)
print("Tax: $",   round(tax,2))
print("Total Cost: $:", round(total_cost,2))
