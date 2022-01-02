from typing import List

from .base_res import GetItemsResponse, GetResponse, PostResponse
from ..core import WatermarkDataCore


class GetWatermarksResponse(GetItemsResponse):
    @property
    def data(self) -> List[WatermarkDataCore]:
        return [WatermarkDataCore(i) for i in self.as_dict["data"]]


class GetWatermarkResponse(GetResponse):
    @property
    def data(self) -> WatermarkDataCore:
        return WatermarkDataCore(self.as_dict["data"])


class PostWatermarkResponse(PostResponse):
    @property
    def data(self) -> WatermarkDataCore:
        return WatermarkDataCore(self.as_dict["data"])
