import requests
import pytest

BASE_URL = "https://postman-echo.com"


def test_get_with_query_params():
    """Тест GET запроса с query параметрами"""
    params = {"name": "John", "age": 30}
    response = requests.get(f"{BASE_URL}/get", params=params)

    assert response.status_code == 200
    assert response.json()["args"] == params


def test_post_with_json_body():
    """Тест POST запроса с JSON телом"""
    payload = {"message": "Hello, World!", "id": 123}
    response = requests.post(f"{BASE_URL}/post", json=payload)

    assert response.status_code == 200
    assert response.json()["json"] == payload


def test_post_with_form_data():
    """Тест POST запроса с form data"""
    form_data = {"username": "testuser", "password": "secret"}
    response = requests.post(f"{BASE_URL}/post", data=form_data)

    assert response.status_code == 200
    assert response.json()["form"] == form_data


def test_put_request():
    """Тест PUT запроса"""
    payload = {"updated": "data"}
    response = requests.put(f"{BASE_URL}/put", json=payload)

    assert response.status_code == 200
    assert response.json()["json"] == payload


def test_response_headers():
    """Тест проверки заголовков ответа"""
    response = requests.get(f"{BASE_URL}/get")

    assert response.status_code == 200
    assert "content-type" in response.headers
    assert "application/json" in response.headers["content-type"]


def test_delete_request():
    """Тест DELETE запроса"""
    response = requests.delete(f"{BASE_URL}/delete")

    assert response.status_code == 200




