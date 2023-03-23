# Shijang Lin PSID: 2018904

# zyLab 10.17

class ItemToPurchase:

    def __init__(self, name="none", price=0, quantity=0):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity

    def print_item_cost(self):
        print(
            f'{self.item_name} {self.item_quantity} @ ${self.item_price:.0f} = $'
            f'{self.item_price * self.item_quantity:.0f}')


if __name__ == '__main__':
    print('Item 1')
    print('Enter the item name:')
    item1_name = input()
    print('Enter the item price:')
    item1_price = float(input())
    print('Enter the item quantity:')
    item1_quantity = int(input())
    print()

    item1 = ItemToPurchase(item1_name, item1_price, item1_quantity)

    print('Item 2')
    print('Enter the item name:')
    item2_name = input()
    print('Enter the item price:')
    item2_price = float(input())
    print('Enter the item quantity:')
    item2_quantity = int(input())

    item2 = ItemToPurchase(item2_name, item2_price, item2_quantity)

    print()
    print('TOTAL COST')
    item1.print_item_cost()
    item2.print_item_cost()
    print()
    print(f'Total: ${(item1_price * item1_quantity) + (item2_price * item2_quantity):.0f}')
