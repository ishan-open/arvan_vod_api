from typing import List

from .base_res import GetItemsResponse, GetResponse, PostResponse
from ..core import (
    ProfileDataCore,
)


class GetProfilesResponse(GetItemsResponse):
    @property
    def data(self) -> List[ProfileDataCore]:
        return [ProfileDataCore(i) for i in self.as_dict["data"]]


class GetProfileResponse(GetResponse):
    @property
    def data(self) -> ProfileDataCore:
        return ProfileDataCore(self.as_dict["data"])


class PostProfileResponse(PostResponse):
    @property
    def data(self) -> ProfileDataCore:
        return ProfileDataCore(self.as_dict["data"])
