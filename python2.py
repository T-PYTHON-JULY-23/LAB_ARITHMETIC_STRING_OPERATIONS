price = 4.16
quantity = 2
tax_rate = 6.5
subtotal = (price*quantity)
tax = round((subtotal*(tax_rate/100)),2)
#rtax=round(tax,2)
total = (subtotal+tax)
#rtotal = round(total)
print("price of item:${0}".format(price))
print("Quantity:",quantity)
print("Tax rate:{0}%".format(tax_rate))


print("Subtotal : $" + str(subtotal))
print("Tax : $" + str (tax)) 
print("Total :$" +str (total))




