# === Каталог товаров ===

Приложение для управления категориями и товарами с возможностью загрузки данных из JSON-файла

---
## Возможности

- Создание категорий товаров
- Управление товарами внутри категорий
- Автоматический подсчет количества категорий и товаров
- Загрузка данных из JSON-файла
---


## Классы

### `Product`

Класс для представления товара:

```python
class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
```

### `Category`
Класс для представления категории товаров:

```python
class Category:
    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
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
for category in categories:
    print(category)
    for product in category.products:
        print(f"  {product}")

print(f"\nВсего категорий: {Category.category_count}")
print(f"Всего товаров: {Product.product_count}")
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

