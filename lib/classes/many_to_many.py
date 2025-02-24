class Coffee:
    all_coffee = []
    
    def __init__(self, name):
        self.name = name
        self._orders = []
        Coffee.all_coffee.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name_value):
        if hasattr(self, '_name'):
            return
        if not isinstance(name_value, str):
            return
        elif len(name_value) < 3:
            return
        self._name = name_value
    
    # Change to method instead of property
    def orders(self):
        return self._orders
    
    # Change to method instead of property
    def customers(self):
        # Get unique customers who have ordered this coffee
        return list(set([order.customer for order in self._orders]))
    
    def num_orders(self):
        return len(self._orders)
    
    def average_price(self):
        if not self._orders:
            return 0
        return sum([order.price for order in self._orders]) / len(self._orders)

class Customer:
    all_customers = []
    
    def __init__(self, name):
        self.name = name
        self._orders = []
        Customer.all_customers.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name_value):
        if type(name_value) != str or (len(name_value) < 1 or len(name_value) > 15):
            return
        else:
            self._name = name_value
    
    # Change to method instead of property
    def orders(self):
        return self._orders
    
    # Change to method instead of property
    def coffees(self):
        # Get unique coffees ordered by this customer
        return list(set([order.coffee for order in self._orders]))
    
    def create_order(self, coffee, price):
        new_order = Order(self, coffee, price)
        return new_order

class Order:
    all = []
    
    def __init__(self, customer, coffee, price):
        self._customer = None
        self._coffee = None
        self._price = None
        
        self.customer = customer
        self.coffee = coffee
        self.price = price
        
        # Add this order to the lists
        if self._customer and self._coffee:
            self._customer._orders.append(self)
            self._coffee._orders.append(self)
            Order.all.append(self)
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price_value):
        if hasattr(self, '_price') and self._price is not None:
            return
        if not isinstance(price_value, float):
            return
        elif not(1 <= price_value <= 10):
            return
        self._price = price_value
    
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer_value):
        if isinstance(customer_value, Customer):
            self._customer = customer_value
    
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, coffee_value):
        if isinstance(coffee_value, Coffee):
            self._coffee = coffee_value