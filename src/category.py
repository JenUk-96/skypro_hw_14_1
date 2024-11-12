class Category:
    """Класс категорий продуктов"""
    name: str  # Имя категории
    description: str  # Описание категории продукта
    products: list  # Список товаров категории

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        """Метод для инициализации экземпляра класса категорий. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.product_count += len(products)
