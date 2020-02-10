# shopping-cart

This program facilitates the grocery store checkout process. Cashier's can type in barcodes, which are linked to a CSV file, and the program will output a receipt. The receipt will be outputted on the user interface and a duplicate copy will be created on the computer in the form of a text file. 

How will the program create the receipts? It will take the barcode and look up all relevant information (names and prices). It will then store said information in a list of dictionareis called "boughtItems" and from there print out a receipt with the correct items and prices. At the end it will print the subtotal, tax amount and total. 

On the receipt one can find the grocery store's name, website, purchase information and a friendly message to the consumer.

Any barcode inputs that do not match an id on the products list in the CSV file will cause an error to appear to the cashier that states, "Invalid entry. Please try again."

The csv package is used in this program.

The python commands you will need to input on your command-line editor are:
  
   #navigating to the correct directory/the path to your file
   cd ~/Desktop/shopping cart 
   
   #setup your environment
   conda create -n shopping-env python=3.7 # (first time only)
   conda activate shopping-env
  
   #run the program
   python shoppingCart.py #to run this program you will need to have downloaded the products.csv in this repository
   #alternatively, if you would like to run the file without a csv you can type python shoppingCartBasic2.py
   
