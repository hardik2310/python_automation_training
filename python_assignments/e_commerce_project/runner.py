from e_commerce_project.item_package.item_module import Item
from e_commerce_project.shopping_cart.shopping_cart_module import ShoppingCart

item1 = Item(description='Shirt Description')
item2 = Item(description='Pent Description')

print()
print(item1.display_description)
print(item2.display_description)

# item1 = item2
# print(item1.display_description) => Pent Description
# print(item2.display_description) => Pent Description

item1 = Item(item_id=1001, quantity=2, price=400, description='Shirt Description', )
item2 = Item(item_id=1002, quantity=10, price=300, description='Pent Description')

final_item1_price = item1.quantity * item1.price
final_item2_price = item2.quantity * item2.price

print('\nPrice for item2 : ', final_item1_price)
print('Final price for Item 1 after discount:', ShoppingCart.discount(item1.quantity, final_item1_price))

print('\nPrice for item 2: ', final_item2_price)
print('Final price for Item 2 after discount:', ShoppingCart.discount(item2.quantity, final_item2_price))
