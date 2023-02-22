class ShoppingCart:

    def __init__(self):
        pass

    @staticmethod
    def discount(quantity, final_price):
        if quantity == 2:
            return final_price - ((final_price * 10)/100)
        elif 3 <= quantity <= 5:
            return final_price - ((final_price * 15) / 100)
        elif quantity > 5:
            return final_price - ((final_price * 25) / 100)