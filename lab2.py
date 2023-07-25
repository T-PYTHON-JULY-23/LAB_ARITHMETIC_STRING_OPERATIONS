price = 2.99
quantity = 3
tax_rate = 7.5
subtotal = price * quantity 
tax =  round(subtotal * tax_rate /100 ,2 )
total = subtotal + tax 
print (" ''' \n ")
print("Price of item : $" + str(price))
print ("Quantity :"+ str(quantity))
print("Tax rate :"+str(tax_rate)+"% \n \n")
print ("Sub total : $"+ str(subtotal))
print("Tax : $"+ str(tax))
print("Total : $" + str(total))
print(" \n ''' ")