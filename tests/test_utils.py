from unittest.mock import mock_open, patch

from src.utils import create_objects, read_json


def test_open_json_correct():
    with patch("builtins.open", mock_open(read_data='["1"]')):
        assert read_json("") == ["1"]
    with patch("builtins.open", mock_open(read_data='{"1" . "2"')):
        assert read_json("") == []
    assert read_json("") == []


def test_create_objects_empty():
    assert create_objects([]) == []


def test_create_objects_not_empty():
    input_data = [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, но и получение"
            "дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                }
            ],
        }
    ]
    result = create_objects(input_data)
    assert result[0].name == "Смартфоны"
