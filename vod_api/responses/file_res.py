from http import HTTPStatus
from requests import Response

from .base_res import BaseResponse


class GetFilesResponse(BaseResponse):
    def __init__(self, response: Response):
        super(GetFilesResponse, self).__init__(response)
        
    def data(self):
        return self.as_dict["data"]

    def links(self):
        return self.as_dict["links"]

    def meta(self):
        return self.as_dict["meta"]
