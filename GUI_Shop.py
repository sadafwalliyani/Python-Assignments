import PySimpleGUI as sg
import os
import numpy as np

class shopping_list:
    def __init__(self, name_of_customer, address:list, items_list, total_price):
        self.name = name_of_customer
        self.address = address
        self.items_list = items_list
        self.total_price = int(total_price)

    def set_name(self, customer_name):
        self.name = customer_name
        return self.name

    def set_address(self, city, neighborhood):
        self.address = [city, neighborhood]
        return self.address

    def add_item_to_receipt(self, item, price):
        self.items_list.append([item, price])
        return self.items_list

    def get_total_price(self):
        self.total_price = 0
        for i in self.items_list:
            price = i[1]
            self.total_price += price
        return self.total_price

customer1 = shopping_list("1", ["empty", "empty"], [["empty", 0]], 0)
customer2 = shopping_list("2", ["empty", "empty"], [["empty", 0]], 0)
customer3 = shopping_list("3", ["empty", "empty"], [["empty", 0]], 0)
customer4 = shopping_list("4", ["empty", "empty"], [["empty", 0]], 0)
customer5 = shopping_list("5", ["empty", "empty"], [["empty", 0]], 0)

def AddInfoToArray(CustomerInfo, names, citys, neighbors, items, prices):
    names.append(CustomerInfo.name)
    citys.append(CustomerInfo.address[0])
    neighbors.append(CustomerInfo.address[1])
    cnt = 0
    for item in CustomerInfo.items_list:
        if cnt >= 1:
            names.append('')
            citys.append('')
            neighbors.append('')
        items.append(item[0])
        prices.append(str(item[1]))
        cnt += 1

def SaveCustomerInfo(path):
    print(path)
    names = ['Name']
    citys = ['City']
    neighbors = ['NeighborHood']
    items = ['Item']
    prices = ['Price']
    AddInfoToArray(customer1, names, citys, neighbors, items, prices)
    AddInfoToArray(customer2, names, citys, neighbors, items, prices)
    AddInfoToArray(customer3, names, citys, neighbors, items, prices)
    AddInfoToArray(customer4, names, citys, neighbors, items, prices)
    AddInfoToArray(customer5, names, citys, neighbors, items, prices)

    np.savetxt(path, [p for p in zip(names, citys, neighbors, items, prices)], delimiter=',', fmt='%s')


