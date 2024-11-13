import pytest

from src.category import Category
from src.products import Product

new_product = Product.new_product(
    {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
)


@pytest.fixture
def first_category(samsung, iphone):
    return Category(name="Смартфоны",
                    description="Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                    products=[samsung, iphone]
                    )


@pytest.fixture
def samsung():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5
    )


@pytest.fixture
def iphone():
    return Product(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8
    )


def test_category_init(first_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert len(first_category.products) == 2


def test_class_category(second_category, firs_category):
    assert second_category.name == "Техника"
    assert second_category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert second_category.category_count == 2
    assert second_category.product_count == 4
    assert len(firs_category.products) == 1
