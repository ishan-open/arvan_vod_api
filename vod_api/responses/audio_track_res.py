from typing import List

from .base_res import GetItemsResponse, GetResponse, PostResponse
from ..core import AudioTrackDataCore


class GetAudioTracksResponse(GetItemsResponse):
    @property
    def data(self) -> List[AudioTrackDataCore]:
        return [AudioTrackDataCore(i) for i in self.as_dict["data"]]


class GetAudioTrackResponse(GetResponse):
    @property
    def data(self) -> AudioTrackDataCore:
        return AudioTrackDataCore(self.as_dict["data"])


class PostAudioTrackResponse(PostResponse):
    @property
    def data(self) -> AudioTrackDataCore:
        return AudioTrackDataCore(self.as_dict["data"])
