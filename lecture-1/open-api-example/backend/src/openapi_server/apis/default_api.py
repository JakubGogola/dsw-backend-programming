# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.default_api_base import BaseDefaultApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from pydantic import StrictInt
from typing import Any, List
from openapi_server.models.order import Order
from openapi_server.models.order_create import OrderCreate
from openapi_server.models.user import User
from openapi_server.models.user_create import UserCreate


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/orders",
    responses={
        201: {"model": Order, "description": "Zamówienie zostało utworzone"},
    },
    tags=["default"],
    summary="Tworzy nowe zamówienie",
    response_model_by_alias=True,
)
async def create_order(
    order_create: OrderCreate = Body(None, description=""),
) -> Order:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().create_order(order_create)


@router.post(
    "/users",
    responses={
        201: {"model": User, "description": "Użytkownik został utworzony"},
    },
    tags=["default"],
    summary="Tworzy nowego użytkownika",
    response_model_by_alias=True,
)
async def create_user(
    user_create: UserCreate = Body(None, description=""),
) -> User:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().create_user(user_create)


@router.delete(
    "/users/{id}",
    responses={
        204: {"description": "Użytkownik został usunięty"},
    },
    tags=["default"],
    summary="Usuwa użytkownika",
    response_model_by_alias=True,
)
async def delete_user(
    id: StrictInt = Path(..., description=""),
) -> None:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().delete_user(id)


@router.get(
    "/users/{id}",
    responses={
        200: {"model": User, "description": "Szczegóły użytkownika"},
        404: {"description": "Użytkownik nie znaleziony"},
    },
    tags=["default"],
    summary="Pobiera szczegóły użytkownika",
    response_model_by_alias=True,
)
async def get_user(
    id: StrictInt = Path(..., description=""),
) -> User:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().get_user(id)


@router.get(
    "/users/{id}/orders",
    responses={
        200: {"model": List[Order], "description": "Lista zamówień użytkownika"},
    },
    tags=["default"],
    summary="Pobiera zamówienia użytkownika",
    response_model_by_alias=True,
)
async def get_user_orders(
    id: StrictInt = Path(..., description=""),
) -> List[Order]:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().get_user_orders(id)


@router.get(
    "/users",
    responses={
        200: {"model": List[User], "description": "Lista użytkowników"},
    },
    tags=["default"],
    summary="Pobiera listę użytkowników",
    response_model_by_alias=True,
)
async def get_users(
) -> List[User]:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().get_users()
