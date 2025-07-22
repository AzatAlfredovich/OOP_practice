import pytest

from src.main import Category, Product


@pytest.fixture
def sample_product():
    return Product("Test Product", "Test Description", 100.0, 10)


@pytest.fixture
def sample_products():
    return [
        Product("Product 1", "Desc 1", 10.0, 5),
        Product("Product 2", "Desc 2", 20.0, 3),
        Product("Product 3", "Desc 3", 30.0, 7),
    ]


@pytest.fixture
def sample_category(sample_products):
    return Category("Test Category", "Test Category Description", sample_products)


@pytest.fixture
def empty_category():
    return Category("Empty Category", "No products", [])
