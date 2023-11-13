import logging
from typing import Any, Dict, Optional

import requests
from requests import Response as HTTPResponse

log = logging.getLogger(__name__)


class HTTPClient:
    def get(
        self,
        *,
        url_service: str,
        timeout: float = 45,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, Any]] = None,
        cookies: Optional[Dict[str, Any]] = None,
    ) -> HTTPResponse:
        if headers is None:
            headers = {}
        return requests.get(
            url_service,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
        )

    def post(
        self,
        *,
        url_service: str,
        timeout: float = 45,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        body: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, Any]] = None,
        cookies: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
    ) -> HTTPResponse:
        if headers is None:
            headers = {}
        return requests.post(
            url_service,
            params=params,
            json=body,
            data=data,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            files=files,
        )

    def put(
        self,
        *,
        url_service: str,
        timeout: float = 45,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        body: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, Any]] = None,
        cookies: Optional[Dict[str, Any]] = None,
    ) -> HTTPResponse:
        if headers is None:
            headers = {}
        return requests.put(
            url_service,
            params=params,
            json=body,
            data=data,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
        )

    def delete(
        self,
        *,
        url_service: str,
        timeout: float = 45,
        headers: Optional[Dict[str, Any]] = None,
        cookies: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> HTTPResponse:
        if headers is None:
            headers = {}
        return requests.delete(
            url_service,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            )

    def patch(
        self,
        *,
        url_service: str,
        timeout: float = 45,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        body: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, Any]] = None,
        cookies: Optional[Dict[str, Any]] = None,
    ) -> HTTPResponse:
        if headers is None:
            headers = {}
        return requests.patch(
            url_service,
            params=params,
            json=body,
            data=data,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
        )