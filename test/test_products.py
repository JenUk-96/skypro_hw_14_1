import unittest

import pytest

from src.category import Category
from src.products import Product, LawnGrass, Smartphone

product1 = Product(
    "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)


@pytest.fixture
def samsung():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )


new_product = Product.new_product(
    {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
)


def test_init(samsung):
    assert samsung.name == "Samsung Galaxy S23 Ultra"
    assert samsung.description == "256GB, Серый цвет, 200MP камера"
    assert samsung.price == 180000.0
    assert samsung.quantity == 5


@pytest.fixture
def iphone():
    return Product(
        name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8
    )


def test_init_product(iphone):
    assert iphone.name == "Iphone 15"
    assert iphone.description == "512GB, Gray space"
    assert iphone.price == 210000.0
    assert iphone.quantity == 8


def test_new_product():
    new_product.price = 0
    assert new_product.price == 180000
    new_product.price = 12000
    assert new_product.price == 12000


def test_str_iphone(iphone):
    assert "Iphone 15, 210000.0 руб. Остаток: 8"


def test_str_samsung(samsung):
    assert "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5"


def test_invalid_sum(product_one, product_grass_1):
    assert "Возникла ошибка TypeError при попытке сложения"


def test_add_smartphone(product_one, product_two):
    assert 198000.0


class TestCaseProduct(unittest.TestCase):

    def test_add(self):
        smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                                 "S23 Ultra", 256, "Серый")
        smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
        grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
        grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
        category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
        with self.assertRaises(TypeError):
            invalid_sum = smartphone1 + grass1
            invalid_sum_2 = grass2 + smartphone2
            invalid_sum_3 = grass2 + category_smartphones

    def test_add_positive(self):
        smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                                 "S23 Ultra", 256, "Серый")
        smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
        grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
        grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
        assert grass1 + grass2 == 16750.0
        assert smartphone1 + smartphone2 == 2580000.0

    def test_creation_str(self):
        product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
        assert str(product1) == 'Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт'
        assert str(product2) == 'Iphone 15, 210000.0 руб. Остаток: 8 шт'
        assert str(product3) == 'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт'

    def test_repr(self):
        product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        assert repr(product1) == "Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"
