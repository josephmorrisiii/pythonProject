# Joseph Morris
#1840300

class ItemToPurchase:
     def __init__(self, item_name = 'none', item_price = 0, item_quantity = 0):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0

     def print_item_cost(self):
        print(self.item_name + " " + str(self.item_quantity) + " @ $"
              + str(self.item_price) +
              " = $" + str(self.item_price * self.item_quantity))


if __name__ == "__main__":
    print("Item 1")
    item_one = ItemToPurchase()
    item_two = ItemToPurchase()

    item_one.item_name = input('Enter the item name:\n')
    item_one.item_price = int(input('Enter the item price:\n'))
    item_one.item_quantity = int(input('Enter the item quantity:\n'))

    print("\nItem 2")
    item_two.item_name = input('Enter the item name:\n')
    item_two.item_price = int(input('Enter the item price:\n'))
    item_two.item_quantity = int(input('Enter the item quantity:\n'))

    print("\nTOTAL COST")

    item_one.print_item_cost()
    item_two.print_item_cost()

    total_cost_of_items = (item_one.item_price * item_one.item_quantity) + (item_two.item_price * item_two.item_quantity)

    print("\nTotal: $" + str(total_cost_of_items))
