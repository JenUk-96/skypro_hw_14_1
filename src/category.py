from src.products import Product


class Category:
    """Класс категорий продуктов"""
    name: str  # Имя категории
    description: str  # Описание категории продукта
    products: list  # Список товаров категории

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        """Метод для инициализации экземпляра класса категорий. Задаем значения атрибутам экземпляра."""
        self.list_product = None
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def products(self):
        return self.__products

    def add_products(self, new_product: Product):
        self.__products.append(new_product)
        Category.category_count += 1

    @property
    def product_list(self):
        product_str = ""
        for product in self.products:
            product_str += (
                f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
            )
        return product_str

    def __str__(self):
        all_quantity = 0
        for i in self.__products:
            all_quantity += i.quantity
        return f"{self.name}, Количество продукта: {all_quantity}\n"