def main():
    # Define the window's contents
    left_col = [[sg.Text('Folder'), sg.In(size=(25,1), enable_events=True ,key='-FOLDER-'), sg.FolderBrowse()]]

    layout = [
            [sg.Text(size=(20,1), text="Customer Number"), sg.Input(key='IN_CUST_NUM', size=(40,1))],
            [sg.Text(size=(20,1), text="Customer Name"), sg.Input(key='IN_CUST_NAME', size=(40,1))],
            [sg.Text(size=(20,1), text="City"), sg.Input(key='IN_CUST_CITY', size=(40,1))],
            [sg.Text(size=(20,1), text="Neighborhood"), sg.Input(key='IN_CUST_NEI', size=(40,1))],
            [sg.Text(size=(20,1), text="Item"), sg.Input(key='IN_CUST_ITEM', size=(40,1))],
            [sg.Text(size=(20,1), text="Price"), sg.Input(key='IN_CUST_PRICE', size=(40,1))],
            [sg.Button('Set Customer Info', key='SetInfo'), sg.Button('Total Price for Customer',key='PriceIndi'), sg.Button('Total Price for All Customers',key='PriceTotal')],
            [sg.Multiline("Please enter customer information\n\n"
                , size=(63,10), reroute_stdout=False, reroute_cprint=True, write_only=True, key='-OUTPUT-'
            )],
            [sg.Column(left_col, element_justification='c'), sg.Button('Quit', key='Quit')]]

    # Create the window
    window = sg.Window('Shopping List', layout, resizable=False)
    filename = ""
    CustomerNum = 0
    CustomerName = ""
    City = ""
    Neighborhood = ""
    Item = ""
    Price = 0
    root = ""
    # Display and interact with the Window using an Event Loop
    while True:
        event, values = window.read()
        
        # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break
        # elif event == 'Browse':
        #     filename = sg.popup_get_file('Enter the file you wish to process')
        #     sg.popup('You entered', filename)

        elif event == '-FOLDER-':
            root = values['-FOLDER-']  

        elif event == 'SetInfo':
            try:
                CustomerNum = int(values['IN_CUST_NUM'])
            except:
                sg.cprint("\nplease enter the customer number that you wants to apply to (1 to 5)\n")
                continue
            if CustomerNum <= 0 or CustomerNum >= 6:
                sg.cprint("\nplease enter the customer number that you wants to apply to (1 to 5).\n")
                continue

            CustomerName = values['IN_CUST_NAME']
            if len(CustomerName) <= 3:
                sg.cprint("please enter a valid name with more than three character\n")
                continue
            
            if CustomerNum == 1:
                sg.cprint("Customer 1 name have been changed successfully to: "+customer1.set_name(CustomerName)+"\n")
            elif CustomerNum == 2:
                sg.cprint("Customer 2 name have been changed successfully to: "+customer2.set_name(CustomerName)+"\n")
            elif CustomerNum == 3:
                sg.cprint("Customer 3 name have been changed successfully to: "+customer3.set_name(CustomerName)+"\n")
            elif CustomerNum == 4:
                sg.cprint("Customer 4 name have been changed successfully to: "+customer4.set_name(CustomerName)+"\n")
            elif CustomerNum == 5:
                sg.cprint("Customer 5 name have been changed successfully to: "+customer5.set_name(CustomerName)+"\n")

            City = values['IN_CUST_CITY']
            Neighborhood = values['IN_CUST_NEI']

            if len(City) <= 3:
                sg.cprint("please enter the name of the city you live in which has more than 3 characters\n")
                continue
            if len(Neighborhood) <= 3:
                sg.cprint("please enter neighborhood which has more than 3 characters\n")
                continue

            if CustomerNum == 1:
                customer1.set_address(City, Neighborhood)
                sg.cprint("the address of the customer "+customer1.name+" have been sat successfully to: City: " 
                    +City+" neighborhood: "+Neighborhood+"\n")
            elif CustomerNum == 2:
                customer2.set_address(City, Neighborhood)
                sg.cprint("the address of the customer "+customer2.name+" have been sat successfully to: City: " 
                    +City+" neighborhood: "+Neighborhood+"\n")
            elif CustomerNum == 3:
                customer3.set_address(City, Neighborhood)
                sg.cprint("the address of the customer "+customer3.name+" have been sat successfully to: City: " 
                    +City+" neighborhood: "+Neighborhood+"\n")
            elif CustomerNum == 4:
                customer4.set_address(City, Neighborhood)
                sg.cprint("the address of the customer "+customer4.name+" have been sat successfully to: City: " 
                    +City+" neighborhood: "+Neighborhood+"\n")
            elif CustomerNum == 5:
                customer5.set_address(City, Neighborhood)
                sg.cprint("the address of the customer "+customer5.name+" have been sat successfully to: City: " 
                    +City+" neighborhood: "+Neighborhood+"\n")

            Item = values['IN_CUST_ITEM']
            try:
                Price = int(values['IN_CUST_PRICE'])
            except:
                sg.cprint("Please enter numerical value for price\n")
                continue

            if CustomerNum == 1:
                sg.cprint(customer1.add_item_to_receipt(Item, Price))
                sg.cprint("item: "+Item+" have been added successfully with the price of: "+str(Price)+"to "+customer1.name+"shopping list"+"\n")
            elif CustomerNum == 2:
                sg.cprint(customer2.add_item_to_receipt(Item, Price))
                sg.cprint("item: "+Item+" have been added successfully with the price of: "+str(Price)+"to "+customer2.name+"shopping list"+"\n")
            elif CustomerNum == 3:
                sg.cprint(customer3.add_item_to_receipt(Item, Price))
                sg.cprint("item: "+Item+" have been added successfully with the price of: "+str(Price)+"to "+customer3.name+"shopping list"+"\n")
            elif CustomerNum == 4:
                sg.cprint(customer4.add_item_to_receipt(Item, Price))
                sg.cprint("item: "+Item+" have been added successfully with the price of: "+str(Price)+"to "+customer4.name+"shopping list"+"\n")
            elif CustomerNum == 5:
                sg.cprint(customer5.add_item_to_receipt(Item, Price))
                sg.cprint("item: "+Item+" have been added successfully with the price of: "+str(Price)+"to "+customer5.name+"shopping list"+"\n")

            path = os.path.join(root, 'info.csv')
            SaveCustomerInfo(path)
            
        elif event == 'PriceIndi':
            path = os.path.join(root, "Shopping_bill.txt")
            f = open(path, "a")
            if CustomerNum == 1:
                total_price = customer1.get_total_price()
                sg.cprint(str(total_price)+"\n")
                sg.cprint("customer "+customer1.name+" total money paid is: "+str(total_price)+"\n")
                print("The total price for", customer1.name, "is:", total_price, "$", file=f)
                f.close()
            elif CustomerNum == 2:
                total_price = customer2.get_total_price()
                sg.cprint(str(total_price)+"\n")
                sg.cprint("customer "+customer2.name+" total money paid is: "+str(total_price)+"\n")
                print("The total price for", customer2.name, "is:", total_price, "$", file=f)
                f.close()
            elif CustomerNum == 3:
                total_price = customer3.get_total_price()
                sg.cprint(str(total_price)+"\n")
                sg.cprint("customer "+customer3.name+" total money paid is: "+str(total_price)+"\n")
                print("The total price for", customer3.name, "is:", total_price, "$", file=f)
                f.close()
            elif CustomerNum == 4:
                total_price = customer4.get_total_price()
                sg.cprint(str(total_price)+"\n")
                sg.cprint("customer "+customer4.name+" total money paid is: "+str(total_price)+"\n")
                print("The total price for", customer4.name, "is:", total_price, "$", file=f)
                f.close()
            elif CustomerNum == 5:
                total_price = customer5.get_total_price()
                sg.cprint(str(total_price)+"\n")
                sg.cprint("customer "+customer5.name+" total money paid is: "+str(total_price)+"\n")
                print("The total price for", customer5.name, "is:", total_price, "$", file=f)
                f.close()
        elif event == 'PriceTotal':
            path = os.path.join(root, "Shoppinglist_bill.txt")
            f = open(path, "a")
            all_customer_total_prices = float(customer1.get_total_price() + 
            customer2.get_total_price() + 
            customer3.get_total_price() + 
            customer4.get_total_price() + 
            customer5.get_total_price())
            sg.cprint("total customer money paid is: "+str(all_customer_total_prices)+"\n")
            print("The total price for all customer is:", all_customer_total_prices, "$", file=f)
            f.close()
    
    # adding my code
    # Define the columns of the table
