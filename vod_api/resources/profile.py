from .base import Base


class Profile(Base):
    def __init__(self, api_key: str):
        super(Profile, self).__init__(api_key)
