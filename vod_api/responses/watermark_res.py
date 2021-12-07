from requests import Response
from typing import List
from http import HTTPStatus

from .base_res import BaseResponse
from ..core import (
    WatermarkDataCore, MetaCore,
)
from ..errors import (
    InvalidParameterError, NotFoundError,
)


class GetWatermarksResponse(BaseResponse):
    def __init__(self, response: Response):
        super(GetWatermarksResponse, self).__init__(response)

    @property
    def data(self) -> List[WatermarkDataCore]:
        return [WatermarkDataCore(i) for i in self.as_dict["data"]]

    @property
    def links(self) -> dict:
        return self.as_dict["links"]
    
    @property
    def meta(self) -> MetaCore:
        return MetaCore(self.as_dict["meta"])


class GetWatermarkResponse(BaseResponse):
    def __init__(self, response: Response):
        super(GetWatermarkResponse, self).__init__(response)
        if self.status_code != HTTPStatus.OK:
            if self.status_code == HTTPStatus.NOT_FOUND:
                raise NotFoundError(self.as_dict["message"])

    @property
    def data(self) -> WatermarkDataCore:
        return WatermarkDataCore(self.as_dict["data"])


class PostWatermarkResponse(BaseResponse):
    def __init__(self, response: Response):
        super(PostWatermarkResponse, self).__init__(response)
        if self.status_code != HTTPStatus.CREATED:
            if self.status_code == HTTPStatus.NOT_FOUND:
                raise NotFoundError(self.as_dict["message"])
            elif self.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
                raise InvalidParameterError(self.as_dict["errors"])

    @property
    def data(self) -> WatermarkDataCore:
        return WatermarkDataCore(self.as_dict["data"])

    @property
    def message(self) -> str:
        return self.as_dict["message"]
