from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @abstractmethod
    def __add__(self, other):
        pass


class MixinLog:

    def __init__(self):
        self.__repr__()

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"


class Product(MixinLog, ABC):
    """Класс продукт, который обладает общими свойствами"""

    name: str  # Название продукта
    description: str  # Описание продукта
    price: float  # Цена продукта
    quantity: int  # Количество продукта

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""

        if quantity == 0:
            raise ValueError("Товар с нулевым значением не может быть добавлен.")

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()
        print(repr(self))

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float):
        if value > 0:
            self.__price = value
        elif value <= 0:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, product_data):
        name = product_data.get("name")
        description = product_data.get("description")
        price = product_data.get("price")
        quantity = product_data.get("quantity")
        return cls(name, description, price, quantity)

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт"

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError
        else:
            add = self.__price * self.quantity + other.price * other.quantity
            return add


class Smartphone(Product):
    """Подкласс Смартфон"""

    efficiency: str  # Эффективность
    model: str  # Модель телефона
    memory: int  # Объем памяти телефона
    color: str  # Цвет конткретного телефона

    def __init__(self, name, description, price, quantity, efficiency: float, model: str, memory: int, color: str):
        """Метод для инициализации экземпляра класса Смартфон. Задаем значения атрибутам экземпляра"""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        super().__add__(other)
        if not isinstance(other, Smartphone):
            raise TypeError
        else:
            add = self.price * self.quantity + other.price * other.quantity
            return add


class LawnGrass(Product):
    """Подкласс Трава газонная"""

    country: str  # Страна-производитель
    germination_period: int  # Срок прорастания
    color: str  # Цвет травы

    def __init__(self, name, description, price, quantity, country: str, germination_period: int, color: str):
        """Метод для инициализации экземпляра класса Трава газонная. Задаем значения атрибутам экземпляра"""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        super().__add__(other)
        if not isinstance(other, LawnGrass):
            raise TypeError
        else:
            add = self.price * self.quantity + other.price * other.quantity
            return add
