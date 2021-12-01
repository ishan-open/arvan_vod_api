from requests import Response
from typing import List
from http import HTTPStatus

from .base_res import BaseResponse
from ..core import (
    AudioTrackDataCore, MetaCore,
)
from ..errors import (
    InvalidParameterError, NotFoundError,
)


class GetAudioTracksResponse(BaseResponse):
    def __init__(self, response: Response):
        super(GetAudioTracksResponse, self).__init__(response)

    @property
    def data(self) -> List[AudioTrackDataCore]:
        return [AudioTrackDataCore(i) for i in self.as_dict["data"]]

    @property
    def links(self) -> dict:
        return self.as_dict["links"]
    
    @property
    def meta(self) -> MetaCore:
        return MetaCore(self.as_dict["meta"])


class GetAudioTrackResponse(BaseResponse):
    def __init__(self, response: Response):
        super(GetAudioTrackResponse, self).__init__(response)
        if self.status_code != HTTPStatus.OK:
            if self.status_code == HTTPStatus.NOT_FOUND:
                raise NotFoundError(self.as_dict["message"])

    @property
    def data(self) -> AudioTrackDataCore:
        return AudioTrackDataCore(self.as_dict["data"])


class PostAudioTrackResponse(BaseResponse):
    def __init__(self, response: Response):
        super(PostAudioTrackResponse, self).__init__(response)
        if self.status_code != HTTPStatus.CREATED:
            if self.status_code == HTTPStatus.NOT_FOUND:
                raise NotFoundError(self.as_dict["message"])
            elif self.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
                raise InvalidParameterError(self.as_dict["errors"])

    @property
    def data(self) -> AudioTrackDataCore:
        return AudioTrackDataCore(self.as_dict["data"])

    @property
    def message(self) -> str:
        return self.as_dict["message"]


class DeleteAudioTrackResponse(BaseResponse):
    def __init__(self, response: Response):
        super(DeleteAudioTrackResponse, self).__init__(response)
        if self.status_code == HTTPStatus.NOT_FOUND:
            raise NotFoundError(self.message)

    @property
    def message(self) -> str:
        return self.as_dict["message"]
