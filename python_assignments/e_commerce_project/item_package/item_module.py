class Item:

    def __init__(self, item_id=None, description=None, quantity=None, price=None):
        self.id = item_id
        self.desc = description
        self.quantity = quantity
        self.price = price

    @property
    def display_description(self):
        return self.desc
