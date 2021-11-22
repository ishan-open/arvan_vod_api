from requests import Response
from http import HTTPStatus

from ..errors import InvalidKeyError


class BaseResponse:
    def __init__(self, response: Response):
        if response.status_code == HTTPStatus.UNAUTHORIZED:
            raise InvalidKeyError

        self.response = response
        self.status_code = response.status_code
        self.content = response.content

    @property
    def as_dict(self):
        return self.response.json()
