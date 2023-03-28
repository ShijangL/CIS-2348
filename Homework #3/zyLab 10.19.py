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

    def add_item(self):
        print('\nADD ITEM TO CART', end='\n')
        item_name = str(input('Enter the item name:'))
        item_description = str(input('\nEnter the item description:'))
        item_price = float(input('\nEnter the item price:'))
        item_quantity = int(input('\nEnter the item quantity:\n'))
        self.cart_items.append(ItemToPurchase(item_name, item_price, item_quantity, item_description))

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

