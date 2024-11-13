import pytest

from src.category import Category
from test.test_products import samsung, iphone, product1, product2

category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2])

@pytest.fixture
def first_category():
    return Category(name = "Смартфоны",
                    description = "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                    products = [samsung, iphone]
                    )

def test_category_init(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert len(first_category.list_product) == 3

    assert first_category.category_count == 2
    assert second_category.product_count == 4
