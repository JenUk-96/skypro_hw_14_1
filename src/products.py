class Product:
    """Класс продукт, который обладает общими свойствами"""
    name: str  # Название продукта
    description: str  # Описание продукта
    price: float  # Цена продукта
    quantity: int  # Количество продукта

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            print("Цена не должна быть отрицательной или равной 0")
        else:
            self.__price = value

    @classmethod
    def new_product(cls, product_data):
        name = product_data.get("name")
        description = product_data.get("description")
        price = product_data.get("price")
        quantity = product_data.get("quantity")
        return cls(name, description, price, quantity)

    def __repr__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} \n"

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity}"

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity * self.price + other.quantity * other.price

        raise TypeError


class Smartphone(Product):
    """  Подкласс Смартфон """
    efficiency: str  # Эффективность
    model: str  # Модель телефона
    memory: int  # Объем памяти телефона
    color: str  # Цвет конткретного телефона

    def __init__(self, name, description, price, quantity, efficiency: str, model: str, memory: int, color: str):
        """ Метод для инициализации экземпляра класса Смартфон. Задаем значения атрибутам экземпляра """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """ Подкласс Трава газонная """
    country: str  # Страна-производитель
    germination_period: int  # Срок прорастания
    color: str  # Цвет травы

    def __init__(self, name, description, price, quantity, country: str, germination_period: str, color: str, ):
        """ Метод для инициализации экземпляра класса Трава газонная. Задаем значения атрибутам экземпляра """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
