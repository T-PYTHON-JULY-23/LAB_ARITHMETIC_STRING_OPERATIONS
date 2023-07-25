price = 2.99
quantity = 3
tax_rate = 7.5

subtotal = price * quantity
tax =  round(subtotal * tax_rate/100, 2)
total = subtotal + tax

result1 = "Price of item: ${}\nQuantity: {}\nTax rate: {}%".format(price, quantity, tax_rate)
result2="\nSubtotal: ${}\nTax: ${}\nTotal: ${}".format(subtotal, tax, total)
print(result1)
print(result2)
