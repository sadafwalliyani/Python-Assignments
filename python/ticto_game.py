class Customer:
    def __init__(self, name, address, shopping_list, total_paid):
        self.name = name
        self.address = address
        self.shopping_list = shopping_list
        self.total_paid = total_paid

    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def add_item(self, item, price):
        self.shopping_list.append((item, price))
        self.total_paid += price

    def get_total_paid(self):
        return self.total_paid

customers = []

def create_customer(name, city, neighborhood):
    address = (city, neighborhood)
    shopping_list = []
    total_paid = 0
    customers.append(Customer(name, address, shopping_list, total_paid))

def set_name(index, name):
    customers[index].set_name(name)

def set_address(index, city, neighborhood):
    address = (city, neighborhood)
    customers[index].set_address(address)

def add_item(index, item, price):
    customers[index].add_item(item, price)

def get_total_paid(index):
    return customers[index].get_total_paid()

print(create_customer)

