# shopping_cart.py

import time #for built-in pauses
delay = 2 #delay output

import datetime #import datetime 
x = datetime.datetime.now() #assigning variable x for current date

#list of the products in the store
products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50, "price_per": "item"},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99, "price_per": "item"},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49, "price_per": "item"},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99, "price_per": "item"},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99, "price_per": "item"},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99, "price_per": "item"},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50, "price_per": "item"},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25, "price_per": "item"},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50, "price_per": "item"},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99, "price_per": "item"},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99, "price_per": "item"},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50, "price_per": "item"},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00, "price_per": "item"},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99, "price_per": "item"},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50, "price_per": "item"},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50, "price_per": "item"},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99, "price_per": "item"},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50, "price_per": "item"},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99, "price_per": "item"},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25, "price_per": "item"},
    {"id":21, "name": "Organic Bananas", "department": "fruit", "aisle": "produce", "price": .79, "price_per": "pound"}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

#create a list of valid barcodes
barcodes = []   #list
for i in range(len(products)):  #for loop to get barcodes of all products in system
    barcodes.append(str(products[i]["id"])) #appending valid barcodes list with string of all product ids

#setting up variables for while loop
cont = True

boughtItems = []    #initiate list of dictionaries of bought items noting their name and price to later print on receipt

while cont == True :    #while loop to keep asking for product codes until cashier runs out ("DONE")
    barcode = input("Enter barcode or DONE to finish. ")    #declaring variable barcode--string
    #netsted if/elif/else to evaluate cashier's input(DONE/valid/invalid)
    if barcode == "DONE" or barcode == "done":  #case sensitivity options DONE/done
            break   #breaks while loop. continues with rest of code.

    elif barcode in barcodes:   #for valid barcodes
        for i in range(len(products)):  #nested for (and if) to determine correct product
            if barcode == str(products[i]["id"]):   
                if products[i]["price_per"] == "pound": #nested if/else because if price_per pound, need product weight to calculate price
                    pounds = eval(input("Enter the item's weight in pounds.  "))    #pounds input
                    ppp = (products[i]["price"]) * pounds   #product price calculation
                    boughtItems.append({"name":products[i]["name"],"price": ppp})   
                else:   #if price_per item then the price is what is listed
                    boughtItems.append({"name":products[i]["name"],"price": products[i]["price"]})  
    else: #not DONE and not a valid barcode, then invlaid 
        print("Invalid entry. Please try again. ")  #error print


#printing a receipt to the viewer
print()
print()
time.sleep(delay)
print("Great, here is your receipt! ")
print()
print()
time.sleep(delay-1)


#receipt output to command-line
print("--------------------------------")
print("   OLIVER'S LOCAL MARKET   ")    #store name
print("     oliversmarket.com     ")    #store site
print("--------------------------------")
print("Checkout at:", x)    #Checkout at x, which is current time and date
print("--------------------------------")

subtotal = 0    
tax = .0875


template = "${:.2f}"    #formatting template for all $USD amounts. 

for i in range(len(boughtItems)):   #for loop to print aname and price in boughtItems list of dictionaries
    print(boughtItems[i]["name"], "  ", template.format(boughtItems[i]["price"]))
    subtotal += boughtItems[i]["price"] #increases subtotal for each product

print()
print("--------------------------------")

print ("SUBTOTAL: ", template.format(subtotal)) #print subtotal in USD format

taxTotal = tax * subtotal   #tax calculation
print("TAX: ", template.format(taxTotal)) #print tax in USD format

total = subtotal + taxTotal #total calculation
print("TOTAL: ", template.format(total)) #print total in USD format

print("--------------------------------")
print("Thanks for choosing us, neighbor!")  #kind message
print("Please come again. ")
print("--------------------------------")

#creating a txt file for the receipt
filename = "receipts."+ str(x)+".txt"   #the text filename is receipt.currentdate&time
f = open(filename, "w") #create new file with the above filename and open for writing 

#writing all the above receipt into the text file
#text files only take string inputs and only one input per f.write()
#\n is indicative of a carriage return 
f.write("--------------------------------\n   OLIVER'S LOCAL MARKET   \n     oliversmarket.com     \n")
f.write("--------------------------------\n Checkout at:")
f.write(str(x))
f.write("\n--------------------------------\n")
for i in range(len(boughtItems)):
    f.write(boughtItems[i]["name"]) 
    f.write("  ")
    f.write(str(template.format(boughtItems[i]["price"])))
    f.write("\n")
f.write("\n--------------------------------\nSUBTOTAL: ")
f.write(str(template.format(taxTotal)))
f.write("\nTAX: ")
f.write(str(template.format(taxTotal)))
f.write("\nTOTAL: ")
f.write(str(template.format(total)))
f.write("\n--------------------------------\nThanks for choosing us, neighbor!\nPlease come again.\n--------------------------------")
f.close()   #close the file

