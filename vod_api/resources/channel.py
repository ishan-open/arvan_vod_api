import requests

from .base import Base
from ..responses import (
    GetChannelsReponse, PostChannelResponse,
)


class Channel(Base):
    def __init__(self, api_key: str):
        super(Channel, self).__init__(api_key)

    def get_channels(
                self,
                filter: str = None,
                page: int = None,
                per_page: int = None
            ) -> GetChannelsReponse:
        """
        Return all user's channels.

        Parameters
        ----------
        filter : str
            Filter result

        page : int
            Page number

        per_page : int
            Page limit
        
        Returns
        -------
        GetChannelsReponse
        """

        params = {
            "filter": filter,
            "page": page,
            "per_page": per_page
        }
        return GetChannelsReponse(requests.get(
                self._get_channels_url(),
                headers=self.auth,
                params=params
            ))

    def post_channel(
                self,
                title: str,
                description: str = None,
                secure_link_enabled: bool = False,
                secure_link_key: str = None,
                secure_link_with_ip: bool = True,
                ads_enabled: bool = False,
                present_type: str = "auto",
                campaign_id: str = None,
            ) -> PostChannelResponse:
        """
        Store a newly channel. 

        Parameters
        ----------
        title : str
            required, Title of channel

        description : str
            Description of channel

        secure_link_enabled : bool
            Enable or disable secure link for all videos in channel

        secure_link_key : str
            Key for generate secure links

        secure_link_with_ip : bool
            IP can be considered as an optional parameter

        ads_enabled : bool
            Enable or disable Ads for all videos in channel

        present_type : str
             Enum: "auto" and "manual", Ads present method

        campaign_id : str
            Created CampaignId in Ads

        Returns
        -------
        PostChannelResponse
        """

        parameters = {
            "title": title,
            "description": description,
            "secure_link_enabled": secure_link_enabled,
            "secure_link_key": secure_link_key,
            "secure_link_with_ip": secure_link_with_ip,
            "ads_enabled": ads_enabled,
            "present_type": present_type,
            "campaign_id": campaign_id
        }

        return PostChannelResponse(requests.post(
            self._get_channels_url(),json=parameters,headers=self.auth
            ))

    def _get_channels_url(self):
        return f"{self.base_url}/channels"

    def _get_channel_url(self, channel: str):
        return f"{self.base_url}/channels/{channel}"
