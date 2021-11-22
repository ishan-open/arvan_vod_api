import requests

from .base import Base
from ..responses import GetChannelsReponse


class Channel(Base):
    def __init__(self, api_key: str):
        super(Channel, self).__init__(api_key)

    def get_channels(
            self, filter: str = None,
            page: int = None, per_page: int = None
        ) -> GetChannelsReponse:
        """
        Return all user's channels.
        
        parameters
        ----------
        filter : str
            Filter result

        page : int
            Page number

        per_page : int
            Page limit
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

    def _get_channels_url(self):
        return f"{self.base_url}/channels"

    def _get_channel_url(self, channel: str):
        return f"{self.base_url}/channels/{channel}"
