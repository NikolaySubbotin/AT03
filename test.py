import pytest
from unittest.mock import patch
from main import get_random_cat_image

def test_successful_request():
    mock_response = [{"id": "0XYvRd7oD", "url": "https://cdn2.thecatapi.com/images/0XYvRd7oD.jpg",
                      "width": 1204, "height": 1445}]

    with patch('main.requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        result = get_random_cat_image()
        assert result == "https://cdn2.thecatapi.com/images/0XYvRd7oD.jpg"

def test_unsuccessful_request():
    with patch('main.requests.get') as mock_get:
        mock_get.return_value.status_code = 404

        result = get_random_cat_image()
        assert result is None
