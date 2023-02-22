# PART 1
custName = "Mary Smith wants"
itemDesc = " to purchase a Shirt"
message = custName + itemDesc

print(message)

# PART 2
price = 700
tax = 1.5
quantity = 5

message = message.replace('Shirt', str(quantity) + ' Shirt')
print(message)

total = price * tax * quantity

print('\nTotal cost with tax is : ', total)

# PART 3
outOfStock = True

if quantity > 1:
    message = message + '\'s'

print('\n')
print(message)
if outOfStock:
    print('Item is unavailable')
else:
    print('\nTotal cost with tax is : ', total)
    outOfStock = False

# PART 4
items_list = ['Shirt', 'Pent', 'Shoes', 'Tie']
print('\nCustomer wants to buy', len(items_list), ' items.')
print('1st item in list:', items_list[0])

# What happens if you use index number 4? => gives 'IndexError: list index out of range' error
