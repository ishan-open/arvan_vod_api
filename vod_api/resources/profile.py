import requests

from .base import Base
from ..responses import (
    GetProfilesResponse, GetProfileResponse,
    PostProfileResponse, DeleteResponse,
)

class Profile(Base):
    def __init__(self, api_key: str):
        super(Profile, self).__init__(api_key)

    def get_profiles(
            self,
            channel: str,
            filter: str = None,
            page: int = None,
            per_page: int = None
        ) -> GetProfilesResponse:
        """
        Return all channel's profiles. 

        Parameters
        ----------
        channel : str
            The Id of channel

        filter : str
            Filter result

        page : int
            Page number

        per_page : int
            Page limit

        Returns
        -------
        GetProfilesResponse

        Example
        -------
        >>> profiles = api.profile.get_profiles(channel_id).data
        >>> for p in profiles:
        >>>     print(p.id, p.title)
        """
        parameters = {
            "filter": filter,
            "page": page,
            "per_page": per_page
        }
        return GetProfilesResponse(requests.get(
                self._get_profiles_url(channel), params=parameters, headers=self.auth
            ))

    def get_profile(
            self,
            profile: str
        ) -> GetProfileResponse:
        """
        Return the specified profile. 

        Parameters
        ----------
        profile : str
            The Id of profile

        Returns
        -------
        GetProfileResponse

        Example
        -------
        >>> x = api.profile.get_profile(profile_id).data
        >>> print(x.id)
        >>> print(x.title)
        """
        return GetProfileResponse(requests.get(
                self._get_profile_url(profile), headers=self.auth
            ))

    def post_profile(
            self,
            channel: str,
            title: str,
            descripton: str = None,
            convert_mode: str = "auto",
            thumbnail_time : int = None,
            watermark_id: str = None,
            watermark_area: str = None,
            convert_info: list = None,
            options: list = None
        ) -> PostProfileResponse:
        """
        Store a newly created profile. 

        Parameters
        ----------
        channel : str
            The Id of channel

        title : str
            Title of the profile

        description : str
            Description of the profile

        convert_mode : str
            Enum: "auto" "manual"
            Convert mode

        thumbnail_time : int
            Screenshot time for generate thumbnail for video in seconds

        watermark_id : str
            If you want to use watermark for a video, use this ID

        watermark_area : str
            Enum: "CENTER" "FIX_TOP_LEFT" "FIX_TOP_RIGHT" "FIX_TOP_CENTER" "FIX_BOTTOM_LEFT" "FIX_BOTTOM_RIGHT" "FIX_BOTTOM_CENTER" "ANIMATE_LEFT_TO_RIGHT" "ANIMATE_TOP_TO_BOTTOM"
            Area of the watermark if watermark_id presents

        convert_info : list
            Array of convert details

        options : list
            Array of option details

        Returns
        -------
        PostProfileResponse

        Example
        -------
        >>> x = api.profile.post_profile(channel_id, "my profile", convert_info=[])
        >>> print(x.status_code)
        >>> print(x.data.id)
        >>> print(x.data.title)
        """
        parameters = {
            "title": title,
            "description": descripton,
            "convert_mode": convert_mode,
            "thumbnail_time": thumbnail_time,
            "watermark_id": watermark_id,
            "watermark_area": watermark_area,
            "convert_info": convert_info,
            "options": options
        }

        return PostProfileResponse(requests.post(
                self._get_profiles_url(channel),
                json=parameters,
                headers=self.auth
            ))

    def patch_profile(
            self,
            profile: str,
            title: str = None,
            description: str = None,
            convert_mode: str = None,
            thumbnail_time: int = None,
            watermark_id: str = None,
            watermark_area: str = None,
            convert_info: list = None,
            options: list = None,
        ) -> PostProfileResponse:
        """
        Update the specified profile. 

        Parameters
        ----------
        profile : str
            The Id of profile

        title : str
            Title of the profile

        description : str
            Description of the profile

        convert_mode : str
            Enum: "auto" "manual"
            Convert mode

        thumbnail_time : int
            Screenshot time for generate thumbnail for video in seconds

        watermark_id : str
            If you want to use watermark for a video, use this ID

        watermark_area : str
            Enum: "CENTER" "FIX_TOP_LEFT" "FIX_TOP_RIGHT" "FIX_TOP_CENTER" "FIX_BOTTOM_LEFT" "FIX_BOTTOM_RIGHT" "FIX_BOTTOM_CENTER" "ANIMATE_LEFT_TO_RIGHT" "ANIMATE_TOP_TO_BOTTOM",
            Area of the watermark if watermark_id presents

        convert_info : list
            Array of convert details

        options : list
            Array of option details

        Returns
        -------
        PostProfileResponse

        Example
        -------
        >>> x = api.profile.patch_profile(profile_id, title="new title")
        >>> print(x.data.id)
        >>> print(x.data.title)
        """
        parameters = {
            "title": title,
            "description": description,
            "convert_mode": convert_mode,
            "thumbnail_time": thumbnail_time,
            "watermark_id": watermark_id,
            "watermark_area": watermark_area,
            "convert_info": convert_info,
            "options": options
        }
        parameters = {key: value for key, value in parameters.items() if value is not None}

        return PostProfileResponse(requests.patch(
                self._get_profile_url(profile), json=parameters, headers=self.auth
            ))

    def delete_profile(self, profile: str) -> DeleteResponse:
        """
        Remove the specified profile. 

        Parameters
        ----------
        profile : str
            The Id of profile

        Returns
        -------
        DeleteResponse

        Example
        -------
        >>> api.profile.delete_profile(profile_id)
        """
        return DeleteResponse(requests.delete(self._get_profile_url(profile), headers=self.auth))

    def _get_profiles_url(self, channel_id: str) -> str:
        # https://napi.arvancloud.com/vod/2.0/channels/{channel}/profiles
        return f"{self.base_url}/channels/{channel_id}/profiles"

    def _get_profile_url(self, profile_id: str) -> str:
        # https://napi.arvancloud.com/vod/2.0/profiles/{profile}
        return f"{self.base_url}/profiles/{profile_id}"
