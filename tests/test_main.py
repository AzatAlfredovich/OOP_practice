from src.main import Category, Product


# Тесты для класса Product
class TestProduct:
    def test_product_initialization(self, sample_product):
        assert sample_product.name == "Test Product"
        assert sample_product.description == "Test Description"
        assert sample_product.price == 100.0
        assert sample_product.quantity == 10

    def test_product_count_increment(self, sample_product):
        initial_count = Product.product_count
        Product("New Product", "New Desc", 50.0, 2)
        assert Product.product_count == initial_count + 1


# Тесты для класса Category
class TestCategory:
    def test_category_initialization(self, sample_category, sample_products):
        assert sample_category.name == "Test Category"
        assert sample_category.description == "Test Category Description"
        assert sample_category.products == sample_products

    def test_empty_category(self, empty_category):
        assert empty_category.name == "Empty Category"
        assert empty_category.description == "No products"
        assert empty_category.products == []

    def test_category_count_increment(self, sample_category):
        initial_count = Category.category_count
        Category("Another Category", "Desc", [])
        assert Category.category_count == initial_count + 1


# Тесты для подсчета продуктов и категорий
class TestCounters:
    def test_product_counter(self):
        initial_count = Product.product_count
        Product("P1", "D1", 1.0, 1)
        Product("P2", "D2", 2.0, 2)
        assert Product.product_count == initial_count + 2

    def test_category_counter(self):
        initial_count = Category.category_count
        Category("C1", "D1", [])
        Category("C2", "D2", [])
        assert Category.category_count == initial_count + 2

    def test_products_in_category_counter(self, sample_products):
        initial_count = Category.product_count
        Category("Test", "Test", sample_products)
        assert Category.product_count == initial_count + len(sample_products)
