from requests import Response
from typing import List
from http import HTTPStatus

from .base_res import BaseResponse
from ..core import (
    ChannelDataCore, ChannelMetaCore,
    ChannelPostDataCore,
)
from ..errors import (
    InvalidParameterError,
)


class GetChannelsReponse(BaseResponse):
    def __init__(self, response: Response):
        super(GetChannelsReponse, self).__init__(response)

    @property
    def data(self) -> List[ChannelDataCore]:
        return [ChannelDataCore(c) for c in self.as_dict["data"]]

    @property
    def links(self) -> dict:
        return self.as_dict["links"]

    @property
    def meta(self) -> ChannelMetaCore:
        return ChannelMetaCore(self.as_dict["meta"])


class PostChannelResponse(BaseResponse):
    def __init__(self, response: Response):
        super(PostChannelResponse, self).__init__(response)
        if self.status_code != HTTPStatus.OK:
            if self.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
                raise InvalidParameterError(self.as_dict["errors"])

    @property
    def data(self) -> ChannelPostDataCore:
        return ChannelPostDataCore(self.as_dict["data"])

    @property
    def message(self) -> str:
        return self.as_dict["message"]
