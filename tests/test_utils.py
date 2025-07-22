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
