from typing import List

from .base_res import GetItemsResponse, GetResponse, PostResponse
from ..core import SubtitleDataCore


class GetSubtitlesResponse(GetItemsResponse):
    @property
    def data(self) -> List[SubtitleDataCore]:
        return [SubtitleDataCore(i) for i in self.as_dict["data"]]


class GetSubtitleResponse(GetResponse):
    @property
    def data(self) -> SubtitleDataCore:
        return SubtitleDataCore(self.as_dict["data"])


class PostSubtitleResponse(PostResponse):
    @property
    def data(self) -> SubtitleDataCore:
        return SubtitleDataCore(self.as_dict["data"])
