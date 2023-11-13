import json
import logging
from datetime import datetime

from requests import Response as HTTPResponse
from requests.exceptions import JSONDecodeError

from app.core.exceptions import HTTPException

logger = logging.getLogger(__name__)


class Responses:
    def __init__(self):
        self.code_switcher = {
            400: self.__400,
            401: self.__401,
            403: self.__403,
            404: self.__404,
            422: self.__422,
            500: self.__500,
        }

    def __400(self):
        return f"{datetime.now()}: Bad request"

    def __401(self):
        return f"{datetime.now()}: Unauthorized"

    def __403(self):
        return f"{datetime.now()}: Forbidden"

    def __404(self):
        return f"{datetime.now()}: Not Found"

    def __422(self):
        return f"{datetime.now()}: Unprocessable Entity"

    def __500(self):
        return f"{datetime.now()}: Internal Server Error"

    def check_codes(self, *, response: HTTPResponse, delete_method=False):
        if response is None:
            raise HTTPException(status_code=500, detail="Could not get response")
        code = self.code_switcher.get(response.status_code, lambda: None)
        content = code()
        if content:
            try:
                logger.error(
                    f"{datetime.now()} - {response.reason if delete_method else response.json().get('detail', None)}"
                )
                response_content = response.content
                detail = (
                    json.loads(response_content).get("detail")
                    or response_content.decode()
                )
            except JSONDecodeError as je:
                detail = f"Expecting property json. This is what was received: {response.content.decode()}"
                print(je)
            except Exception as e:
                detail = str(e)
                print(e)
            raise HTTPException(
                status_code=response.status_code,
                detail=f"Error: {detail}, method: {response.request.method} in service: {response.url}",
            )
