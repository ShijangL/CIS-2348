# Shijang Lin PSID: 2018904

# zyLab 10.19

from os import system

system('cls')


class ItemToPurchase:
    def __init__(self, name="none", price=0, quantity=0, description="none"):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity
        self.item_description = description

    def print_item_cost(self):
        cost_string = f'{self.item_name} {self.item_quantity} @ ${self.item_price:.0f} = ' \
                      f'${self.item_price * self.item_quantity:.0f}'
        print(cost_string)
        cost = self.item_quantity * self.item_price
        return cost_string, cost

    def print_item_description(self):
        string = f'{self.item_name}: {self.item_description}.'
        print(string, end=' ')
        return string


class ShoppingCart:
    def __init__(self, name="none", date="January 1, 2016"):
        self.customer_name = name
        self.current_date = date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self):
        flag = False
        print('REMOVE ITEM FROM CART', end='\n')
        item_name = str(input('Enter name of item to remove:\n'))
        for i in self.cart_items:
            if i.item_name == item_name:
                flag = True
                self.cart_items.remove(i)
        if not flag:
            print('Item not found in cart. Nothing removed.')

    def modify_item(self):
        flag = False
        print('CHANGE ITEM QUANTITY', end='\n')
        item_name = str(input('Enter the item name:\n'))
        new_quantity = int(input('Enter the new quantity:\n'))
        for i in self.cart_items:
            if i.item_name == item_name:
                i.item_quantity = new_quantity
                flag = True
        if not flag:
            print('Item not found in cart. Nothing modified.')

    def get_num_items_in_cart(self):
        num = 0
        for i in self.cart_items:
            num += i.item_quantity
        return num

    def get_cost_of_cart(self):
        cost = 0
        for i in self.cart_items:
            cost += (i.item_price * i.item_quantity)
        return cost

    def print_total(self):
        print('OUTPUT SHOPPING CART', end='\n')
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}", end="\n")
        print(f"Number of Items: {self.get_num_items_in_cart()}", end='\n\n')
        if len(self.cart_items) == 0:
            print(f"SHOPPING CART IS EMPTY")
        else:
            for i in self.cart_items:
                print(f'{i.item_name} {i.item_quantity} @ ${i.item_price:.0f} = ${i.item_quantity * i.item_price:.0f}')
        print(f'\nTotal: ${self.get_cost_of_cart():.0f}', end='\n')

    def print_descriptions(self):
        print("OUTPUT ITEMS' DESCRIPTIONS")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}", end='\n')
        if len(self.cart_items) == 0:
            print(f"SHOPPING CART IS EMPTY")
        else:
            print('\nItem Descriptions', end='\n')
            for i in self.cart_items:
                print(f'{i.item_name}: {i.item_description}', end='\n')


def print_menu(cart):
    customer_cart = cart
    letter = "arcioq"
    command = " "
    menu = ('\nMENU\n'
            'a - Add item to cart\n'
            'r - Remove item from cart\n'
            'c - Change item quantity\n'
            'i - Output items\' descriptions\n'
            'o - Output shopping cart\n'
            'q - Quit\n')

    while command != 'q':
        print(menu, end='\n')

        command = input('Choose an option:')
        print()
        while command not in letter:
            command = input('Choose an option:\n')
        if command == 'a':
            print('\nADD ITEM TO CART', end='\n')
            item_name = str(input('Enter the item name:'))
            item_description = str(input('\nEnter the item description:'))
            item_price = float(input('\nEnter the item price:'))
            item_quantity = int(input('\nEnter the item quantity:\n'))
            cartitem = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            customer_cart.add_item(cartitem)
        if command == 'r':
            customer_cart.remove_item()
        if command == 'c':
            customer_cart.modify_item()
        if command == 'i':
            customer_cart.print_descriptions()
        if command == 'o':
            customer_cart.print_total()


if __name__ == '__main__':
    print("Enter customer's name:")
    cname = input()
    print("Enter today's date:")
    cdate = input()
    print()
    print(f'Customer name: {cname}', end='\n')
    print(f"Today's date: {cdate}", end='\n')

    newcart = ShoppingCart(cname, cdate)
    print_menu(newcart)
