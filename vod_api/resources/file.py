import requests
import base64
import mimetypes

from .base import Base
from ..responses import (
    PostFileResponse, HeadFileResponse,
    GetFilesResponse, PatchFileResponse,
    GetFileResponse, DeleteResponse
)


class File(Base):
    def __init__(self, api_key: str):
        super(File, self).__init__(api_key)

    def get_files(self, channel: str, filter: str = None) -> GetFilesResponse:
        """
        Return all draft files of channel. 

        Parameters
        ----------
        channel : str
            The Id of channel

        filter : str
            Filter result

        Returns
        -------
        GetFilesResponse

        Examples
        --------
        >>> files = api.file.get_files("some channel id").data # list of files
        >>> for file in files: # it's an iterable list with every file's data
        >>>     print(file.id) # can access to file's data
        """
        parameters = {
            "filter": filter
        }

        return GetFilesResponse(requests.get(
                self._get_files_url(channel),
                params=parameters,
                headers=self.auth,
            ))

    def get_file(self, file: str) -> GetFileResponse:
        """
        Return the specified file.

        Parameters
        ----------
        file : str
            The Id of file

        Returns
        -------
        GetFileResponse

        Example
        -------
        >>> file = api.file.get_file("some file id").data
        >>> file.id
        >>> file.filename
        """
        return GetFileResponse(requests.get(
                self._get_file_url(file), headers=self.auth
            ))

    def post_file(
            self,
            channel: str,
            upload_length: int,
            upload_metadata: str,
            tus_resumable: str = "1.0.0"
        ) -> PostFileResponse:
        """
        Request a new upload file.

        Parameters
        ----------
        channel : str
            The Id of channel

        upload_length : int
            To indicate the size of entire upload in bytes

        upload_metadata: str
            To add additional metadata to the upload creation request.
            * MUST contain 'filename' and 'filetype'.
            From all available fields only these two fields will be used.
            * MUST consist of one or more comma-separated key-value pairs.
            * The key and value MUST be separated by a space.
            * The key MUST NOT contain spaces and commas and MUST NOT be empty.
            * The key SHOULD be ASCII encoded and the value MUST be Base64 encoded.

        tus_resumable : str
             Default: '1.0.0', version of tus.io

        Returns
        -------
        PostFileResponse

        Examples
        --------
        >>> length = 123256
        >>> metadata = "filename ZGphbmdvLm1wNA==,filetype dmlkZW8vbXA0"
        >>> x = api.file.post_file(channel_id, length, metadata)
        >>> x.file_id
        >>> x.file_location
        """
        parameters = {
            "tus-resumable": tus_resumable,
            "upload-length": str(upload_length),
            "upload-metadata": upload_metadata,
        }
        parameters.update(self.auth)

        return PostFileResponse(requests.post(
                self._get_files_url(channel), headers=parameters
            ))

    def head_file(self, channel: str, file: str) -> HeadFileResponse:
        """
        Get upload offset. See https://tus.io/ for more detail. 

        Parameters
        ----------
        channel : str
            The Id of channel

        file : str
            The Id of file

        Returns
        -------
        HeadFileResponse

        Example
        -------
        >>> x = api.file.get_upload_offset(channel_id, file_id)
        >>> x.upload_offset
        >>> x.upload_length
        """
        return HeadFileResponse(requests.head(
                self._get_channel_file_url(channel, file), headers=self.auth
            ))

    def patch_file(
        self,
        channel: str,
        file: str,
        data: bytes,
        upload_offset: int = 0,
        content_type: str = "application/offset+octet-stream",
        tus_resumable: str = "1.0.0"
        ) -> PatchFileResponse:
        """
        Upload and apply bytes to a file. See https://tus.io/ for more detail. 

        Parameters
        ----------
        channel : str
            The Id of channel

        file : str
            The Id of file

        data : bytes
            chunked file as bytes

        upload_offset : int
            request and response header indicates a byte offset within a resource.
            * For uploading entire file in one request, set this to '0'

        content_type : str
            Request content type

        tus_resumable : str
            Request content type

        Returns
        -------
        PatchFileResponse

        Example
        -------
        >>> with open(file_name, "rb") as f:
        >>>     data = f.read(1024*1024)
        >>>     while data:
        >>>         x = api.file.upload_chunk(channel_id, file_id, data)
        >>>         print(x.status_code, x.upload_offset)
        >>>         data = f.read(1024*1024)
        """
        parameters = {
            "tus-resumable": tus_resumable,
            "upload-offset": str(upload_offset),
            "Content-Type": content_type,

        }
        parameters.update(self.auth)

        return PatchFileResponse(requests.patch(
                self._get_channel_file_url(channel, file),
                headers=parameters,
                data=data
            ))

    def delete_file(self, file: str) -> DeleteResponse:
        """
        Remove the specified file. 

        Parameters
        ----------
        file : str
            The Id of file

        Returns
        -------
        DeleteResponse

        Example
        -------
        >>> api.file.delete_file("some file id)
        """
        return DeleteResponse(requests.delete(
                self._get_file_url(file), headers=self.auth
            ))

    def _get_files_url(self, channel_id: str):
        # "https://napi.arvancloud.com/vod/2.0/channels/{channel}/files"
        return f"{self.base_url}/channels/{channel_id}/files"
    
    def _get_channel_file_url(self, channel_id: str, file_id: str):
        # "https://napi.arvancloud.com/vod/2.0/channels/{channel}/files"
        return f"{self.base_url}/channels/{channel_id}/files/{file_id}"

    def _get_file_url(self, file_id: str):
        # https://napi.arvancloud.com/vod/2.0/files/{file}
        return f"{self.base_url}/files/{file_id}"

