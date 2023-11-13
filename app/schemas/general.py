from enum import Enum
from typing import Any, TypeVar

from pydantic import BaseModel

ModelType = TypeVar("ModelType", bound=Any)

CrudType = TypeVar("CrudType", bound=Any)

CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
SendSchemaType = TypeVar("SendSchemaType", bound=BaseModel)


class CountDB(BaseModel):
    count: int


class OrderData(str, Enum):
    created_at_desc = "-created_at"
    created_at_asc = "created_at"
    last_modified_desc = "-last_modified"
    last_modified_asc = "last_modified"