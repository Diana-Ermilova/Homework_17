import requests
import pytest
from jsonschema import validate
from test_schema import *

base_url = "https://reqres.in"
endpoint_list_users = "/api/users?page=2"
endpoint_single_user = "/api/users/2"
endpoint_not_found_user = "/api/users/23"
unknown_res = "/api/unknown/23"
headers = { "x-api-key": "reqres-free-v1" } #без хедера не работает

def test_get_list_of_users():
    response = requests.get(base_url + endpoint_list_users)
    assert response.status_code == 200

def test_get_single_user():
    response = requests.get(base_url + endpoint_single_user)
    assert response.status_code == 200
    body = response.json()
    validate(body, get_single_user)

def test_single_resource_404():
    response = requests.get(base_url + unknown_res, headers=headers)
    assert response.status_code == 404
    body = response.json()
    validate(body, single_resource_404)

def test_user_hasnot_been_found():
    response = requests.get(base_url + endpoint_not_found_user)
    assert response.status_code == 401

