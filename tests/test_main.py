from unittest.mock import patch

import pytest

from src.main import Category, CategoryIterator, Product


# Тест на инициализацию класса Продукт
def test_product_initialization(sample_product):
    assert sample_product.name == "Test Product"
    assert sample_product.description == "Test Description"
    assert sample_product.price == 100.0
    assert sample_product.quantity == 10


# Тест на назначение цены
def test_price_property(sample_product):
    assert sample_product.price == 100.0


# Тест на изменение цены
def test_price_setter_valid(sample_product):
    sample_product.price = 150.0
    assert sample_product.price == 150.0


# Тест на неизменение цены, если она отрицательная
def test_price_setter_negative(sample_product, capsys):
    sample_product.price = -50.0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" == captured.out.strip()
    assert sample_product.price == 100.0  # Цена не изменилась


# Тест на неизменение цены, если она нулевая
def test_price_setter_zero(sample_product, capsys):
    sample_product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" == captured.out.strip()
    assert sample_product.price == 100.0  # Цена не изменилась


# Тест на изменение цены
@patch("builtins.input", return_value="y")
def test_price_decrease_confirmed(mock_input, sample_product):
    sample_product.price = 100.0
    assert sample_product.price == 100.0


# Тест на неизменение цены
@patch("builtins.input", return_value="n")
def test_price_decrease_rejected(mock_input, sample_product, capsys):
    sample_product.price = 80.0
    captured = capsys.readouterr()
    assert "Изменение цены отменено" in captured.out
    assert sample_product.price == 100.0  # Цена не изменилась


# Тест на дублирование продуктов в классе Продукт
def test_new_product_no_duplicates():
    product_data = {"name": "New Product", "description": "New Desc", "price": 200.0, "quantity": 5}
    product = Product.new_product(product_data, [])
    assert product.name == "New Product"
    assert product.price == 200.0


# Тест на новый продукт-дубль
def test_new_product_with_duplicates():
    existing_product = Product("Existing Product", "Old Desc", 150.0, 3)
    product_data = {"name": "Existing Product", "description": "New Desc", "price": 200.0, "quantity": 5}
    result = Product.new_product(product_data, [existing_product])
    assert result == existing_product
    assert result.quantity == 5  # Количество обновилось
    assert result.price == 200.0  # Выбрана максимальная цена


# Тест неверного типа продукта
def test_if_product_not_type_product():
    with pytest.raises(TypeError):
        c = Category("Electronics", "TVs and more", [])
        c.add_product("a")
    Category.category_count = 0
    Category.product_count = 0


# Тест для верного сложения в классе Продукт
def test_add_method_in_product_class(sample_product, sample_product_2):
    assert sample_product + sample_product_2 == 2000


# Тест для неверного сложения в классе Продукт
def test_add_method_error_in_product_class(sample_product, sample_product_2):
    with pytest.raises(TypeError):
        assert sample_product + 1


# Тест на инициализацию класса Категория
def test_initialization(sample_category):
    assert sample_category.name == "Test Category"
    assert sample_category.description == "Test Category Description"
    assert len(sample_category._Category__products) == 2
    assert Category.category_count == 1
    assert Category.product_count == 2


# Тест на добавление продукта в Категорию
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


# Тест на вывод описания продукта в Категории
def test_add_method_in_category_class(sample_product):
    assert str(sample_product) == "Test Product, 100.0 руб. Остаток: 10 шт."


# Тест на получение списка продуктов
def test_get_products(not_empty_category):
    assert Category.get_products(not_empty_category) == ["Рыба", "Мясо"]


# Тест на инициализацию класса ИтераторКатегории
def test_iterator_initialization(not_empty_category):
    assert not_empty_category.get_products() == ["Рыба", "Мясо"]


# Тест на выдачу продуктов поочередно
def test_category_iterator(category_iterator_fixture):
    assert category_iterator_fixture._index == 0
    assert next(category_iterator_fixture).name == "Product1"
    assert next(category_iterator_fixture).name == "Product2"
    with pytest.raises(StopIteration):
        assert next(category_iterator_fixture)


