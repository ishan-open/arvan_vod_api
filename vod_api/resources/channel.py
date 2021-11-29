import requests

from .base import Base
from ..responses import (
    GetChannelsReponse, PostChannelResponse,
    DeleteChannelResponse, GetChannelReponse,
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

        Examples
        --------
        >>> x = api.channel.get_channels()
        >>> channels = x.data   # an iterable list with channels object data
        >>> for channel in channels: # can access to every channel's data
        >>>     print(channel.title)
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

        Examples
        --------
        >>> x = api.channel.post_channel(title="testing", description="desc")
        >>> x.data      # an object with created channel data
        >>> x.data.id   # can access to created channel data
        >>> x.data.title
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

    def delete_channel(self, channel: str) -> DeleteChannelResponse:
        """
        Remove the specified channel. 

        Parameters
        ----------
        channel : str
            The Id of channel

        Returns
        -------
        DeleteChannelResponse

        Examples
        --------
        >>> x = api.channel.delete_channel("some channel id")
        >>> print(x.message) # will print ' channel deleted successfully '
        """

        return DeleteChannelResponse(requests.delete(
                self._get_channel_url(channel), headers=self.auth
            ))

    def get_channel(self, channel: str) -> GetChannelReponse:
        """
        Return the specified channel. 

        Parameters
        ----------
        channel : str
            The Id of channel

        Returns
        -------
        GetChannelReponse

        Examples
        --------
        >>> x = api.channel.get_channel("some channel id")
        >>> x.data      # an object with channel's data
        >>> x.data.tile # can access to channel's data
        >>> x.data.id
        """

        return GetChannelReponse(requests.get(
                self._get_channel_url(channel), headers=self.auth
            ))

    def patch_channel(
            self,
            channel: str,
            title: str = None,
            description: str = None,
            secure_link_enabled: bool = None,
            secure_link_key: str = None,
            secure_link_with_ip: bool = True,
            ads_enabled: bool = False,
            present_type: str = None,
            campaign_id: str = None,
        ) -> PostChannelResponse:
        """
        Update the specified channel. 

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

        Examples
        --------
        >>> x = api.channel.update_channel("some channel id", title="new title")
        >>> x.data # can access to updated channel's data
        >>> x.data.id
        >>> x.data.title
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
        parameters = {key: value for key, value in parameters.items() if value is not None}

        return PostChannelResponse(requests.patch(
                self._get_channel_url(channel),
                headers=self.auth,
                json=parameters
            ))

    def _get_channels_url(self):
        return f"{self.base_url}/channels"

    def _get_channel_url(self, channel: str):
        return f"{self.base_url}/channels/{channel}"
