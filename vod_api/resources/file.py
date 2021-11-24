import requests
import base64
import mimetypes

from .base import Base


class File(Base):
    def __init__(self, api_key: str):
        super(File, self).__init__(api_key)

    def get_files(self, channel: str, filter: str = None):
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

        Examples
        --------

        """
        parameters = {
            "filter": filter
        }

        res = requests.get(
            self._get_files_url(channel), params=parameters, headers=self.auth
            )

        print(res.status_code)
        try:
            print(res.json())
        except:
            print(res.content)

    def post_file(
            self,
            channel: str,
            upload_length: int,
            upload_metadata: str,
            tus_resumable: str = "1.0.0"
        ):
        """
        Request a new upload file.

        Parameters
        ----------
        channel : str
            The Id of channel

        upload-length : int
            To indicate the size of entire upload in bytes

        upload-metadata: str
            To add additional metadata to the upload creation request.
            * MUST contain 'filename' and 'filetype'.
            From all available fields only these two fields will be used.
            * MUST consist of one or more comma-separated key-value pairs.
            * The key and value MUST be separated by a space.
            * The key MUST NOT contain spaces and commas and MUST NOT be empty.
            * The key SHOULD be ASCII encoded and the value MUST be Base64 encoded.

        tus-resumable : str
             Default: '1.0.0', version of tus.io

        
        """
        pass

    def _get_files_url(self, channel_id: str):
        # "https://napi.arvancloud.com/vod/2.0/channels/{channel}/files"
        return f"{self.base_url}/channels/{channel_id}/files"
    
    def _get_file_url(self, file_id: str):
        # https://napi.arvancloud.com/vod/2.0/files/{file}
        return f"{self.base_url}/files/{file_id}"

