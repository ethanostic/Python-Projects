standard_demand_price = 10

class Product:
    '''
    Creates a product and it attributes.
    '''

    # Creates the product name and the demand
    def __init__(self, name):
        self.name = name
        self.price = standard_demand_price

    # Update product price
    def update_price(self):
        # self.price = demand * self.price

    # Produces products and deducts from company after updating price
    def produce(self, company, amount):
        self.update_price()
        company.deduct_money(self.price * amount)

class Company:
    '''
    Creates a company and its attributes.
    '''

    # Creates company name and an empty bank account
    def __init__(self, name):
        self.name = name
        self.account = 0

    # Adds money to account
    def add_money(self, money_changed):
        self.account += money_changed

    # Deduct money from account
    def deduct_money(self, money_changed):
        self.account -= money_changed


Ethan = Company("Ethan")

Food = Product("Food")
Food.produce(Ethan, 10)
print(Ethan.account)