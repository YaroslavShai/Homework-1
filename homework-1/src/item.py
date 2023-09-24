class Item:
    all = None
    pay_rate = None
    def __init__(self, name, price, quanity):
        self.name = name
        self.price = price
        self.quanity = quanity

    def calculate_total_price(self):
        total_price = self.price * self.quanity

        return total_price

    def apply_discount(self):
        self.price *= self.pay_rate







