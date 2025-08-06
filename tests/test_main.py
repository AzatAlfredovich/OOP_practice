from unittest.mock import patch

import pytest

from src.main import Category, CategoryIterator, Product
from tests.conftest import sample_products

# Тесты для класса Product


def test_product_initialization(sample_product):
    assert sample_product.name == "Test Product"
    assert sample_product.description == "Test Description"
    assert sample_product.price == 100.0
    assert sample_product.quantity == 10


def test_price_property(sample_product):
    assert sample_product.price == 100.0


def test_price_setter_valid(sample_product):
    sample_product.price = 150.0
    assert sample_product.price == 150.0


def test_price_setter_negative(sample_product, capsys):
    sample_product.price = -50.0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" == captured.out.strip()
    assert sample_product.price == 100.0  # Цена не изменилась


def test_price_setter_zero(sample_product, capsys):
    sample_product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" == captured.out.strip()
    assert sample_product.price == 100.0  # Цена не изменилась


@patch("builtins.input", return_value="y")
def test_price_decrease_confirmed(mock_input, sample_product):
    sample_product.price = 100.0
    assert sample_product.price == 100.0


@patch("builtins.input", return_value="n")
def test_price_decrease_rejected(mock_input, sample_product, capsys):
    sample_product.price = 80.0
    captured = capsys.readouterr()
    assert "Изменение цены отменено" in captured.out
    assert sample_product.price == 100.0  # Цена не изменилась


def test_new_product_no_duplicates():
    product_data = {"name": "New Product", "description": "New Desc", "price": 200.0, "quantity": 5}
    product = Product.new_product(product_data, [])
    assert product.name == "New Product"
    assert product.price == 200.0


def test_new_product_with_duplicates():
    existing_product = Product("Existing Product", "Old Desc", 150.0, 3)
    product_data = {"name": "Existing Product", "description": "New Desc", "price": 200.0, "quantity": 5}
    result = Product.new_product(product_data, [existing_product])
    assert result == existing_product
    assert result.quantity == 5  # Количество обновилось
    assert result.price == 200.0  # Выбрана максимальная цена


def test_if_product_not_type_product():
    with pytest.raises(TypeError):
        c = Category("Electronics", "TVs and more", [])
        c.add_product("a")
    Category.category_count = 0
    Category.product_count = 0


def test_add_method_in_product_class(sample_product, sample_product_2):
    assert sample_product + sample_product_2 == 2000


def test_add_method_error_in_product_class(sample_product, sample_product_2):
    with pytest.raises(TypeError):
        assert sample_product + 1


# Тесты для класса Category


def test_initialization(sample_category):
    assert sample_category.name == "Test Category"
    assert sample_category.description == "Test Category Description"
    assert len(sample_category._Category__products) == 2
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_add_product_in_category():
    Category.category_count = 0
    Category.product_count = 0

    p = Product("TV", "Smart TV", 50000.0, 4)
    c = Category("Electronics", "TVs and more", [])

    assert Category.category_count == 1
    assert Category.product_count == 0

    c.add_product(p)

    assert Category.product_count == 1
    assert "TV, 50000.0 руб. Остаток: 4 шт." in c.products


def test_add_method_in_category_class(sample_product):
    assert str(sample_product) == "Test Product, 100.0 руб. Остаток: 10 шт."


def test_get_products(not_empty_category):
    assert Category.get_products(not_empty_category) == ["Рыба", "Мясо"]


def test_iterator_initialization(not_empty_category):
    assert not_empty_category.get_products() == ["Рыба", "Мясо"]


def test_category_iterator(category_iterator_fixture):
    assert category_iterator_fixture._index == 0
    assert next(category_iterator_fixture).name == "Product1"
    assert next(category_iterator_fixture).name == "Product2"
    with pytest.raises(StopIteration):
        assert next(category_iterator_fixture)


def test_str_category(sample_category):
    assert str(sample_category) == "Test Category, количество продуктов: 15 шт."


def test_iter_returns_self(sample_category):
    new_example = CategoryIterator(sample_category)
    assert new_example.__iter__() is new_example


def test_smartphone_initialization(smartphone_1_fixture):
    assert smartphone_1_fixture.name == "iphone"
    assert smartphone_1_fixture.description == "good"
    assert smartphone_1_fixture.price == 2000
    assert smartphone_1_fixture.quantity == 2
    assert smartphone_1_fixture.efficiency == "30%"
    assert smartphone_1_fixture.model == "13"
    assert smartphone_1_fixture.memory == "256gb"
    assert smartphone_1_fixture.color == "blue"


def test_smartphone_category(smartphone_1_fixture):
    assert str(smartphone_1_fixture) == "iphone, 2000 руб. Остаток: 2 шт. | Модель: 13, Память: 256gb, Цвет: blue"


def test_lawngrass_initialization(lawngrass_1_fixture):
    assert lawngrass_1_fixture.name == "Сорняк!"
    assert lawngrass_1_fixture.description == "бесполезный"
    assert lawngrass_1_fixture.price == 1
    assert lawngrass_1_fixture.quantity == 1000
    assert lawngrass_1_fixture.country == "Удмуртия"
    assert lawngrass_1_fixture.germination_period == "12 часов"
    assert lawngrass_1_fixture.color == "серый"


def test_lawngrass_category(lawngrass_1_fixture):
    assert str(lawngrass_1_fixture) == "Сорняк!, 1 руб. Остаток: 1000 шт. | Период роста: 12 часов, Страна: Удмуртия"
