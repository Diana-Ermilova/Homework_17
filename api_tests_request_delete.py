from http.client import responses

import requests

base_url = "https://reqres.in"
endpoint_user = "/api/users/2"
headers = { "x-api-key": "reqres-free-v1" } #а без хедера 401


def test_delete_user():
    response_delete = requests.delete(base_url + endpoint_user, headers=headers)
    assert response_delete.status_code == 204
    response_get = requests.get(base_url + endpoint_user, headers=headers)
    assert response_get.status_code == 200