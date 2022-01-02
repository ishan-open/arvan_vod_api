from typing import List

from .base_res import GetItemsResponse, GetResponse, PostResponse
from ..core import VideoDataCore


class GetVideosResponse(GetItemsResponse):
    @property
    def data(self) -> List[VideoDataCore]:
        return [VideoDataCore(i) for i in self.as_dict["data"]]


class GetVideoResponse(GetResponse):
    @property
    def data(self) -> VideoDataCore:
        return VideoDataCore(self.as_dict["data"])


class PostVideoResponse(PostResponse):
    @property
    def data(self) -> VideoDataCore:
        return VideoDataCore(self.as_dict["data"])