# Тест на строковое представление Категории
def test_str_category(sample_category):
    assert str(sample_category) == "Test Category, количество продуктов: 15 шт."


# Тест на работу итератора
def test_iter_returns_self(sample_category):
    new_example = CategoryIterator(sample_category)
    assert new_example.__iter__() is new_example


# Тест на инициализацию дочернего класса Смартфон
def test_smartphone_initialization(smartphone_1_fixture):
    assert smartphone_1_fixture.name == "iphone"
    assert smartphone_1_fixture.description == "good"
    assert smartphone_1_fixture.price == 2000
    assert smartphone_1_fixture.quantity == 2
    assert smartphone_1_fixture.efficiency == "30%"
    assert smartphone_1_fixture.model == "13"
    assert smartphone_1_fixture.memory == "256gb"
    assert smartphone_1_fixture.color == "blue"


# Тест на строковое представление класса Смартфон
def test_smartphone_category(smartphone_1_fixture):
    assert str(smartphone_1_fixture) == "iphone, 2000 руб. Остаток: 2 шт. | Модель: 13, Память: 256gb, Цвет: blue"


# Тест на инициализацию дочернего класса ГазоннаяТрава
def test_lawngrass_initialization(lawngrass_1_fixture):
    assert lawngrass_1_fixture.name == "Сорняк!"
    assert lawngrass_1_fixture.description == "бесполезный"
    assert lawngrass_1_fixture.price == 1
    assert lawngrass_1_fixture.quantity == 1000
    assert lawngrass_1_fixture.country == "Удмуртия"
    assert lawngrass_1_fixture.germination_period == "12 часов"
    assert lawngrass_1_fixture.color == "серый"


# Тест на строковое представление класса ГазоннаяТрава
def test_lawngrass_category(lawngrass_1_fixture):
    assert str(lawngrass_1_fixture) == "Сорняк!, 1 руб. Остаток: 1000 шт. | Период роста: 12 часов, Страна: Удмуртия"


# Тест на строковое представление класса-миксина №1
def test_logger_mixin_str():
    product = Product("SomeItem", "Description", 1000.0, 12)
    assert str(product) == "SomeItem, 1000.0 руб. Остаток: 12 шт."


# Тест на строковое представление класса-миксина №2
def test_logger_mixin_str_2(capsys):
    Product("SomeItem", "Description", 1000.0, 12)
    message = capsys.readouterr()
    assert (
        message.out.strip()
        == "Создан объект класса Product с аргументами: ('SomeItem', 'Description', 1000.0, 12), {}"
    )


# Тест на строковое представление класса Продукт для разработчика
def test_product_repr():
    product = Product("Кофе", "Арабика средней обжарки", 150.0, 10)
    expected_repr = "Product('Кофе', 'Арабика средней обжарки', 150.0, 10)"
    assert repr(product) == expected_repr, f"Ошибка: ожидалось '{expected_repr}', получено '{repr(product)}'"


# Тест на нулевое количество продукта
def test_no_quantity_in_product():
    with pytest.raises(ValueError):
        Product("Existing Product", "Old Desc", 150.0, 0)


# Тест на нулевое количество списка продуктов
def test_in_category_no_total_quantity_product(capsys):
    p = Product("Valid", "Описание", 100.0, 1)
    category = Category("Категория", "Тест", [])

    p_zero = object.__new__(Product)
    p_zero.name = "Zero"
    p_zero.description = "Ошибка"
    p_zero._Product__price = 100.0
    p_zero.quantity = 0

    category.add_product(p_zero)

    captured = capsys.readouterr()
    assert "Обработка добавления товара завершена." in captured.out
    assert "Нельзя добавить товар с нулевым количеством" in captured.out


# Тест на средний ценник
def test_category_middle_price_empty():
    category = Category("Пустая", "Без товаров", [])
    assert category.middle_price() == 0
