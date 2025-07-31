from unittest.mock import patch

import pytest

from src.main import Category, Product


# Тесты для класса Product
class TestProduct:
    def test_product_initialization(self, sample_product):
        assert sample_product.name == "Test Product"
        assert sample_product.description == "Test Description"
        assert sample_product.price == 100.0
        assert sample_product.quantity == 10

    def test_price_property(self, sample_product):
        assert sample_product.price == 100.0

    def test_price_setter_valid(self, sample_product):
        sample_product.price = 150.0
        assert sample_product.price == 150.0

    def test_price_setter_negative(self, sample_product, capsys):
        sample_product.price = -50.0
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" == captured.out.strip()
        assert sample_product.price == 100.0  # Цена не изменилась

    def test_price_setter_zero(self, sample_product, capsys):
        sample_product.price = 0
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" == captured.out.strip()
        assert sample_product.price == 100.0  # Цена не изменилась

    @patch("builtins.input", return_value="y")
    def test_price_decrease_confirmed(self, mock_input, sample_product):
        sample_product.price = 100.0
        assert sample_product.price == 100.0

    @patch("builtins.input", return_value="n")
    def test_price_decrease_rejected(self, mock_input, sample_product, capsys):
        sample_product.price = 80.0
        captured = capsys.readouterr()
        assert "Изменение цены отменено" in captured.out
        assert sample_product.price == 100.0  # Цена не изменилась

    def test_new_product_no_duplicates(self):
        product_data = {"name": "New Product", "description": "New Desc", "price": 200.0, "quantity": 5}
        product = Product.new_product(product_data, [])
        assert product.name == "New Product"
        assert product.price == 200.0

    def test_new_product_with_duplicates(self):
        existing_product = Product("Existing Product", "Old Desc", 150.0, 3)
        product_data = {"name": "Existing Product", "description": "New Desc", "price": 200.0, "quantity": 5}
        result = Product.new_product(product_data, [existing_product])
        assert result == existing_product
        assert result.quantity == 5  # Количество обновилось
        assert result.price == 200.0  # Выбрана максимальная цена

    def test_if_product_not_type_product(self):
        with pytest.raises(TypeError):
            c = Category("Electronics", "TVs and more", [])
            c.add_product("a")
        Category.category_count = 0
        Category.product_count = 0


# Тесты для класса Category
class TestCategory:

    def test_initialization(self, sample_category):
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
