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
