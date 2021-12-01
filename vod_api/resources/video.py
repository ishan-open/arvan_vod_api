import requests

from .base import Base
from ..responses import (
    PostVideoResponse, GetVideosResponse,
    GetVideoResponse, DeleteVideoResponse,
)


class Video(Base):
    def __init__(self, api_key: str):
        super(Video, self).__init__(api_key)

    def get_videos(
        self,
        channel: str,
        filter: str = None,
        page: int = None,
        per_page: int = None,
        secure_ip: str = None,
        secure_expire_time: int = None
        ) -> GetVideosResponse:
        """
        Return all channel's videos. 

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
        GetVideosResponse

        Example
        -------
        >>> videos = api.video.get_videos("some channel id").data
        >>> for video in videos: # an iterable list with videos data
        >>>     print(video.id)
        >>>     print(video.title)
        """
        parameters = {
            "channel": channel,
            "filter": filter,
            "page": page,
            "per_page": per_page,
            "secure_ip": secure_ip,
            "secure_expire_time": secure_expire_time
        }

        return GetVideosResponse(requests.get(
                self._get_videos_url(channel),
                params=parameters,
                headers=self.auth
            ))

    def get_video(
            self,
            video: str,
            secure_ip: str = None,
            secure_expire_time: str = None
        ) -> GetVideoResponse:
        """
        Return the specified video. 

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
        GetVideoResponse

        Example
        -------
        >>> video = api.video.get_video("some video id").data
        >>> print(video.id)
        >>> print(video.title)
        """
        parameters = {
            "secure_ip": secure_ip,
            "secure_expire_time": secure_expire_time,
        }
        return GetVideoResponse(requests.get(
                self._get_video_url(video),
                params=parameters,
                headers=self.auth
            ))

    def post_video(
            self,
            channel: str,
            title: str,
            description: str = None,
            video_url: str = None,
            file_id: str = None,
            convert_mode: str = "auto",
            profile_id: str = None,
            parallel_convert: bool = False,
            thumbnail_time: int = 0,
            watermark_id: str = None,
            watermark_area: str = "CENTER",
            convert_info: list = None,
            options: list = None
        ) -> PostVideoResponse:
        """
        Store a newly created video.

        Parameters
        ----------
        channel : str
            Title of the Channel

        title : str
            Title of the video

        description : str
            Description of the video

        video_url : str
            Public URL of video

        file_id : str
            ID of the video file

        convert_mode : str
            Enum: "auto" "manual" "profile" , Convert mode
        
        profile_id : str
            The profile ID that video convert with it (priority is with video properties)

        parallel_convert : bool
            Default: false
            Set this convert parallel when any video(s) is converting.
            Parallel limit is 3

        thumbnail_time : int
            Screenshot time for generate thumbnail for video in seconds

        watermark_id : str
            If you want to use watermark for a video, use this ID

        watermark_area : str
            Enum: "CENTER" "FIX_TOP_LEFT" "FIX_TOP_RIGHT" "FIX_TOP_CENTER" "FIX_BOTTOM_LEFT" "FIX_BOTTOM_RIGHT" "FIX_BOTTOM_CENTER" "ANIMATE_LEFT_TO_RIGHT" "ANIMATE_TOP_TO_BOTTOM"
            Area of the watermark if watermark_id presents

        convert_info : list
            Array of convert details

        opetions : list
            Array of option details

        Returns
        -------
        PostVideoResponse

        Example
        -------
        >>> x = api.video.post_video("some channel id", "title", file_id="some video file id")
        >>> x.data # an object with created video's data
        >>> x.data.id
        >>> x.data.title
        """
        parameters = {
            "title": title,
            "description": description,
            "video_url": video_url,
            "file_id": file_id,
            "convert_mode": convert_mode,
            "profile_id": profile_id,
            "parallel_convert": parallel_convert,
            "thumbnail_time": thumbnail_time,
            "watermark_id": watermark_id,
            "watermark_area": watermark_area,
            "convert_info": convert_info,
            "options": options
        }

        return PostVideoResponse(requests.post(
                self._get_videos_url(channel),
                json=parameters,
                headers=self.auth
            ))

    def patch_video(
            self,
            video: str,
            title: str = None,
            description: str = None
        ) -> PostVideoResponse:
        """
        Update the specified video. 

        Parameters
        ----------
        video : str
            The Id of video

        title : str
            Title of the video

        description : str
            Description of the video
        
        Returns
        -------
        PostVideoResponse

        Example
        -------
        >>> x = api.video.patch_video("some video id", title="new title").data
        >>> x.title # will access to new video's data
        """
        parameters = {
            "title": title,
            "description": description,
        }
        parameters = {key: value for key, value in parameters.items() if value is not None}

        return PostVideoResponse(requests.patch(
                self._get_video_url(video),
                json=parameters,
                headers=self.auth
            ))

    def delete_video(self, video: str) -> DeleteVideoResponse:
        """
        Remove the specified video. 

        Parameters
        ----------
        video : str
            The Id of video

        Returns
        -------
        DeleteVideoResponse

        Example
        -------
        >>> api.video.delete_video("some video id").message
        """
        return DeleteVideoResponse(requests.delete(
            self._get_video_url(video), headers=self.auth
        ))

    def _get_videos_url(self, channel_id: str) -> str:
        # https://napi.arvancloud.com/vod/2.0/channels/{channel}/videos
        return f"{self.base_url}/channels/{channel_id}/videos"

    def _get_video_url(self, video_id: str) -> str:
        # https://napi.arvancloud.com/vod/2.0/videos/{video}
        return f"{self.base_url}/videos/{video_id}"
