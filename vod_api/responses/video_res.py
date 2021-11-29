from http import HTTPStatus
from requests import Response
from typing import List

from .base_res import BaseResponse
from ..errors import (
    NotFoundError, InvalidParameterError,
)
from ..core import (
    VideoDataCore, MetaCore,
)


class GetVideosResponse(BaseResponse):
    def __init__(self, response: Response):
        super(GetVideosResponse, self).__init__(response)
        if self.status_code != HTTPStatus.OK:
            if self.status_code == HTTPStatus.NOT_FOUND:
                raise NotFoundError(self.as_dict["message"])

    @property
    def data(self) -> List[VideoDataCore]:
        return [VideoDataCore(i) for i in self.as_dict["data"]]

    @property
    def links(self) -> dict:
        return self.as_dict["links"]

    @property
    def meta(self) -> MetaCore:
        return MetaCore(self.as_dict["meta"])


class GetVideoResponse(BaseResponse):
    def __init__(self, response: Response):
        super(GetVideoResponse, self).__init__(response)
        if self.status_code != HTTPStatus.OK:
            if self.status_code == HTTPStatus.NOT_FOUND:
                raise NotFoundError(self.as_dict["message"])

    @property
    def data(self) -> VideoDataCore:
        return VideoDataCore(self.as_dict["data"])


class PostVideoResponse(BaseResponse):
    def __init__(self, response: Response):
        super(PostVideoResponse, self).__init__(response)
        if self.status_code != HTTPStatus.CREATED:
            if self.status_code == HTTPStatus.NOT_FOUND:
                raise NotFoundError(self.as_dict["message"])
            elif self.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
                raise InvalidParameterError(self.as_dict["errors"])

    @property
    def data(self) -> VideoDataCore:
        return VideoDataCore(self.as_dict["data"])

    @property
    def message(self) -> str:
        return self.as_dict["message"]


class DeleteVideoResponse(BaseResponse):
    def __init__(self, response: Response):
        super(DeleteVideoResponse, self).__init__(response)
        if self.status_code == HTTPStatus.NOT_FOUND:
            raise NotFoundError(self.message)

    @property
    def message(self) -> str:
        return self.as_dict["message"]
