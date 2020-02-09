# shopping_cart.py

#from pprint import pprint

import csv  #import this to read csv files

import time #for built-in pauses
delay = 2 #delay output

import datetime #import datetime 
d = datetime.datetime.now()
x = d.strftime("%B %d, %Y at %I:%M %p") #formatting time help from https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior

#create a list of valid barcodes
barcodes = []   #list
count = 0   #start a count to keep track of lines of the csv file
fhand = open("products.csv", "r")   #products based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017
for line in fhand:  #for loop to print what is in dataframe
       id, name, aisle, department, price, price_per = line.strip().split(",") #strips off \n. delimits by ','
       count +=1
       if count >1:
           barcodes.append(id)  #valid barcodes are type string

#setting up variables for while loop
cont = True

boughtItems = []    #initiate list of dictionaries of bought items noting their name and price to later print on receipt

while cont == True :    #while loop to keep asking for product codes until cashier runs out ("DONE")
    barcode = input("Enter barcode or DONE to finish. ")    #declaring variable barcode--string
    #netsted if/elif/else to evaluate cashier's input(DONE/valid/invalid)
    if barcode == "DONE" or barcode == "done":  #case sensitivity options DONE/done
            break   #breaks while loop. continues with rest of code.

    elif barcode in barcodes:   #for valid barcodes
        fhand = open("products.csv", "r")
        for line in fhand:  #for loop to print what is in dataframe
            id, name, aisle, department, price, price_per = line.strip().split(",") #strips off \n. delimits by ','.
            if barcode == id:
                if price_per == "pound": #nested if/else because if price_per pound, need product weight to calculate price
                    pounds = eval(input("Enter the item's weight in pounds.  "))    #pounds input
                    ppp = float(price) * pounds   #product price calculation
                    boughtItems.append({"name": name,"price": ppp})   
                else:   #if price_per item then the price is what is listed
                    boughtItems.append({"name":name,"price": float(price)})  
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
print("Checkout on", x)    #Checkout at x, which is current time and date
print("--------------------------------")
print()

subtotal = 0    
tax = .0875


template = "${:.2f}"    #formatting template for all $USD amounts. help from https://www.reddit.com/r/learnpython/comments/45c9kw/adding_or_in_python_without_space_in_between_the/

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
f.write("--------------------------------\n Checkout on ")
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





       