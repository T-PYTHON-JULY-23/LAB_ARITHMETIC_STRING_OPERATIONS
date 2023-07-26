
#purchase invoice 
price= 5.75
quantity= 4
tax_rate= 15
subtotal = price*quantity
tax= subtotal*(tax_rate/100)
total= subtotal+tax

print(f"Price of item: ${price}") #استخدامه عشان استغني عن الفواصل بين النص والمتغير
print("Quantity: ",quantity)
print("Tax rate:", tax_rate, "%")
print('\n' )
print("Subtotal: $",subtotal)
print("Tax: $",round(tax,2))
print("Total: $", total)