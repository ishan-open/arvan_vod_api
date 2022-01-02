from typing import List

from .base_res import GetItemsResponse, GetResponse, PostResponse
from ..core import (
    ChannelDataCore,
)


class GetChannelsReponse(GetItemsResponse):
    @property
    def data(self) -> List[ChannelDataCore]:
        return [ChannelDataCore(c) for c in self.as_dict["data"]]


class GetChannelReponse(GetResponse):
    @property
    def data(self) -> ChannelDataCore:
        return ChannelDataCore(self.as_dict["data"])


class PostChannelResponse(PostResponse):
    @property
    def data(self) -> ChannelDataCore:
        return ChannelDataCore(self.as_dict["data"])
