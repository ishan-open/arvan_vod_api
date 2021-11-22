from requests import Response
from typing import List

from .base_res import BaseResponse
from ..core import (
    ChannelDataCore, ChannelMetaCore,
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
