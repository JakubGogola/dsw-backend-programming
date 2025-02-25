# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import StrictInt
from typing import Any, List
from openapi_server.models.order import Order
from openapi_server.models.order_create import OrderCreate
from openapi_server.models.user import User
from openapi_server.models.user_create import UserCreate


class BaseDefaultApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseDefaultApi.subclasses = BaseDefaultApi.subclasses + (cls,)
    async def create_order(
        self,
        order_create: OrderCreate,
    ) -> Order:
        ...


    async def create_user(
        self,
        user_create: UserCreate,
    ) -> User:
        ...


    async def delete_user(
        self,
        id: StrictInt,
    ) -> None:
        ...


    async def get_user(
        self,
        id: StrictInt,
    ) -> User:
        ...


    async def get_user_orders(
        self,
        id: StrictInt,
    ) -> List[Order]:
        ...


    async def get_users(
        self,
    ) -> List[User]:
        ...
