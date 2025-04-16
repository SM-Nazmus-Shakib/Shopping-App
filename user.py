# user.py
from abc import ABC, abstractmethod
from orders import Order

class User(ABC):
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password  # In real app, store hashed password

    @abstractmethod
    def get_role(self):
        pass

class Seller(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
    
    def get_role(self):
        return "seller"

class Customer(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.cart = Order()
    
    def get_role(self):
        return "customer"
    
    def add_to_cart(self, menu, item_name, quantity):
        item = menu.find_item(item_name)
        if item:
            if item.quantity >= quantity:
                self.cart.add_item(item, quantity)
                print(f'{quantity} {item.name}(s) added to cart')
            else:
                print(f'Only {item.quantity} available in stock')
        else:
            print('Item not found!')
    
    def view_cart(self):
        if not self.cart.items:
            print('Your cart is empty')
            return
        
        print('\n***** Your Cart *****')
        print('Item\t\tPrice\tQty\tSubtotal')
        for item, quantity in self.cart.items.items():
            print(f'{item.name}\t${item.price}\t{quantity}\t${item.price * quantity}')
        print(f'\nTotal: ${self.cart.total_price()}')
    
    def pay_bill(self):
        if not self.cart.items:
            print('Your cart is empty')
            return
        
        total = self.cart.total_price()
        print(f'\nTotal amount to pay: ${total}')
        print('Payment successful!')
        # Update stock in real implementation
        self.cart.clear()
        print('Thank you for your purchase!')