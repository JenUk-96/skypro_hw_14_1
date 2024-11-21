import pytest

from src.products import Product

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
        quantity=5
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
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8
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
