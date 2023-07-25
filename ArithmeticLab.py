
#purchase invoice 
price= 5.75
quantity= 4
tax_rate= 0.15
subtotal = price*quantity
tax= subtotal*tax_rate
total= subtotal+tax

print("Price of item: $", price)
print("Quantity: ",quantity)
print("Tax rate: ", tax_rate*100, "%")
print('\n' )
print("Subtotal: $",subtotal)
print("Tax: $",round(tax,2))
print("Total: $", total)

