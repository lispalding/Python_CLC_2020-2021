# PROGRAM NAME: Lisette_Spalding__Cash_Register__09-18-2020.py
# PROGRAM PURPOSE: To print a (fake) bill of sale.
# MADE BY: Lisette Spalding
# DATE LAST MODIFIED: 09-18-2020
# PYTHON VER. USED: Python 3.8

# !! NOTE !!: Please run program in Windows Command Line

# Declaring variables

# Declaring item price variables & items bought
itemBought1 = "Persona 5 Royal"
itemBought2 = "Catherine: Full Body"
itemPrice1 = 39.99 # Both items 1 and 2 cost this
itemBought3 = "Final Fantasy XII Remake"
itemPrice2 = 44.99
itemBought4 = "Amiibo: Cloud Strife (Final Fantasy XII)"
itemPrice3 = 33.00
itemBought5 = "Amiibo: Urbosa (Legend of Zelda: Breath of the Wild)"
itemBought6 = "Amiibo: Mipha (Legend of Zelda: Breath of the Wild)"
itemPrice4 = 15.99 # Both items 5 and 6 cost this
itemBought7 = "Amiibo: Toon Link (Legend of Zelda)"
itemPrice5 = 17.55
# Total of items bought would be: 7
itemNum = 7

# Declaring how to calculate the subTotal
subTotal = itemPrice1*2 + itemPrice2 + itemPrice3 + itemPrice4*2 + itemPrice5

# Declaring a tax rate
taxRate = 0.07

# Declaring tax amount
taxAmount = round(taxRate*subTotal, 2)
# round makes it so that my decimal place is rounded to the place I desire!!

# Declaring how to calculate the total price
totalPrice = subTotal + taxAmount

# And now on to declaring the style variables

# Line Variables
billLine1 = " _______________________->"
billLine2 = "<-_______________________"
itemLine1 = "------------------"
taxLine = "---------------------"
priceLine = "--------------------"
subLine = "----------------------"
itemLine2 = "--------------------"
divider = "|----------------------------------------------------------------|"
endLine = "|________________________________________________________________|"

# Printing out what I want...
print(billLine1,"Bill Of Sale",billLine2)
print("|",itemBought1,itemLine1+"---------------------",str(itemPrice1)+"$","|")
print("|",itemBought2,itemLine1+"----------------",str(itemPrice1)+"$","|")
print("|",itemBought3,itemLine1+"------------",str(itemPrice2)+"$","|")
print("|",itemBought4,"---------------",str(itemPrice3)+"$","|")
print("|",itemBought5,"--",str(itemPrice4)+"$","|")
print("|",itemBought6,"---",str(itemPrice4)+"$","|")
print("|",itemBought7,itemLine1+"-",str(itemPrice5)+"$","|")
print("|",itemLine2,"Number of Items:  "+str(itemNum)+" ",itemLine2,"|")
print(divider)
print("|",taxLine, "Tax Price:  "+str(taxAmount)+"$",taxLine,"|")
print("|",subLine,"SubTotal: "+str(subTotal)+"$",subLine,"|")
print(divider)
print("|",priceLine,"Total Price: "+str(totalPrice)+"$",priceLine,"|")
print(endLine)
