# === Каталог товаров ===

Приложение для управления категориями и товарами с возможностью загрузки данных из JSON-файла

---
## Возможности

- Создание категорий товаров
- Управление товарами внутри категорий
- Автоматический подсчет количества категорий и товаров
- Перебор продуктов в рамках категории
- Загрузка данных из JSON-файла
---


## Классы

### `Product`

Класс для представления товара:

```python
class Product:
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
```

### `Category`
Класс для представления категории товаров:

```python
class Category:
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
```

### `CategoryIterator`
Класс для перебора продуктов в рамках категории:

```python
class CategoryIterator:
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
```
---

## Функции

1. Загружает данные из JSON-файла и подготавливает список для обработки объектов категорий и товаров
```python
def read_json(path: str) -> list:
    pass
```

2. Обрабатывает объекты категорий и товаров
```python
def create_objects(data: list) -> list:
    pass
```

### Параметры:
```python
full_path = os.path.abspath(path)  # путь к JSON-файлу
```

### Формат JSON-файла:

```json
[
    {
        "name": "Название категории",
        "description": "Описание категории",
        "products": [
            {
                "name": "Товар 1",
                "description": "Описание товара",
                "price": "100.0",
                "quantity": "5"
            }
        ]
    }
]
```
---

### Загрузка данных из файла
```python
data = read_json('путь до файла')
```
---

### Вывод информации
```python
def __str__(self):
"""Строковое отображение объекта Product"""
    return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

def __str__(self):
"""Строковое представление объекта Category"""
    total_quantity = sum(product.quantity for product in self.__products)
    return f"{self.name}, количество продуктов: {total_quantity} шт."
```
---

## Установка
Git-репозиторий автора: [Azat Khaliullin](https://github.com/AzatAlfredovich)

Скачивание JSON-файла с данными: [Google Drive](https://drive.google.com/file/d/1fTgJX1_-rI2JbuM2He6OPyU_N5PyePsd/view)

---

## Тестирование

Команда для запуска тестов
```

pytest --cov
```
---

