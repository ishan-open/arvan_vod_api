from http import HTTPStatus
from requests import Response
from typing import List

from .base_res import (
    BaseResponse, GetItemsResponse,
    GetResponse, PostResponse,
)
from ..errors import NotFoundError, InvalidOffsetError
from ..core import FileCore


class GetFilesResponse(GetItemsResponse):
    @property
    def data(self) -> List[FileCore]:
        return [FileCore(file) for file in self.as_dict["data"]]


class GetFileResponse(GetResponse):
    @property
    def data(self) -> FileCore:
        return FileCore(self.as_dict["data"])


class PostFileResponse(PostResponse):
    def __init__(self, response: Response):
        super(PostFileResponse, self).__init__(response)
        self.created_file_location = self.response.headers["location"]
        self.created_file_id = self.file_location.rsplit("/")[-1]

    @property
    def data(self):
        return self.as_dict.get("data")

    @property
    def file_id(self) -> str:
        return self.created_file_id

    @property
    def file_location(self) -> str:
        return self.created_file_location


class HeadFileResponse(BaseResponse):
    def __init__(self, response: Response):
        super(HeadFileResponse, self).__init__(response)
        if self.status_code != HTTPStatus.OK:
            if self.status_code == HTTPStatus.NOT_FOUND:
                raise NotFoundError("ChannelId or FileId is Invalid!")

    @property
    def upload_length(self) -> str:
        return self.response.headers["Upload-Length"]

    @property
    def upload_offset(self) -> str:
        return self.response.headers["Upload-Offset"]


class PatchFileResponse(BaseResponse):
    def __init__(self, response: Response):
        super(PatchFileResponse, self).__init__(response)
        if self.status_code != HTTPStatus.NO_CONTENT:
            if self.status_code == HTTPStatus.REQUESTED_RANGE_NOT_SATISFIABLE:
                raise InvalidOffsetError
            elif self.status_code == HTTPStatus.NOT_FOUND:
                raise NotFoundError("FileId is invalid!")

    @property
    def upload_offset(self) -> str:
        return self.response.headers["Upload-Offset"]
