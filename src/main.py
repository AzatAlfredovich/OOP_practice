class Product:

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        """
        Строковое отображение объекта Product
        """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """
        Складывание стоимости продуктов
        """
        return self.__price * self.quantity + other.__price * other.quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        # доп.задание при понижении цены (проверка цены)

        current_price = self.__price
        if new_price < current_price:
            confirmation = input(
                f"Цена понижается с {current_price} до {new_price}."
                f"Если хотите понизить цену введите 'y', либо вернуть текущую цену 'n': "
            )
            if confirmation.lower() != "y":
                print("Изменение цены отменено")
                return

        self.__price = new_price

    @classmethod
    def new_product(cls, product_data: dict, existing_products: list = []):
        """
        Создает новый товар с проверкой на дубликаты
        Параметры:
        - product_data: словарь с данными товара
        - existing_products: список существующих товаров для проверки
        Возвращает: объект Product
        """

        name = product_data["name"]
        description = product_data["description"]
        price = float(product_data["price"])
        quantity = int(product_data["quantity"])

        for existing_product in existing_products:
            if existing_product.name.lower() == name.lower():
                existing_product.quantity = quantity  # Объединяем количество
                existing_product.price = max(existing_product.price, price)  # Берём максимальную цену продукта
                print(f"Товар {name} уже существует. Объединено количество и выбрана наибольшая цена")
                return existing_product

        return cls(name, description, price, quantity)  # Если дубликатов нет - создаем новый товар


class Category:

    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products) -> None:

        self.name = name
        self.description = description
        self.__products = products if products else []
        self.__products_count = len(products)  # Счетчик товаров конкретной категории
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        """
        Строковое представление объекта Category
        """
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}\n"
        return products_str

    def add_product(self, product: Product) -> None:
        """
        Добавляет продукт и увеличивает счетчик
        """
        if not isinstance(product, Product):  # ДОБАВЛЕНО: проверка на тип
            raise TypeError("Можно добавить только объект класса Product или его наследника")

        self.__products.append(product)
        Category.product_count += 1

    def get_products(self) -> list[Product]:
        """
        Внутренний метод для доступа к списку продуктов (для итератора)
        """
        return self.__products


class CategoryIterator:
    """
    Итератор для перебора продуктов в категории.
    """

    def __init__(self, category_obj: Category):
        self._products = category_obj.get_products()
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._products):
            product = self._products[self._index]
            self._index += 1
            return product
        raise StopIteration


# if __name__ == '__main__':
#     product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
#     print(str(product1))
#     print(str(product2))
#     print(str(product3))
#
#     category1 = Category(
#         "Смартфоны",
#         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#         [product1, product2, product3]
#     )
#
#     print(str(category1))
#
#     print(category1.products)
#
#     print(product1 + product2)
#     print(product1 + product3)
#     print(product2 + product3)
