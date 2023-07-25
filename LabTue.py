#1. Define a variable named "price" and set its value to the cost of the item the customer is purchasing (e.g., $2.99).
price = float(input("Enter the price:"))
#2. Define a variable named "quantity" and set its value to the number of items the customer is purchasing (e.g., 3).
quantity = int(input("Enter the quantity:"))
#3. Define a variable named "tax_rate" and set its value to the tax rate in your area (e.g., 7.5%).
tax_rate = 0.075
#4. Calculate the subtotal by multiplying the price by the quantity and store the result in a variable named "subtotal".
subtotal = price * quantity
#5. Calculate the tax by multiplying the subtotal by the tax rate (in decimal form, e.g., 0.075) and store the result in a variable named "tax".
tax = subtotal * tax_rate
#6. Calculate the total cost by adding the subtotal and the tax, and store the result in a variable named "total".
Total = subtotal + tax
#7. Print the subtotal, tax, and total costs, formatted as currency (e.g., $8.97 for the total cost).
print("Price of item:${}".format(price))
print("quantity:",quantity)
print("Tax rate:{}%".format(tax_rate))
print("Subtotal is : ${}".format(subtotal))
print("Tax is :${}".format(tax))
print("Toatal is: ${}".format(Total))
