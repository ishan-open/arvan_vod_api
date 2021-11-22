from .base import Base


class AudioTrack(Base):
    def __init__(self, api_key: str):
        super(AudioTrack, self).__init__(api_key)
