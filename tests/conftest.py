import pytest

from src.main import Category, CategoryIterator, LawnGrass, Product, Smartphone


@pytest.fixture
def sample_product():
    return Product("Test Product", "Test Description", 100.0, 10)


@pytest.fixture
def sample_product_2():
    return Product("Test Product", "Test Description", 200.0, 5)


@pytest.fixture
def sample_products():
    return [
        Product("Product 1", "Desc 1", 10.0, 5),
        Product("Product 2", "Desc 2", 20.0, 3),
        Product("Product 3", "Desc 3", 30.0, 7),
    ]


@pytest.fixture
def sample_category():
    product_1 = Product("Product1", "Desc1", 100.0, 5)
    product_2 = Product("Product2", "Desc2", 200.0, 10)
    return Category("Test Category", "Test Category Description", [product_1, product_2])


@pytest.fixture
def empty_category():
    return Category("Empty Category", "No products", [])


@pytest.fixture
def not_empty_category():
    return Category("Test Category", "Have products", ["Рыба", "Мясо"])


@pytest.fixture
def category_iterator_fixture(sample_category):
    return CategoryIterator(sample_category)


@pytest.fixture
def smartphone_1_fixture():
    return Smartphone("iphone", "good", 2000, 2, "30%", "13", "256gb", "blue")


@pytest.fixture
def lawngrass_1_fixture():
    return LawnGrass("Сорняк!", "бесполезный", 1, 1000, "Удмуртия", "12 часов", "серый")
