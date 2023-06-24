import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
import json

client = APIClient()


@pytest.mark.django_db
def test_register_user():
    payload = dict(
        username='harry',
        password='harry',
        conform_password='harry',
        admin="true"
    )
    response = client.post("/api/register/", payload)
    data = response.data
    assert "password" not in data
    assert data["username"] == payload['username']
    assert response.status_code == 201


@pytest.mark.django_db
def test_login_user():
    payload = dict(
        username='harry',
        password='harry',
        conform_password='harry',
        admin="true"
    )

    client.post("/api/register/", payload)
    response = client.post("/api/login/", dict(username='harry', password='harry'))
    data = response.data
    assert response.status_code == 200


@pytest.mark.django_db
def test_logout_user(client):
    payload = dict(
        username='harry',
        password='harry',
        conform_password='harry',
        admin="true"
    )

    client.post("/api/register/", payload)
    response = client.post("/api/login/", dict(username='harry', password='harry'))
    token = response.data
    headers = {'Authorization': f'Token {token["token"]}'}
    head = json.dumps(headers)
    response = client.post("/api/logout/", HTTP_AUTHORIZATION=f'Token {token["token"]}')
    data = response.data

    assert token['token']
    assert data is None
    assert response.status_code == 204


@pytest.mark.django_db
def test_create_event(client):
    payload = dict(
        username='harry',
        password='harry',
        conform_password='harry',
        admin="true"
    )
    client.post("/api/register/", payload)
    response = client.post("/api/login/", dict(username='harry', password='harry'))
    token = response.data

    response = client.post("/api/admin/create/", {
        'event': 'Paradise',
        'start_date': '2023-06-07',
        'end_date': '2024-01-01',
        'seat': '10',
        'details': 'new world',
    },
                           HTTP_AUTHORIZATION=f'Token {token["token"]}')

    data = response.data

    assert response.status_code == 201

@pytest.mark.django_db
def test_list_event(client):
    payload = dict(
        username='harry',
        password='harry',
        conform_password='harry',
        admin="true"
    )
    client.post("/api/register/", payload)
    response = client.post("/api/login/", dict(username='harry', password='harry'))
    token = response.data

    response = client.post("/api/admin/list/", HTTP_AUTHORIZATION=f'Token {token["token"]}')

    data = response.data

    assert response.status_code == 200
