import requests

from .base import Base
from ..responses import (
    GetAudiosResponse, GetAudioResponse,
    PostAudioResponse, DeleteAudioResponse,
)

class Audio(Base):
    """Audio"""

    def __init__(self, api_key: str):
        super(Audio, self).__init__(api_key)

    def get_audio(
        self,
        audio: str,
        secure_ip: str = None,
        secure_expire_time: int = None
        ) -> GetAudioResponse:
        """
        Return the specified audio.

        Parameters
        ----------
        audio : str
            The Id of audio

        secure_ip : str
            The IP address for generate secure links for.
            If channel is secure default is request IP

        secure_expire_time : int
            The Unix Timestamp for expire secure links.
            * If channel is secure default is 24 hours later from now

        Returns
        -------
        GetAudioResponse

        Example
        -------
        >>> audio = api.audio.get_audio("some file id").data
        >>> print(audio.id)
        >>> print(audio.title)
        """
        parameters = {
            "secure_ip": secure_ip,
            "secure_expire_time": secure_expire_time,
        }
        return GetAudioResponse(requests.get(
            self._get_audio_url(audio),
            params=parameters,
            headers=self.auth
        ))

    def post_audio(
            self,
            channel: str,
            title: str,
            description: str = None,
            audio_url : str = None,
            file_id : str = None,
            convert_mode: str = "auto",
            parallel_convert: bool = False,
            convert_info: list = None
        ) -> PostAudioResponse:
        """
        Store a newly created audio.

        Parameters
        ----------
        channel : str
            The Id of channel

        title : str
            Title of the audio

        description : str
            Description of the audio

        audio_url : str
            Public URL of audio

        file_id : str
            ID of the audio file

        convert_mode : str
            Enum: "auto" "manual" "profile" 
            Convert mode

        parallel_convert : bool
            Default: false
            Set this convert parallel when any audio(s) is converting.
            Parallel limit is 3

        convert_info : list
            Array of convert details

        Returns
        -------
        PostAudioResponse

        Example
        -------
        >>> x = api.audio.post_audio(channel_id, "first audio", file_id="some file id")
        >>> x.data # an object with created audio data
        >>> x.data.id # can access to audio's data
        >>> x.data.title
        """
        parameters = {
            "title": title,
            "description": description,
            "audio_url": audio_url,
            "file_id": file_id,
            "convert_mode": convert_mode,
            "parallel_convert": parallel_convert,
            "convert_info": convert_info
        }

        return PostAudioResponse(requests.post(
                self._get_audios_url(channel),
                json=parameters,
                headers=self.auth
            ))

    def patch_audio(
            self, audio: str, title: str = None, description: str = None
        ) -> PostAudioResponse:
        """
        Update the specified audio.

        Parameters
        ----------
        audio : str
            The Id of audio

        title : str
            Title of the audio

        description : str
            Description of the audio

        Returns
        -------
        PostAudioResponse

        Example
        -------
        >>> x = api.audio.patch_audio("some audio id", title="new title")
        >>> x.data # will returns new updated data
        >>> print(x.data.title)  
        """
        parameters = {
            "title": title,
            "description": description
        }
        parameters = {key: value for key, value in parameters.items() if value is not None}

        return PostAudioResponse(requests.patch(
            self._get_audio_url(audio),
            json=parameters,
            headers=self.auth
        ))

    def delete_audio(self, audio: str) -> DeleteAudioResponse:
        """
        Remove the specified audio.
        
        Parameters
        ----------
        audio : str
            The Id of audio

        Returns
        -------
        DeleteAudioResponse

        Example
        -------
        >>> api.audio.delete_audio("some audio id")
        """
        return DeleteAudioResponse(requests.delete(
            self._get_audio_url(audio),
            headers=self.auth
        ))

    def get_audios(
                self,
                channel: str,
                filter: str = None,
                page: int = None,
                per_page: int = None,
                secure_ip: str = None,
                secure_expire_time: int = None
            ) -> GetAudiosResponse:
        """
        Return all channel's audios.

        Parameters
        ---------
        channel : str
            required, The Id of channel

        filter : str
            Filter result

        page : int
            Page number

        per_page : int
            Page limit for query

        secure_ip : str
            The IP address for generate secure links for. If channel is secure default is request IP

        secure_expire_time : int
            The Unix Timestamp for expire secure links. * If channel is secure default is 24 hours later from now
        
        Returns
        -------
        GetAudiosResponse

        Example
        -------
        >>> audios = api.audio.get_audios("some channel id").data
        >>> for audio in audios: # an iterable list with audios data
        >>> print(audio.id, audio.title)
        """
        parameters = {
            "filter": filter,
            "page": page,
            "per_page": per_page,
            "secure_ip": secure_ip,
            "secure_expire_time": secure_expire_time,
        }
        return GetAudiosResponse(requests.get(
                self._get_audios_url(channel),
                params=parameters,
                headers=self.auth
            ))

    def _get_audios_url(self, channel_id: str) -> str:
        # https://napi.arvancloud.com/vod/2.0/channels/{channel}/audios
        return f"{self.base_url}/channels/{channel_id}/audios"

    def _get_audio_url(self, audio_id) -> str:
        # https://napi.arvancloud.com/vod/2.0/audios/{audio}
        return f"{self.base_url}/audios/{audio_id}"
