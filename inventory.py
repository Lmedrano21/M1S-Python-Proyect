name = str #variable to store the name of the item
price = float #variable to store the price of the item
quantity = int #variable to store the quantity of the item
validator = True #variable to control the while loop for input validation
total_cost = float #variable to store the total cost of the item

print("Welcome to the inventory management system")

while validator:
    try: #
        name = input("Enter the name of the item: ") #input for the name of the item
        price = float(input("Enter the price of the item: ")) #input for the price of the item, converted to float
        quantity = int(input("Enter the quantity of the item: ")) #input for the quantity of the item, converted to int
        total_cost = price * quantity #calculating the total cost of the item
        validator = False
    except ValueError:
        print("Invalid input. Please enter the correct data type.")
            
print(f"Product: {name} || Price: ${price:.2f} || Quantity: {quantity} || Total Cost: ${total_cost:.2f}") 
#This programm will prompt the user to enter the name, price, and quantity of an item, and then it will calculate and display the total cost of the item. 
# The program also includes input validation to ensure that the user enters the correct data types for price and quantity.