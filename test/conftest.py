import pytest

from src.category import Category
from src.products import Product


@pytest.fixture()
def product_one():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture()
def product_two():
    return Product("Nokia228", "5TB, Серый цвет, 999MP камера", 1800000.0, 1)


@pytest.fixture()
def product_tree():
    return Product("MSI GF 76 Katana", "512GB, Черный цвет, 16gb ОЗУ, Win11", 79900, 3)


@pytest.fixture()
def second_category():
    return Category(name='Техника',
                    description="Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                    products=[
                        Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
                        Product("Nokia228", "5TB, Серый цвет, 999MP камера", 1800000.0, 1),
                        Product("MSI GF 76 Katana", "512GB, Черный цвет, 16gb ОЗУ, Win11", 79900, 3),
                        ])


@pytest.fixture
def firs_category():
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        products=[Product("MSI GF 76 Katana", "512GB, Черный цвет, 16gb ОЗУ, Win11", 79900, 3)])
