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

