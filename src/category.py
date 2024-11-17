from src.products import Product


class Category:

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name: str = name
        self.description: str = description
        self.products: list = products
        self.category_count += 1
        self.product_count = len(products)
