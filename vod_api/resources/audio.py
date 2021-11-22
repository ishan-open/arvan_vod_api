from .base import Base


class Audio(Base):
    """Audio"""

    def __init__(self, api_key: str):
        super(Audio, self).__init__(api_key)

    def get_audio(self):
        """Return the specified audio."""
        pass

    def post_audio(self):
        """Store a newly created audio."""
        pass

    def update_audio(self):
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
        pass
