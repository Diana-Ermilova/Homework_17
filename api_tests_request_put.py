from test_schema import update_user
from http.client import responses
import requests
from jsonschema.validators import validate

base_url = "https://reqres.in"
endpoint_update = "/api/users/2"

body_update = {"name": "Tom","job": "zion resident"}
headers = { "x-api-key": "reqres-free-v1" } #уже знаем, что без хедера не работает

def test_update_user():
    response = requests.put(base_url + endpoint_update, data=body_update, headers=headers)
    assert response.status_code == 200
    assert response.status_code == 200
    assert response.json()["job"] == "zion resident"
    assert response.json()["name"] == "Tom"
    response_body = response.json()
    validate(response_body, update_user)