table_columns = ['Name', 'City', 'Neighborhood', 'Item', 'Price']

# Create an empty table with the defined columns
table = sg.Table(values=[['']*len(table_columns)], headings=table_columns, max_col_width=25, auto_size_columns=True,
                justification='center', alternating_row_color='lightblue', size=(None, None), key='TABLE')

# Add the table to the layout
layout = [    [sg.Text(size=(20,1), text="Customer Number"), sg.Input(key='IN_CUST_NUM', size=(40,1))],
    [sg.Text(size=(20,1), text="Customer Name"), sg.Input(key='IN_CUST_NAME', size=(40,1))],
    [sg.Text(size=(20,1), text="City"), sg.Input(key='IN_CUST_CITY', size=(40,1))],
    [sg.Text(size=(20,1), text="Neighborhood"), sg.Input(key='IN_CUST_NEI', size=(40,1))],
    [sg.Text(size=(20,1), text="Item"), sg.Input(key='IN_ITEM', size=(40,1))],
    [sg.Text(size=(20,1), text="Price"), sg.Input(key='IN_PRICE', size=(40,1))],
    [sg.Button('Add Item'), sg.Button('Remove Item'), sg.Button('Save'), sg.Button('Print')],
    [table],
    [sg.Text(size=(20,1), text="Total Paid Amount"), sg.Text(key='TOTAL_PAID_AMOUNT', size=(40,1))]
]

# Create the window
window = sg.Window('Shopping List', layout)


            
        # Output a message to the window
        

        #window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI")

    # Finish up by removing from the screen
window.close()
        
    

main()

