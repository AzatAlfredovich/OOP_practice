from abc import ABC, abstractmethod


class InvalidQuantityException(Exception):
    pass


class BaseProduct(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        pass

    @price.setter
    @abstractmethod
    def price(self, value: float) -> None:
        pass


class LoggerMixin:
    def __init__(self, *args, **kwargs):
        print(f"Создан объект класса {self.__class__.__name__} с аргументами: {args}, {kwargs}")


class Product(LoggerMixin, BaseProduct):

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):

        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        super().__init__(name, description, price, quantity)
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r}, {self.description!r}, {self.price}, {self.quantity})"

    def __add__(self, other):
        """
        Складывание стоимости продуктов
        """
        if type(self) != type(other):
            raise TypeError("Можно складывать только объекты одного типа")
        return self.price * self.quantity + other.price * other.quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
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
        Добавление продукта и увеличение счетчика
        """
        try:
            if not isinstance(product, Product):
                raise TypeError("Можно добавить только объект класса Product или его наследника")
            if product.quantity == 0:
                raise InvalidQuantityException("Нельзя добавить товар с нулевым количеством в категорию")

            self.__products.append(product)
            Category.product_count += 1
        except InvalidQuantityException as e:
            print(e)
        else:
            print(f"Товар {product.name} успешно добавлен.")
        finally:
            print("Обработка добавления товара завершена.")

    def get_products(self) -> list[Product]:
        """
        Внутренний метод для доступа к списку продуктов (для итератора)
        """
        return self.__products

    def middle_price(self) -> float:
        """
        Подсчет среднего ценника товаров
        """
        try:
            total = sum(p.price for p in self.__products)
            return total / len(self.__products)
        except ZeroDivisionError:
            return 0


class CategoryIterator:
    """
    Итератор для перебора продуктов в категории
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


class Smartphone(Product):
    """
    Дочерний класс от класса Product для смартфонов
    """

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self) -> str:
        base_info = super().__str__()
        return f"{base_info} | Модель: {self.model}, Память: {self.memory}, Цвет: {self.color}"


class LawnGrass(Product):
    """
    Дочерний класс от класса Product для газонной травы
    """

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self) -> str:
        base_info = super().__str__()
        return f"{base_info} | Период роста: {self.germination_period}, Страна: {self.country}"
