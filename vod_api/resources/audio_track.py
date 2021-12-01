import requests

from .base import Base
from ..responses import (
    GetAudioTracksResponse, GetAudioTrackResponse,
    PostAudioTrackResponse, DeleteAudioTrackResponse,
)


class AudioTrack(Base):
    def __init__(self, api_key: str):
        super(AudioTrack, self).__init__(api_key)

    def get_audio_tracks(
            self,
            video: str,
            secure_ip: str = None,
            secure_expire_time: int = None
        ) -> GetAudioTracksResponse:
        """
        Display a listing of the Audio Tracks. 

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
        GetAudioTracksResponse

        Example
        -------
        >>> audio_tracks = api.audio_track.get_audio_tracks(video_id).data
        >>> for at in audio_tracks: # an iterable list with audio tracks data
        >>>    print(at.id, at.url)
        """
        parameters = {
            "secure_ip": secure_ip,
            "secure_expire_time": secure_expire_time
        }

        return GetAudioTracksResponse(requests.get(
            self._get_audio_tracks_url(video),
            params=parameters,
            headers=self.auth
        ))

    def get_audio_track(
            self,
            audio_track: str,
            secure_ip: str = None,
            secure_expire_time: int = None
        ) -> GetAudioTrackResponse:
        """
        Return the specified audio track. 

        Parameters
        ----------
        audio_track : str
            The Id of audio track

        secure_ip : str
            The IP address for generate secure links for.
            If channel is secure default is request IP

        secure_expire_time : int
            The Unix Timestamp for expire secure links.
            * If channel is secure default is 24 hours later from now
        
        Returns
        -------
        GetAudioTrackResponse

        Example
        -------
        >>> x = api.audio_track.get_audio_track("some audio track id")
        >>> x.data # an object with audio track data
        >>> x.data.id # can access to audio track data
        >>> x.data.url
        """
        parameters = {
            "secure_ip": secure_ip,
            "secure_expire_time": secure_expire_time
        }

        return GetAudioTrackResponse(requests.get(
            self._get_audio_track_url(audio_track),
            params=parameters,
            headers=self.auth
        ))

    def post_audio_track(
            self,
            video: str,
            lang: str,
            audio_track: str
        ) -> PostAudioTrackResponse:
        """
        Store a newly created audio track.
        
        Parameters
        ----------
        video : str
            The Id of video

        lang : str
            Enum: "fa", "en", "es", "it", "ko", "de", "fr", "ru", "hi", "ar", "pt", and ...
            Track language

        audio_track : str
            The Mp3 or ACC Audio file.
        
        Returns
        -------
        PostAudioTrackResponse

        Example
        -------
        >>> with open("some file name", "rb") as file:
        >>>    x = api.audio_track.post_audio_track("some video id", "en", file)
        >>>    x = x.data # an object with created AudioTrack's data
        >>>    print(x.data.id)
        """
        file = {
            "audio_track": audio_track,
        }
        parameters = {
            "lang": lang,
        }

        return PostAudioTrackResponse(requests.post(
                self._get_audio_tracks_url(video),
                data=parameters,
                files=file,
                headers=self.auth
            ))

    def delete_audio_track(self, audio_track: str) -> DeleteAudioTrackResponse:
        """
        Remove the specified audio track. 

        Parameters
        ----------
        audio_track : str
            The Id of audio track

        Returns
        -------
        DeleteAudioTrackResponse

        Example
        -------
        >>> 
        """
        return DeleteAudioTrackResponse(requests.delete(
                self._get_audio_track_url(audio_track), headers=self.auth
            ))

    def _get_audio_tracks_url(self, video_id: str) -> str:
        # https://napi.arvancloud.com/vod/2.0/videos/{video}/audio-tracks
        return f"{self.base_url}/videos/{video_id}/audio-tracks"
    
    def _get_audio_track_url(self, audio_track_id: str) -> str:
        # https://napi.arvancloud.com/vod/2.0/audio-tracks/{audio_track}
        return f"{self.base_url}/audio-tracks/{audio_track_id}"
