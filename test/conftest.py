import pytest

from src.category import Category
from src.products import Product


@pytest.fixture()
def product_one():
    return Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )


@pytest.fixture()
def product_two():
    return Product("Nokia228", "5TB, Серый цвет, 999MP камера", 1800000.0, 1)


@pytest.fixture()
def product_tree():
    return Product("MSI GF 76 Katana", "512GB, Черный цвет, 16gb ОЗУ, Win11", 79900, 3)


@pytest.fixture()
def product_grass_1():
    return Product("Газонная трава", "Элитная трава для газона", 500.0, 20)


@pytest.fixture()
def product_grass_2():
    return Product("Газонная трава 2", "Выносливая трава", 450.0, 15)


@pytest.fixture()
def no_product():
    return


@pytest.fixture()
def second_category():
    return Category(
        name="Техника",
        description="Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        products=[
            Product(
                "Samsung Galaxy S23 Ultra",
                "256GB, Серый цвет, 200MP камера",
                180000.0,
                5,
            ),
            Product("Nokia228", "5TB, Серый цвет, 999MP камера", 1800000.0, 1),
            Product(
                "MSI GF 76 Katana", "512GB, Черный цвет, 16gb ОЗУ, Win11", 79900, 3
            ),
        ],
    )


@pytest.fixture
def firs_category():
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        products=[
            Product("MSI GF 76 Katana", "512GB, Черный цвет, 16gb ОЗУ, Win11", 79900, 3)
        ],
    )


@pytest.fixture
def category_grass():
    return Category(
        name="Газонная трава",
        description="Элитная трава для газона",
        products=[
            Product("Газонная трава", "Элитная трава для газона", 500.0, 20),
            Product("Газонная трава 2", "Выносливая трава", 450.0, 15),
        ],
    )


@pytest.fixture
def product_apple() -> Product:
    return Product("apple", "sweet", 129, 15)


@pytest.fixture
def category_food() -> Category:
    return Category("food", "some food", ["apple", "banana", "meat", "milk", "eggs"])


@pytest.fixture
def lst_products() -> list:
    return []


@pytest.fixture
def category_magazines() -> Category:
    return Category("magazines", "sth to read", ["magazines", "newspapers", "book"])


@pytest.fixture
def str_exp() -> list:
    return ["Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.",
            "Iphone 15, 210000.0 руб. Остаток: 8 шт.",
            "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."]
