import uuid


class Item:
    status_active = 1
    status_deleted = 0

    def __init__(self, brand, product, color, size, price, buyer="anonymous"):
        self.id = str(uuid.uuid4())
        self.brand = brand
        self.product = product
        self.color = color
        self.size = size
        self.price = price
        self.buyer = buyer
        self.count = 1

    def add_count(self):
        self.count += 1

    def deduct_count(self):
        self.count -= 1

    def get_id(self):
        return self.id

    def get_product(self):
        return self.product

    def __str__(self):
        return f'ID: {self.id}\n' \
               f'Brand: {self.brand}\n' \
               f'Product: {self.product}\n' \
               f'Color: {self.color}\n' \
               f'Size: {self.size}\n' \
               f'Price: {self.price}\n' \
               f'Count: {self.count}\n' \
               f'Buyer: {self.buyer}\n'
