# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# AJehle,8.24.2020, Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
import errno

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        AJehle,8.24.2020,Modified code to complete assignment 8
    """
    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        AJehle,8.25.2020,Modified code to complete Assignment08
    """

    def __init__(self, list_of_product_objects):
        self.list_of_product_objects = list_of_product_objects

    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        objFile = open(file_name, 'w')
        for prods in list_of_product_objects:
            objFile.write(prods.product_name + ',' + prods.product_price + '\n')
        objFile.close()

    @staticmethod
    def read_data_from_file(file_name):
        lstTable = []
        try:
            objFile = open(file_name, 'r')
            for row in objFile:
                strData = row.split(",")
                objP = Product(product_name=strData[0].strip(),
                               product_price=strData[1].strip())
                lstTable.append(objP)
            objFile.close()
            print(f'Opened list from: {file_name}')
            return lstTable

        except FileNotFoundError:
            print('No existing file. New catalogue created.')
            return lstTable
        except Exception as e:
            print(f'List not imported. Received error: {e}')
            return lstTable

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Processes data in a list of product objects:

       methods:
           print_menu():

           input_choice(): -> (menu choice)
           
           print_current_products():
           
           add_product(): -> (product name and price)

       changelog: (When,Who,What)
           RRoot,1.1.2030,Created Class
           AJehle,8.25.2020,Modified code to complete Assignment08
       """
    pass

    @staticmethod
    def print_menu():
        """  Display a menu of choices to the user
        :return: nothing
        """
        print('''
            Menu of Options
            1) Display current products
            2) Add new product
            3) Save and Exit      
            ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_choice():
        """ Gets the menu choice from a user
        :return: string
        """
        choice = str(input("Which menu option would you like to perform? [1 to 3] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_products(list_of_rows):
        """ Shows the current products in the list
        :param list_of_product_rows: (list) of products and prices you want to display
        :return: nothing
        """
        print("******* The current products are: *******")
        for prods in list_of_rows:
            print(prods.product_name + ", $" + prods.product_price)
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def add_product(list_of_rows: list):
        product_name = str(input("Which product would you like to add? ")).strip()
        product_price = str(input('What price does ' + product_name + ' have?: $')).strip()
        objP = Product(product_name=product_name,
                       product_price=product_price)
        try:
            list_of_rows.append(objP)
            print(product_name + " added!")
        except:
            print(product_name + " was not successfully added")
        return list_of_rows

    pass
# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)

while True:
# Show user a menu of options
    IO.print_menu()

# Get user's menu option choice
    strChoice = IO.input_choice()
    if strChoice.strip() == '1':
    # Show user current data in the list of product objects
        IO.print_current_products(lstOfProductObjects)

    elif strChoice.strip() == '2':
    # Let user add data to the list of product objects
        lstOfProductObjects = IO.add_product(lstOfProductObjects)

    elif strChoice.strip() == '3':
    # let user save current data to file and exit program
        try:
            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            print("Save successful!")
            break
        except:
            print("List not saved successfully")
    else:
        print("Please select valid option.")
