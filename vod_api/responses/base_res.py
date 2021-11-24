from requests import Response
from http import HTTPStatus

from ..errors import InvalidKeyError, ArvanInternalError


class BaseResponse:
    def __init__(self, response: Response):
        if response.status_code == HTTPStatus.UNAUTHORIZED:
            raise InvalidKeyError

        elif response.status_code not in (
                HTTPStatus.OK, HTTPStatus.CREATED,
                HTTPStatus.NOT_FOUND, HTTPStatus.NO_CONTENT,
                HTTPStatus.UNPROCESSABLE_ENTITY,
            ):
            raise ArvanInternalError

        self.response = response
        self.status_code = response.status_code
        self.content = response.content

    @property
    def as_dict(self):
        return self.response.json()
