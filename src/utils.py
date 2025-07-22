import json
import os.path

from src.main import Category, Product


def read_json(path: str) -> list:
    """Функция, которая преобразует JSON-объект в Python-объект"""
    full_path = os.path.abspath(path)
    try:
        with open(full_path, "r", encoding="utf-8") as file:
            data = list(json.load(file))
            return data
    except json.JSONDecodeError:
        return []
    except Exception as e:
        return []


def create_objects(data: list) -> list:
    categories = []
    for category_data in data:
        products = []
        for product_data in category_data["products"]:
            products.append(Product(**product_data))
        categories.append(Category(**category_data))
    return categories
