from requests import Response
from typing import List
from http import HTTPStatus

from .base_res import BaseResponse
from ..core import (
    SubtitleDataCore, MetaCore,
)
from ..errors import (
    InvalidParameterError, NotFoundError,
)


class GetSubtitlesResponse(BaseResponse):
    def __init__(self, response: Response):
        super(GetSubtitlesResponse, self).__init__(response)

    @property
    def data(self) -> List[SubtitleDataCore]:
        return [SubtitleDataCore(i) for i in self.as_dict["data"]]

    @property
    def links(self) -> dict:
        return self.as_dict["links"]
    
    @property
    def meta(self) -> MetaCore:
        return MetaCore(self.as_dict["meta"])


class GetSubtitleResponse(BaseResponse):
    def __init__(self, response: Response):
        super(GetSubtitleResponse, self).__init__(response)
        if self.status_code != HTTPStatus.OK:
            if self.status_code == HTTPStatus.NOT_FOUND:
                raise NotFoundError(self.as_dict["message"])

    @property
    def data(self) -> SubtitleDataCore:
        return SubtitleDataCore(self.as_dict["data"])


class PostSubtitleResponse(BaseResponse):
    def __init__(self, response: Response):
        super(PostSubtitleResponse, self).__init__(response)
        if self.status_code != HTTPStatus.CREATED:
            if self.status_code == HTTPStatus.NOT_FOUND:
                raise NotFoundError(self.as_dict["message"])
            elif self.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
                raise InvalidParameterError(self.as_dict["errors"])

    @property
    def data(self) -> SubtitleDataCore:
        return SubtitleDataCore(self.as_dict["data"])

    @property
    def message(self) -> str:
        return self.as_dict["message"]


class DeleteSubtitleResponse(BaseResponse):
    def __init__(self, response: Response):
        super(DeleteSubtitleResponse, self).__init__(response)
        if self.status_code == HTTPStatus.NOT_FOUND:
            raise NotFoundError(self.message)

    @property
    def message(self) -> str:
        return self.as_dict["message"]
