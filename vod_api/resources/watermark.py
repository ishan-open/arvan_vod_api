import requests

from .base import Base
from ..responses import (
    GetWatermarksResponse, PostWatermarkResponse,
    GetWatermarkResponse, DeleteWatermarkResponse,
)

class Watermark(Base):
    def __init__(self, api_key: str):
        super(Watermark, self).__init__(api_key)

    def get_watermarks(
            self,
            channel: str,
            filter: str = None,
            page: int = None,
            per_page: int = None,
            secure_ip: str = None,
            secure_expire_time: int = None,
        ) -> GetWatermarksResponse:
        """
        Return all channel's watermarks.
        
        Parameters
        ----------
        channel : str
            The Id of channel
        
        filter : str
            Filter result

        page : int
            Page number

        per_page : int
            Page limit for query

        secure_ip : str
            The IP address for generate secure links for.
            If channel is secure default is request IP

        secure_expire_time : int
            The Unix Timestamp for expire secure links.
            * If channel is secure default is 24 hours later from now

        Returns
        -------
        GetWatermarksResponse

        Example
        -------
        >>> watermarks = api.watermark.get_watermarks(channel_id).data
        >>> for water in watermarks:
        >>>     print(water.id)
        >>>     print(water.title)
        """
        parameters = {
            "filter": filter,
            "page": page,
            "per_page": per_page,
            "secure_ip": secure_ip,
            "secure_expire_time": secure_expire_time
        }

        return GetWatermarksResponse(requests.get(
            self._get_watermarks_url(channel),
            params=parameters,
            headers=self.auth
        ))

    def get_watermark(self, watermark: str) -> GetWatermarkResponse:
        """
        Return the specified watermark.
        
        Parameters
        ----------
        watermark : str
            The Id of watermark

        Returns
        -------
        GetWatermarkResponse

        Example
        -------
        >>> x = api.watermark.get_watermark(watermark_id).data
        >>> print(x.id)
        >>> print(x.title)
        >>> print(x.url)
        """
        return GetWatermarkResponse(requests.get(
                self._get_watermark_url(watermark),
                headers=self.auth
            ))

    def post_watermark(
            self,
            channel: str,
            title: str,
            watermark: str,
            description: str = None
        ) -> PostWatermarkResponse:
        """
        Store a newly created Watermark.
        
        Parameters
        ----------
        channel : str
            The Id of channel

        title : str
            Title of watermark

        watermark : str
            string <binary>, Watermark file

        description : str
            Description of watermark
        
        Returns
        -------
        PostWatermarkResponse

        Example
        -------
        >>> file_name = "photo.jpg"
        >>> with open(file_name, "rb") as file:
        >>>     x = api.watermark.post_watermark(channel_id, "linux watermark", file, "this is desc" )
        >>>     print(x.message)
        >>>     print(x.data.id)
        >>>     print(x.data.id)
        """
        file = {
            "watermark": watermark,
        }
        parameters = {
            "title": title,
            "description": description
        }

        return PostWatermarkResponse(requests.post(
                self._get_watermarks_url(channel),
                data=parameters,
                files=file,
                headers=self.auth
            ))

    def patch_watermark(
            self,
            watermark: str,
            title: str = None,
            description: str = None,
        ) -> PostWatermarkResponse:
        """
        Update the specified watermark.
        
        Parameters
        ----------
        watermark : str
            The Id of watermark

        title : str
            Title of watermark

        description : str
            Description of watermark

        Returns
        -------
        PostWatermarkResponse

        Example
        -------
        >>> x = api.watermark.patch_watermark(watermark_id, description="new desc")
        >>> print(x.message)
        >>> print(x.data.id)
        >>> print(x.data.description)
        """
        parameters = {
            "title": title,
            "description": description
        }

        return PostWatermarkResponse(requests.patch(
                self._get_watermark_url(watermark),
                json=parameters,
                headers=self.auth
            ))

    def delete_watermark(self, watermark: str) -> DeleteWatermarkResponse:
        """
        Remove the specified watermark.
        
        Parameters
        ----------
        watermark : str
            The Id of watermark

        Returns
        -------
        DeleteWatermarkResponse        

        Example
        -------
        >>> x = api.watermark.delete_watermark(watermark_id)
        >>> print(x.message)
        """
        return DeleteWatermarkResponse(requests.delete(
                self._get_watermark_url(watermark),
                headers=self.auth
            ))
    
    def _get_watermarks_url(self, channel_id) -> str:
        # https://napi.arvancloud.com/vod/2.0/channels/{channel}/watermarks
        return f"{self.base_url}/channels/{channel_id}/watermarks"
    
    def _get_watermark_url(self, watermark_id) -> str:
        # https://napi.arvancloud.com/vod/2.0/watermarks/{watermark}
        return f"{self.base_url}/watermarks/{watermark_id}"
