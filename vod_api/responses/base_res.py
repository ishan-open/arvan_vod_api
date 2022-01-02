from requests import Response
from http import HTTPStatus
from abc import ABC, abstractmethod

from ..core import MetaCore
from ..errors import (
    InvalidKeyError, ArvanInternalError,
    NotFoundError, InvalidParameterError,
)


class BaseResponse(ABC):
    def __init__(self, response: Response):
        if response.status_code == HTTPStatus.UNAUTHORIZED:
            raise InvalidKeyError

        elif response.status_code not in (
                HTTPStatus.OK,
                HTTPStatus.CREATED,
                HTTPStatus.NOT_FOUND,
                HTTPStatus.NO_CONTENT,
                HTTPStatus.UNPROCESSABLE_ENTITY,
                HTTPStatus.REQUESTED_RANGE_NOT_SATISFIABLE,
            ):
            raise ArvanInternalError

        self.response = response
        self.status_code = response.status_code
        self.content = response.content

    @abstractmethod
    def data(self):
        raise NotImplementedError

    @property
    def as_dict(self):
        return self.response.json()


class GetItemsResponse(BaseResponse):
    def __init__(self, response: Response):
        super(GetItemsResponse, self).__init__(response)

    @property
    def links(self) -> dict:
        return self.as_dict["links"]

    @property
    def meta(self) -> MetaCore:
        return MetaCore(self.as_dict["meta"])


class GetResponse(BaseResponse):
    def __init__(self, response: Response):
        super(GetResponse, self).__init__(response)
        if self.status_code == HTTPStatus.NOT_FOUND:
            raise NotFoundError(self.as_dict["message"])


class PostResponse(BaseResponse):
    def __init__(self, response: Response):
        super(PostResponse, self).__init__(response)
        if self.status_code not in (HTTPStatus.OK, HTTPStatus.CREATED):
            if self.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
                raise InvalidParameterError(self.as_dict["errors"])

            elif self.status_code == HTTPStatus.NOT_FOUND:
                raise NotFoundError(self.message)

    @property
    def message(self) -> str:
        return self.as_dict["message"]


class DeleteResponse(BaseResponse):
    def __init__(self, response: Response):
        super(DeleteResponse, self).__init__(response)
        if self.status_code == HTTPStatus.NOT_FOUND:
            raise NotFoundError(self.message)

    @property
    def data(self):
        return self.as_dict.get("data")

    @property
    def message(self) -> str:
        return self.as_dict["message"]
