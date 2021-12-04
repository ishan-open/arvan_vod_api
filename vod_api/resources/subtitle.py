import requests

from .base import Base
from ..responses import (
    GetSubtitleResponse, GetSubtitlesResponse,
    PostSubtitleResponse, DeleteSubtitleResponse,
)


class Subtitle(Base):
    def __init__(self, api_key: str):
        super(Subtitle, self).__init__(api_key)
    
    def get_subtitle(
            self,
            subtitle: str,
            secure_ip: str = None,
            secure_expire_time: int = None
        ) -> GetSubtitleResponse:
        """
        Return the specified subtitle. 

        Parameters
        ----------
        subtitle : str
            The Id of subtitle

        secure_ip : str
            The IP address for generate secure links for.
            If channel is secure default is request IP

        secure_expire_time : int
            The Unix Timestamp for expire secure links.
            * If channel is secure default is 24 hours later from now

        Returns
        -------
        GetSubtitleResponse

        Example
        -------
        >>> x = api.subtitle.get_subtitle(subtitle_id).data
        >>> print(x.lang)
        >>> print(x.url)
        """
        parameters = {
            "secure_ip": secure_ip,
            "secure_expire_time": secure_expire_time
        }

        return GetSubtitleResponse(requests.get(
                self._get_subtitle_url(subtitle),
                params=parameters,
                headers=self.auth
            ))

    def get_subtitles(
            self,
            video: str,
            secure_ip: str = None,
            secure_expire_time: int = None
        ) -> GetSubtitlesResponse:
        """
        Display a listing of the subtitle.

        Parameters
        ----------
        video : str
            The Id of video

        secure_ip : str
            The IP address for generate secure links for.
            If channel is secure default is request IP

        secure_expire_time : int
            The Unix Timestamp for expire secure links.
            * If channel is secure default is 24 hours later from now

        Returns
        -------
        GetSubtitlesResponse

        Example
        -------

        """
        parameters = {
            "secure_ip": secure_ip,
            "secure_expire_time": secure_expire_time
        }

        return GetSubtitlesResponse(requests.get(
                self._get_subtitles_url(video),
                params=parameters,
                headers=self.auth
            ))

    def post_subtitle(
            self,
            video: str,
            lang: str,
            subtitle: str
        ) -> PostSubtitleResponse:
        """
        Store a newly created subtitle.

        Parameters
        ----------
        video : str
            The Id of video

        lang : str
            Enum: "fa", "en", "es", "it", "ko", "de", "fr", "ru", "hi", "ar", "pt", and ...
            Subtitle language

        subtitle : str
            string <binary>, The SRT or VTT subtitle file.
        
        Returns
        -------
        PostSubtitleResponse

        Example
        -------
        >>> file_name = "subtitle.srt"
        >>> with open(file_name, "rb") as file:
        >>>     x = api.subtitle.post_subtitle(video_id, "fa", file)
        >>>     print(x.message)
        >>>     print(x.data.id)
        """
        file = {
            "subtitle": subtitle
        }

        parameters = {
            "lang": lang
        }

        return PostSubtitleResponse(requests.post(
                self._get_subtitles_url(video),
                files=file,
                data=parameters,
                headers=self.auth
            ))

    def delete_subtitle(self, subtitle: str) -> DeleteSubtitleResponse:
        """
        Remove the specified subtitle. 

        Parameters
        ----------
        sutitle : str
            The Id of subtitle

        Returns
        -------
        DeleteSubtitleResponse

        Example
        -------
        >>> api.subtitle.delete_subtitle("some subtitle id")
        """
        return DeleteSubtitleResponse(requests.delete(
                self._get_subtitle_url(subtitle), headers=self.auth
            ))

    def _get_subtitles_url(self, video_id: str):
        # https://napi.arvancloud.com/vod/2.0/videos/{video}/subtitles
        return f"{self.base_url}/videos/{video_id}/subtitles"
    
    def _get_subtitle_url(self, subtitle_id):
        # https://napi.arvancloud.com/vod/2.0/subtitles/{subtitle}
        return f"{self.base_url}/subtitles/{subtitle_id}"
