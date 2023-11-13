from typing import Any, Generic, Optional, Union

from pydantic import BaseModel

from app.infrastructure.http.client import HTTPClient
from app.infrastructure.http.responses import Responses
from app.schemas.general import CreateSchemaType, OrderData, UpdateSchemaType


class BaseService(Generic[CreateSchemaType, UpdateSchemaType]):
    def __init__(
        self,
        url: Optional[str] = None,
        check_codes: Responses = Responses(),
        client: HTTPClient = HTTPClient(),
    ):
        self.url = url
        self._client = client
        self._check_codes = check_codes

    def create(
        self,
        *,
        obj_in: Optional[Union[CreateSchemaType, dict[str, Any]]] = None,
        route: Optional[str] = "",
        params: Optional[dict[str, Any]] = None,
        url: Optional[str] = None,
        headers: Optional[dict[str, Any]] = None,
    ) -> dict[str, Any]:
        url = f"{url or self.url}{route}"
        body = obj_in.model_dump() if isinstance(obj_in, BaseModel) else obj_in
        response = self._client.post(
            url_service=url, body=body, params=params, headers=headers
        )
        response.raise_for_status()
        return response.json()

    def update(
        self,
        *,
        id: Union[int, str],
        obj_in: Union[UpdateSchemaType, dict[str, Any]],
        route: Optional[str] = "",
        url: Optional[str] = None,
        headers: Optional[dict[str, Any]] = None,
    ) -> bool:
        url = f"{url or self.url}{route}/{id}"
        body = (
            obj_in.model_dump(exclude_unset=True)
            if isinstance(obj_in, BaseModel)
            else obj_in
        )
        response = self._client.patch(url_service=url, body=body, headers=headers)
        response.raise_for_status()
        return True

    def update_with_put(
        self,
        *,
        id: Union[int, str],
        obj_in: Union[UpdateSchemaType, dict[str, Any]],
        route: Optional[str] = "",
        url: Optional[str] = None,
        headers: Optional[dict[str, Any]] = None,
    ) -> bool:
        url = f"{url or self.url}{route}/{id}/"
        body = (
            obj_in.model_dump(exclude_unset=True)
            if isinstance(obj_in, BaseModel)
            else obj_in
        )
        response = self._client.put(url_service=url, body=body, headers=headers)
        response.raise_for_status()
        return True

    def delete(
        self,
        *,
        id: Union[int, str],
        route: Optional[str] = "",
        url: Optional[str] = None,
        headers: Optional[dict[str, Any]] = None,
    ) -> bool:
        url = f"{url or self.url}{route}/{id}"
        response = self._client.delete(url_service=url, headers=headers)
        response.raise_for_status()
        return True

    def get_byid(
        self,
        *,
        id: Union[int, str],
        route: Optional[str] = "",
        url: Optional[str] = None,
        headers: Optional[dict[str, Any]] = None,
    ) -> dict[str, Any]:
        url = f"{url or self.url}{route}/{id}"
        response = self._client.get(url_service=url, headers=headers, timeout=180)
        response.raise_for_status()
        return response.json()

    def get_all(
        self,
        payload: Optional[dict[str, Any]],
        skip: int,
        limit: int,
        q: Optional[str] = None,
        route: Optional[str] = "",
        order_by: Optional[OrderData] = None,
        url: Optional[str] = None,
    ) -> list[Any]:
        if payload:
            payload.update({"skip": skip, "limit": limit})
        else:
            payload = {"skip": skip, "limit": limit}
        if q:
            payload.update({"q": q})
        if order_by is not None:
            payload.update({"order_by": order_by.value})
        url = f"{self.url}{route}"
        response = self._client.get(url_service=url, params=payload, timeout=200)
        response.raise_for_status()
        return response.json()

    def count(
        self,
        payload: Optional[dict[str, Any]] = None,
        route: Optional[str] = "",
        url: Optional[str] = None,
    ) -> int:
        url = f"{url or self.url}{route}"
        response = self._client.get(url_service=url, params=payload)
        response.raise_for_status()
        return response.json()
