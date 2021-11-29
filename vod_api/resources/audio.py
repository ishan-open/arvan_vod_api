import requests

from .base import Base


class Audio(Base):
    """Audio"""

    def __init__(self, api_key: str):
        super(Audio, self).__init__(api_key)

    def get_audio(self):
        """Return the specified audio."""
        pass

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
        ):
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

        Example
        -------

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
        res = requests.post(self._get_audios_url(channel), json=parameters, headers=self.auth)
        print(res.status_code)
        try:
            print(res.json())
        except:
            print(res.content)

    def patch_audio(self):
        """Update the specified audio. """
        pass

    def delete_audio(self):
        """Remove the specified audio. """
        pass

    def get_audios(
                self,
                channel: str,
                filter: str = None,
                page: int = None,
                per_page: int = None,
                secure_ip: str = None,
                secure_expire_time: int = None
            ):
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
        """
        res = requests.get(self._get_audios_url(channel), headers=self.auth)
        print(res.status_code)
        try:
            print(res.json())
        except:
            print(res.content)
    
    def _get_audios_url(self, channel_id: str) -> str:
        # https://napi.arvancloud.com/vod/2.0/channels/{channel}/audios
        return f"{self.base_url}/channels/{channel_id}/audios"

    def _get_audio_url(self, audio_id) -> str:
        # https://napi.arvancloud.com/vod/2.0/audios/{audio}
        return f"{self.base_url}/audios/{audio_id}"
