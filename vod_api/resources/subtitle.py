from .base import Base


class Subtitle(Base):
    def __init__(self, api_key: str):
        super(Subtitle, self).__init__(api_key)
