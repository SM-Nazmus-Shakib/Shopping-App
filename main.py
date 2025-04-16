
from user import Customer, Seller
from menu import Menu, MenuItem
from orders import Order

def customer_menu(customer):
    menu = Menu()
    while True:
        print('\nCustomer Menu:')
        print('1. View Products')
        print('2. Add to Cart')
        print('3. View Cart')
        print('4. Checkout')
        print('5. Exit')
        
        choice = input('Enter Your Choice: ')
        
        if choice == '1':
            menu.show_menu()
        elif choice == '2':
            item_name = input('Enter item name: ')
            quantity = int(input('Enter quantity: '))
            customer.add_to_cart(menu, item_name, quantity)
        elif choice == '3':
            customer.view_cart()
        elif choice == '4':
            customer.pay_bill()
        elif choice == '5':
            break
        else:
            print('Invalid Choice!')

def admin_menu(seller):
    menu = Menu()
    
    while True:
        print('\nSeller Menu:')
        print('1. Add Product')
        print('2. Remove Product')
        print('3. View Products')
        print('4. Exit')
        
        choice = input('Enter Your Choice: ')
        
        if choice == '1':
            name = input('Enter product name: ')
            price = float(input('Enter price: '))
            quantity = int(input('Enter quantity: '))
            menu.add_menu_item(MenuItem(name, price, quantity))
            print('Product added successfully!')
        elif choice == '2':
            name = input('Enter product name to remove: ')
            menu.remove_item(name)
        elif choice == '3':
            menu.show_menu()
        elif choice == '4':
            break
        else:
            print('Invalid Choice!')

def main():
    users = []
    
    while True:
        print('\nWelcome to our App!')
        print('1. Customer Login/Register')
        print('2. Seller Login/Register')
        print('3. Exit')
        
        choice = input('Enter Your Choice: ')
        
        if choice == '1':
            email = input('Enter email: ')
            password = input('Enter password: ')
            # In real app, check if user exists, else register
            customer = Customer("Customer", email, password)
            customer_menu(customer)
        elif choice == '2':
            email = input('Enter email: ')
            password = input('Enter password: ')
            # In real app, check if user exists, else register
            seller = Seller("Seller", email, password)
            admin_menu(seller)
        elif choice == '3':
            break
        else:
            print('Invalid Choice!')

if __name__ == "__main__":
    main()