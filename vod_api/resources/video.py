from .base import Base


class Video(Base):
    def __init__(self, api_key: str):
        super(Video, self).__init__(api_key)
