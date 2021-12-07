from http import HTTPStatus
from requests import Response
from typing import List

from .base_res import BaseResponse
from ..errors import (
    InvalidParameterError, NotFoundError,
    InvalidOffsetError,
)
from ..core import (
    FileCore, MetaCore
)


class GetFilesResponse(BaseResponse):
    def __init__(self, response: Response):
        super(GetFilesResponse, self).__init__(response)

    @property
    def data(self) -> List[FileCore]:
        return [FileCore(file) for file in self.as_dict["data"]]

    @property
    def links(self) -> dict:
        return self.as_dict["links"]

    @property
    def meta(self) -> MetaCore:
        return self.as_dict["meta"]


class GetFileResponse(BaseResponse):
    def __init__(self, response: Response):
        super(GetFileResponse, self).__init__(response)
        if self.status_code != HTTPStatus.OK:
            if self.status_code == HTTPStatus.NOT_FOUND:
                raise NotFoundError("Invalid file id")

    @property
    def data(self) -> FileCore:
        return FileCore(self.as_dict["data"])


class PostFileResponse(BaseResponse):
    def __init__(self, response: Response):
        super(PostFileResponse, self).__init__(response)
        if self.status_code != HTTPStatus.CREATED:
            if self.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
                raise InvalidParameterError(self.as_dict["errors"])
        
        self.created_file_location = self.response.headers["location"]
        self.created_file_id = self.file_location.rsplit("/")[-1]

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
