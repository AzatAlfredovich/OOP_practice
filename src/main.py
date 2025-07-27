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
    def new_product(cls, product_data: dict, existing_products: list):
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

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str

    def add_product(self, product: Product) -> None:
        """
        Добавляет продукт и увеличивает счетчик
        """
        if not isinstance(product, Product):  # ДОБАВЛЕНО: проверка на тип
            raise TypeError("Можно добавить только объект класса Product или его наследника")

        self.__products.append(product)
        Category.product_count += 1
