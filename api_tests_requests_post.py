from functools import reduce
from http.client import responses
import requests
import pytest
from jsonschema import validate
from test_schema import post_create_user, post_reg_user, post_reg_user_400

base_url = "https://reqres.in"
endpoint_create = "/api/users"
endpoint_register = "/api/register"

body_create = {"name": "morpheus", "job": "leader"}
body_register = {"email": "eve.holt@reqres.in", "password": "pistol"}
wrong_body = {"email": "tom_doct@test.com", "password": "tom123456"}
headers = { "x-api-key": "reqres-free-v1" } #а без хедера 401

def test_post_create_user():
    response = requests.post(base_url + endpoint_create, data=body_create, headers=headers)
    assert response.status_code == 201
    assert response.json()["name"] == "morpheus"
    assert response.json()["job"] == "leader"
    response_body = response.json()
    validate(response_body, post_create_user)

def test_post_reg_user():
    response = requests.post(base_url + endpoint_register, data=body_register, headers=headers)
    assert response.status_code == 200
    response_body = response.json()
    validate(response_body, post_reg_user)

def test_post_reg_user_400():
    response = requests.post(base_url + endpoint_register, data=wrong_body, headers=headers)
    assert response.status_code == 400
    response_body = response.json()
    validate(response_body, post_reg_user_400)




