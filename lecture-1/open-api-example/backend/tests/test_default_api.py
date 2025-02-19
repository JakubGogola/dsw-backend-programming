# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import StrictInt  # noqa: F401
from typing import Any, List  # noqa: F401
from openapi_server.models.order import Order  # noqa: F401
from openapi_server.models.order_create import OrderCreate  # noqa: F401
from openapi_server.models.user import User  # noqa: F401
from openapi_server.models.user_create import UserCreate  # noqa: F401


def test_create_order(client: TestClient):
    """Test case for create_order

    Tworzy nowe zamówienie
    """
    order_create = {"total":6.0274563,"user_id":0}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/orders",
    #    headers=headers,
    #    json=order_create,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_create_user(client: TestClient):
    """Test case for create_user

    Tworzy nowego użytkownika
    """
    user_create = {"name":"name","email":"email"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/users",
    #    headers=headers,
    #    json=user_create,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_delete_user(client: TestClient):
    """Test case for delete_user

    Usuwa użytkownika
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/users/{id}".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_user(client: TestClient):
    """Test case for get_user

    Pobiera szczegóły użytkownika
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/users/{id}".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_user_orders(client: TestClient):
    """Test case for get_user_orders

    Pobiera zamówienia użytkownika
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/users/{id}/orders".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_users(client: TestClient):
    """Test case for get_users

    Pobiera listę użytkowników
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/users",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

