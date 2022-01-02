from typing import List

from .base_res import GetItemsResponse, GetResponse, PostResponse
from ..core import AudioDataCore


class GetAudiosResponse(GetItemsResponse):
    @property
    def data(self) -> List[AudioDataCore]:
        return [AudioDataCore(i) for i in self.as_dict["data"]]


class GetAudioResponse(GetResponse):
    @property
    def data(self) -> AudioDataCore:
        return AudioDataCore(self.as_dict["data"])


class PostAudioResponse(PostResponse):
    @property
    def data(self) -> AudioDataCore:
        return AudioDataCore(self.as_dict["data"])
