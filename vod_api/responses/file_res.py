from http import HTTPStatus
from requests import Response

from .base_res import BaseResponse
from ..errors import InvalidParameterError, NotFoundError


class GetFilesResponse(BaseResponse):
    def __init__(self, response: Response):
        super(GetFilesResponse, self).__init__(response)
        
    def data(self):
        return self.as_dict["data"]

    def links(self):
        return self.as_dict["links"]

    def meta(self):
        return self.as_dict["meta"]


class PostFileResponse(BaseResponse):
    def __init__(self, response: Response):
        super(PostFileResponse, self).__init__(response)
        if self.status_code != HTTPStatus.OK:
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
